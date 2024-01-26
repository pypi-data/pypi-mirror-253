import ast
import json
import logging
import tempfile
import time
import uuid
import webbrowser
import zipfile
from pathlib import Path
import contextlib

import darwin
import darwin.importer as importer
import fiftyone as fo
import fiftyone.core.labels as fol
import fiftyone.core.media as fomm
import fiftyone.core.metadata as fom
import fiftyone.utils.annotations as foua
import requests

from darwin.client import Client
from darwin.exceptions import NotFound
from darwin.importer import get_importer
from darwin.importer.importer import get_remote_files
from darwin.cli_functions import remove_remote_dataset


logger = logging.getLogger(__name__)

_DEBUG = False

class DarwinBackendConfig(foua.AnnotationBackendConfig):
    def __init__(
        self,
        name,
        label_schema,
        media_field="filepath",
        api_key=None,
        dataset_slug=None,
        atts=None,
        external_storage=None,
        base_url = "https://darwin.v7labs.com/api/v2/teams",
        item_name_annotation=False,
        **kwargs,
    ):
        super().__init__(
            name=name, label_schema=label_schema, media_field=media_field, **kwargs
        )

        self.dataset_slug = dataset_slug
        self.atts = atts
        self.external_storage = external_storage
        self.base_url = base_url
        self._api_key = api_key
        self.item_name_annotation = item_name_annotation

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
        
    def load_credentials(self, api_key=None):
        self._load_parameters(api_key=api_key)


class DarwinBackend(foua.AnnotationBackend):

    @property
    def supported_media_types(self):
        return [fomm.IMAGE, fomm.VIDEO]


    @property
    def supported_label_types(self):
        return [
            "classification",
            "classifications",
            "detection",
            "detections",
            "polygon",
            "polygons",
            "keypoint",
            "keypoints",
        ]

    @property
    def supported_attr_types(self):
        return []

    @property
    def supports_keyframes(self):
        return True

    @property
    def supports_video_sample_fields(self):
        return False

    @property
    def requires_label_schema(self):
        return True

    def recommend_attr_tool(self, name, value):
        return {"type": "text"}

    def requires_attr_values(self, attr_type):
        return attr_type != "text"

    def upload_annotations(self, samples, anno_key, launch_editor=False):
        api = self.connect_to_api()
        results = api.upload_annotations(samples, anno_key, self)

        if launch_editor:
            results.launch_editor()

        return results

    def download_annotations(self, results):
        api = self.connect_to_api()

        logger.info("Downloading labels from V7 Darwin...")
        annotations = api.download_annotations(results)
        logger.info("Download complete")

        return annotations

    def _connect_to_api(self):
        return DarwinAPI(
            api_key=self.config._api_key,
        )


class DarwinAPI(foua.AnnotationAPI):
    def __init__(self, api_key):
        super().__init__()
        self._client = Client.from_api_key(api_key)
        self._api_key = api_key

    def upload_annotations(self, samples, anno_key, backend):

        logger.info('upload anns')
        
        """Uploads annotations to Darwin"""
        label_schema = backend.config.label_schema
        media_field = backend.config.media_field
        external_storage = backend.config.external_storage
        base_url = backend.config.base_url

        logger.debug(f'label_schema: {str(label_schema)}')

        if backend.config.dataset_slug is None:
            backend.config.dataset_slug = f"voxel51-{uuid.uuid4().hex}"

        try:
            dataset = self._client.get_remote_dataset(backend.config.dataset_slug)
        except darwin.exceptions.NotFound:
            dataset = self._client.create_dataset(backend.config.dataset_slug)

        # External Storage Logic
        if external_storage:
            result = _register_items(
                samples,
                backend.config.api_key,
                dataset.slug,
                dataset.team,
                external_storage,
                base_url
            )

        else:
            logging.info("Paths to upload",samples.values(media_field))
            result = dataset.push(files_to_upload=samples.values(media_field))

        filename_sample_id_map = {
            Path(sample[media_field]).name: sample.id for sample in samples
        }

        if external_storage:
            item_sample_map = {
                item.get("id"): {
                    "filename": item.get("name"),
                    "sample_id": filename_sample_id_map[item.get("name")],
                }
                for item in _list_items(
                    backend.config.api_key, dataset.dataset_id, dataset.team,base_url
                )
            }
        else:
            item_sample_map = {
                item.dataset_item_id: {
                    "filename": item.filename,
                    "sample_id": filename_sample_id_map[item.filename],
                }
                for item in result.blocked_items + result.pending_items
            }

        self._create_missing_annotation_classes(label_schema, dataset)

        id_maps, frame_id_map = self._upload_annotations(label_schema, samples, media_field, dataset, backend)

        return DarwinResults(
            samples,
            backend.config,
            anno_key,
            id_maps,
            dataset_slug=dataset.slug,
            item_sample_map=item_sample_map,
            backend=backend,
            frame_id_map = frame_id_map,
        )

    def _convert_image_annotations_to_v7(
        self, sample, frame_size, label_schema, id_maps, backend, frame_val=None
    ):
        '''
        id_maps: fo sample.id -> list-of-fo-labelobj-ids
        '''

        darwin_annotations = []
        for label_field, label_info in label_schema.items():
            try:
                if label_field.startswith("frames"):
                    label_field = label_field.split(".")[1]
                label_type0 = label_info["type"]
                label_type = _UNIQUE_TYPE_MAP.get(label_type0, label_type0)
                if label_type0 == "classification":
                    annotations = [sample[label_field]]
                else:
                    annotations = sample[label_field][label_type]

                for annotation in annotations:
                    # Adding attributes import support here (depreated attributes field)
                    attributes = getattr(annotation,'attributes',None)
                    if attributes is not None:
                        attribute_list = [str({key: value}) for key, value in annotation.attributes.items()]
                    else:
                        attribute_list = []

                    # Adding directly populated attributes. Most usual way to add attributes
                    if backend.config.atts:
                        for attribute in backend.config.atts:
                            try:
                                attribute_list.append(str({attribute: annotation[attribute]}))
                            except:
                                pass
                    
                    attributes = attribute_list if attribute_list else None

                    darwin_annotations.extend(
                        self._convert_image_annotation_to_v7(
                            annotation, label_type, frame_size, sample, backend, attributes
                        )
                    )
                    
                    if frame_val:
                        if sample.id not in id_maps:
                            id_maps[sample.id] = {}
                            id_maps[sample.id][frame_val.id] = []
                        id_maps[sample.id][frame_val.id].append(annotation.id)
                    
                    else:
                        if sample.id not in id_maps:
                            id_maps[sample.id] = []
                        id_maps[sample.id].append(annotation.id)

            except:
                pass
        
        return darwin_annotations

    def _convert_image_annotation_to_v7(
        self, annotation, label_type, frame_size, sample,backend, attributes=None
    ):
        
        annotation_label = annotation.label

        #Item name class setting
        if backend.config.item_name_annotation and annotation.label in ["Item","item","ITEM"]:
            external_path = sample.filepath
            path_list = external_path.split("/")
            sample_name = path_list[-1]
            annotation_label = sample_name

        darwin_annotation = _v7_basic_annotation(
            label=annotation_label,
            confidence=annotation.confidence,
            atts=attributes,
        )

        if label_type == "detections":
            darwin_annotation["bounding_box"] = _51_to_v7_bbox(
                annotation.bounding_box, frame_size
            )
            return [darwin_annotation]

        if label_type == "classifications":
            darwin_annotation["tag"] = {}
            return [darwin_annotation]

        if label_type == "keypoints":
            darwin_annotations = []
            for point in annotation.points:
                darwin_annotation_kp = darwin_annotation.copy()
                darwin_annotation_kp["keypoint"] = _51_to_v7_keypoint(point, frame_size)
                darwin_annotations.append(darwin_annotation_kp)
            return darwin_annotations

        if label_type == "polylines":
            if annotation.closed:
                darwin_annotation["polygon"] = _51_to_v7_polygon(
                    annotation.points, frame_size
                )

            else:
                darwin_annotation["line"] = _51_to_v7_polyline(
                    annotation.points, frame_size
                )
            return [darwin_annotation]

        logger.warn(f"warning, unsupported label type: {label_type}")

    def _upload_annotations(self, label_schema, samples, media_field, dataset,backend):
        """
        Uploads annotations to Darwin
        """
        # Go through each sample and upload annotations
        full_id_maps = {}
        frame_id_map = {}
        files_to_import = []

        with (
            contextlib.nullcontext(tempfile.mkdtemp())
            if _DEBUG
            else tempfile.TemporaryDirectory()) as import_path:
            
            logger.info(f'import_path: {import_path}')
            for label_field, label_info in label_schema.items():
                id_maps = {}
                for sample in samples:
                    
                    logger.info(f'sample: {sample.id}')
                    is_video = sample.media_type == fomm.VIDEO

                    #Checks for videos

                    if sample.metadata is None:
                        if is_video:
                            sample.metadata = fom.VideoMetadata.build_for(
                                sample[media_field]
                            )
                        else:
                            sample.metadata = fom.ImageMetadata.build_for(
                                sample[media_field]
                            )

                    if is_video:
                        frame_size = (
                            sample.metadata.frame_width,
                            sample.metadata.frame_height,
                        )
                    else:
                        frame_size = (sample.metadata.width, sample.metadata.height)

                    file_name = Path(sample[media_field]).name
                    darwin_annotations = []

                    if is_video:
                        frames = {}
                        frame_id_map[sample.id] = {}

                        for frame_number, frame in sample.frames.items():
                            frame_id_map[sample.id][str(frame_number)] = frame.id

                            if frame_number not in frames:
                                frames[frame_number] = []
                            
                            frame_val = frame

                            annotations = self._convert_image_annotations_to_v7(
                                frame, frame_size, label_schema, id_maps, backend, frame_val
                            )
                            for annotation in annotations:
                                ANNOTATION_DATA_KEYS = [
                                    "bounding_box",
                                    "tag",
                                    "polygon",
                                    "keypoint",
                                ]
                                darwin_frame = {
                                    k: annotation[k]
                                    for k in ANNOTATION_DATA_KEYS
                                    if k in annotation
                                }
                                darwin_frame["keyframe"] = True

                                darwin_annotations.append(
                                    {
                                        "frames": {str(frame_number - 1): darwin_frame},
                                        "name": annotation["name"],
                                        "slot_names": annotation["slot_names"],
                                        "ranges": [[frame_number - 1, frame_number]],
                                    }
                                )
                    else:
                        annotations = self._convert_image_annotations_to_v7(
                            sample, frame_size, label_schema, id_maps, backend
                        )
                        darwin_annotations.extend(annotations)

                    temp_file_path = Path(import_path) / Path(f"{uuid.uuid4()}.json")
                    with open(temp_file_path, "w") as temp_file:
                        json.dump(
                            {
                                "version": "2.0",
                                "item": {"name": file_name, "path": ""},
                                "annotations": darwin_annotations,
                            },
                            temp_file,
                            indent=4,
                        )
                    files_to_import.append(temp_file_path)
                parser = get_importer("darwin")
                importer.import_annotations(dataset, parser, files_to_import, append=False, class_prompt=False)
            
            full_id_maps.update({label_field:id_maps})

        return full_id_maps,frame_id_map

    def _create_missing_annotation_classes(self, label_schema, dataset):
        """
        Creates and missing annotation classes in V7 Darwin
        """

        all_classes = dataset.fetch_remote_classes(team_wide=True)
        #lookup_map = {c["name"]: c for c in all_classes}
        classname_anntype_to_class = {}
        for c in all_classes:
            #class_id = c['id']
            class_name = c['name']
            for aty in c['annotation_types']:
                classname_anntype_to_class[(class_name, aty)] = c

        logger.debug(f"_create_missing_annotation_classes all_classes:{all_classes} lookup_map:{classname_anntype_to_class} label_schema:{label_schema}")
        for label_field, label_info in label_schema.items():
            classes = label_info["classes"]
            label_type = label_info["type"]
            annotation_type_translation = self.to_darwin_annotation_type(label_type)
            logger.debug(f"_create_missing_annotation_classes label_type:{label_type} classes:{classes}")
            for cls in classes:
                if (cls, annotation_type_translation) not in classname_anntype_to_class:
                    # create the annotation if it doesn't exist
                    logger.debug(f"_create_missing_annotation_classes creating class cls:{cls} annotation_type_translation:{annotation_type_translation}")
                    dataset.create_annotation_class(
                        cls, annotation_type_translation, ["text"]
                    )
                else:
                    # if it exists but isn't in the dataset, add it
                    matching_class = classname_anntype_to_class[(cls, annotation_type_translation)]
                    logger.debug(f"_create_missing_annotation_classes class exists cls:{cls} in datasets:{matching_class['datasets']}")
                    datasets = [ dataset["id"] for dataset in matching_class["datasets"] ]
                    if dataset.dataset_id not in datasets:
                        logger.debug(f"_create_missing_annotation_classes adding to dataset cls:{cls}")
                        dataset.add_annotation_class(matching_class["id"])

    def to_darwin_annotation_type(self, type):
        if type == "detections":
            return "bounding_box"
        if type == "classification" or type == "classifications":
            return "tag"
        if type == "keypoints":
            return "keypoint"
        if type == "polylines" or type == "polygons":
            return "polygon"
        raise ValueError(f"Unknown type {type}")

    def download_annotations(self, results):
        """
        Downloads annotations from V7 Darwin
        """
        label_schema = results.config.label_schema
        item_sample_map = results.item_sample_map
        frame_id_map = results.frame_id_map
        item_name_annotation = results.config.item_name_annotation

        dataset = self._client.get_remote_dataset(results.config.dataset_slug)
        full_annotations = {}
        with (
            contextlib.nullcontext(tempfile.mkdtemp())
            if _DEBUG
            else tempfile.TemporaryDirectory()) as release_path:
            
            logger.info(f'release_path: {release_path}')

            export_path = self._generate_export(release_path, dataset)
            for label_field, label_info in label_schema.items():

                label_type = label_info["type"]
                label_type = _UNIQUE_TYPE_MAP.get(label_type, label_type)
                sample_annotations = {}

                for annotation_path in export_path.glob("*.json"):
                    data = json.loads(annotation_path.read_text(encoding="UTF-8"))
                    item_id = data["item"]["source_info"]["item_id"]
                    if item_id not in item_sample_map:
                        logger.warn(f"WARNING, {item_id} not in item_sample_map, skipping")
                        continue
                    sample_id = item_sample_map[item_id]["sample_id"]
                    width = data["item"]["slots"][0]["width"]
                    height = data["item"]["slots"][0]["height"]
                    item_name = data["item"]["name"]

                    is_darwin_video = False
                    #Detects if video
                    if data["item"]["slots"][0]["type"] == "video":
                        is_darwin_video = True
                        frame_count = data["item"]["slots"][0]["frame_count"]
                        frame_dict = {}
                        for frame_number in range(1,frame_count+2):
                            frame_dict.update({frame_number: {}})

                    annotations = {}

                    #Video annotations
                    if is_darwin_video:
                        logging.info("Processing video annotations")

                        #Spits merged annotations into per frame annotations
                        video_annotations = self._split_video_annotations(data["annotations"])

                        for annotation in video_annotations:
                            frame_number = list(annotation["frames"].keys())[0]
                            frame_annotation = annotation["frames"][frame_number]
                            confidence = None

                            annot_name = annotation["name"]

                            if item_name_annotation:
                                annot_name = annotation["name"] if annotation["name"] != item_name else "Item"

                            #Checks for unsupported annotation types
                            if "polygon" not in frame_annotation and "bounding_box" not in frame_annotation and "tag" not in frame_annotation and "keypoint" not in frame_annotation:
                                logger.warn("WARNING, unsupported annotation type", annotation)
                                continue

                            darwin_attributes = {}
                            direct_attribute = False
                            if "attributes" in frame_annotation:
                                direct_attribute_dict = {}
                                for attribute in frame_annotation["attributes"]:
                                    # Searching to see if an original attribute or newly added in V7
                                    if "{" in attribute:
                                        direct_attribute = True
                                        attribute = ast.literal_eval(attribute)
                                        direct_attribute_dict.update(attribute)
                                    else:
                                        darwin_attributes[attribute] = True

                            if "properties" in annotation:
                                for prop in annotation["properties"]:
                                    assert prop["name"] != "Text", "Text is a reserved name and cannot be used as a property name"
                                    if prop["name"] in darwin_attributes:
                                        if type(darwin_attributes[prop["name"]]) == list:
                                            darwin_attributes[prop["name"]].append(prop["value"])
                                        else:
                                            tmp_list = [darwin_attributes[prop["name"]], prop["value"]]
                                            darwin_attributes[prop["name"]] = tmp_list
                                    else:
                                        darwin_attributes[prop["name"]] = prop["value"]

                            #Add instance id
                            if "instance_id" in frame_annotation:
                                darwin_attributes["darwin_instance_id"] = frame_annotation["instance_id"]["value"]

                            #Adding text support
                            if "text" in frame_annotation:
                                 darwin_attributes["Text"] = frame_annotation["text"]["text"]

                            if "inference" in frame_annotation:
                                confidence = frame_annotation["inference"]["confidence"] if "confidence" in frame_annotation["inference"] else None

                            voxel_annotation = None
                            if "polygon" in frame_annotation and label_type in ["polygons", "polylines"]:
                                voxel_annotation = _v7_to_51_polygon(
                                    annot_name,
                                    frame_annotation["polygon"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )
                            elif "bounding_box" in frame_annotation and "polygon" not in annotation and label_type in ["detections", "detection"]:
                                voxel_annotation = _v7_to_51_bbox(
                                    annot_name,
                                    frame_annotation["bounding_box"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )
                            elif "tag" in frame_annotation and label_type in ["classifications", "classification"]:
                                voxel_annotation = _v7_to_51_classification(
                                    annot_name,
                                    attributes=darwin_attributes,
                                )
                            elif "keypoint" in frame_annotation and label_type == "keypoints":
                                voxel_annotation = _v7_to_51_keypoint(
                                    annot_name,
                                    frame_annotation["keypoint"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )

                            #Ignores non matching annotation types with label_type 
                            if not voxel_annotation:
                                continue

                            #Adding confidence score
                            if confidence:
                                voxel_annotation.confidence = confidence

                            #Adding direct attributes
                            if direct_attribute:
                                for key,val in direct_attribute_dict.items():
                                    voxel_annotation[key] = val

                            if voxel_annotation.id in annotations:
                                if type(voxel_annotation) == fol.Keypoint:
                                    annotations[voxel_annotation.id].points.extend(
                                        voxel_annotation.points
                                    )
                            else:
                                new_num = str(int(frame_number) + 1)

                                if new_num in frame_id_map[sample_id].keys():
                                   frame_id = frame_id_map[sample_id][new_num]
                                   if frame_id not in annotations.keys():
                                        annotations[frame_id] = {voxel_annotation.id: voxel_annotation}
                                   else:
                                        annotations[frame_id].update({voxel_annotation.id: voxel_annotation})                                       

                                else:
                                    frame_id = None
                                    annotations[frame_id] = {voxel_annotation.id: voxel_annotation}
                                
                        sample_annotations[sample_id] = annotations

                    #Image annotations
                    else:
                        logging.info("Processing image annotations")
                        for annotation in data["annotations"]:
                            confidence = None

                            annot_name = annotation["name"]

                            if item_name_annotation:
                                annot_name = annotation["name"] if annotation["name"] != item_name else "Item"

                            #Checks for unsupported annotation types
                            if "polygon" not in annotation and "bounding_box" not in annotation and "tag" not in annotation and "keypoint" not in annotation:
                                logger.warn("WARNING, unsupported annotation type", annotation)
                                continue

                            direct_attribute = False
                            darwin_attributes = {}
                            if "attributes" in annotation:
                                direct_attribute_dict = {}
                                for attribute in annotation["attributes"]:
                                    # Searching to see if an original attribute or newly added in V7
                                    if "{" in attribute:
                                        direct_attribute = True
                                        attribute = ast.literal_eval(attribute)
                                        direct_attribute_dict.update(attribute)
                                    else:
                                        darwin_attributes[attribute] = True

                            if "properties" in annotation:
                                for prop in annotation["properties"]:
                                    assert prop["name"] != "Text", "Text is a reserved name and cannot be used as a property name"
                                    if prop["name"] in darwin_attributes:
                                        if type(darwin_attributes[prop["name"]]) == list:
                                            darwin_attributes[prop["name"]].append(prop["value"])
                                        else:
                                            tmp_list = [darwin_attributes[prop["name"]], prop["value"]]
                                            darwin_attributes[prop["name"]] = tmp_list
                                    else:
                                        darwin_attributes[prop["name"]] = prop["value"]

                            #Add instance id
                            if "instance_id" in annotation:
                                darwin_attributes["darwin_instance_id"] = annotation["instance_id"]["value"]

                            #Adding text support
                            if "text" in annotation:
                                 darwin_attributes["Text"] = annotation["text"]["text"]

                            if "inference" in annotation:
                                confidence = annotation["inference"]["confidence"] if "confidence" in annotation["inference"] else None

                            voxel_annotation = None
                            if "polygon" in annotation and label_type in ["polygons", "polylines"]:
                                voxel_annotation = _v7_to_51_polygon(
                                    annot_name,
                                    annotation["polygon"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )
                            elif "bounding_box" in annotation and "polygon" not in annotation and label_type in ["detections","detection"]:
                                voxel_annotation = _v7_to_51_bbox(
                                    annot_name,
                                    annotation["bounding_box"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )
                            elif "tag" in annotation and label_type in ["classifications", "classification"]:
                                voxel_annotation = _v7_to_51_classification(
                                    annot_name,
                                    attributes=darwin_attributes,
                                )
                            elif "keypoint" in annotation and label_type == "keypoints":
                                voxel_annotation = _v7_to_51_keypoint(
                                    annot_name,
                                    annotation["keypoint"],
                                    height,
                                    width,
                                    attributes=darwin_attributes,
                                )

                            #Ignores non matching annotation types with label_type
                            if not voxel_annotation:
                                continue

                            #Adding confidence score
                            if confidence:
                                voxel_annotation.confidence = confidence

                            #Adding direct attributes
                            if direct_attribute:
                                for key,val in direct_attribute_dict.items():
                                    voxel_annotation[key] = val

                            if voxel_annotation.id in annotations:
                                if type(voxel_annotation) == fol.Keypoint:
                                    annotations[voxel_annotation.id].points.extend(
                                        voxel_annotation.points
                                    )
                            else:
                                annotations[voxel_annotation.id] = voxel_annotation

                        sample_annotations[sample_id] = annotations

                full_annotations.update({label_field: {label_type: sample_annotations}})

        return full_annotations

    def _generate_export(self, release_path, dataset):
        """
        Generates a V7 export file
        """
        release_name: str = f"voxel51-{uuid.uuid4().hex}"
        self._client.api_v2.export_dataset(
            format="darwin_json_2",
            name=release_name,
            include_authorship=True,
            include_token=False,
            annotation_class_ids=None,
            filters={"not_statuses": ["archived", "error"]},
            dataset_slug=dataset.slug,
            team_slug=dataset.team,
        )

        logger.info("Create export ")
        backoff = 1
        zipfile_path = Path(release_path) / Path(f"{release_name}.zip")
        extracted_path = Path(release_path) / Path(f"{release_name}")
        while True:
            time.sleep(backoff)
            logger.info(".")
            try:
                release = dataset.get_release(release_name)
                release.download_zip(zipfile_path)

                with zipfile.ZipFile(zipfile_path, "r") as zip:
                    zip.extractall(extracted_path)
                return extracted_path

            except darwin.exceptions.NotFound:
                backoff += 1
                continue
        
    def _get_headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"ApiKey {self._api_key}",
        }    

    def _get_workflows_url(self, team_slug):
        return f"https://darwin.v7labs.com/api/v2/teams/{team_slug}/workflows"

    def _get_workflows(self, team_slug):
        url = self._get_workflows_url(team_slug)
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        return response.json()
    
    def _detach_workflow(self, team_slug, workflow):
        url = self._get_workflows_url(team_slug)
        headers = self._get_headers()
        workflow_id = workflow['id']
        url = f'{url}/{workflow_id}/unlink_dataset'

        logger.info('Unlinking workflow {workflow_id}')        
        response = requests.patch(url, headers=headers)

    def _delete_dataset_id(self, dataset_id):
        url = f"https://darwin.v7labs.com/api/datasets/{dataset_id}/archive"
        headers = {
            "accept": "application/json",
            "Authorization": f"ApiKey {self._api_key}"
        }
        response = requests.put(url, headers=headers)

    def _delete_dataset_with_workflow_detach(self, dataset_slug):
        dataset = self._client.get_remote_dataset(dataset_slug)
        dataset_name = dataset.name
        team_slug = dataset.team
        workflows = self._get_workflows(team_slug)
        workflow_dsets = {x['dataset']['name']:x for x in workflows if x['dataset'] is not None}
        if dataset_name in workflow_dsets:
            wflow = workflow_dsets[dataset_name]
            response = self._detach_workflow(team_slug, wflow)
            logger.info(f'Detaching workflow for dataset {dataset_name}')
        else:
            logger.warning(f'Did not find workflow for dataset {dataset_name}')
            response = None

        self._delete_dataset_id(dataset.dataset_id)
        #remove_remote_dataset(dataset_name)
        logger.info(f'Deleting dataset {dataset_name}')


    def _split_video_annotations(self,annotations):
        """
        Splits Darwin JSON video annotations into per frame annotations
        """
        converted_annotations = []

        for annot in annotations:
            frame_dict = annot.pop("frames")
            
            for key in frame_dict.keys():
                new_annot = {}
                new_annot.update(annot)
                new_annot["frames"] = {key: frame_dict[key]}
                new_annot["ranges"] = [[int(key), int(key) + 1]]
                converted_annotations.append(new_annot)

        return converted_annotations

    @property
    def client(self):
        return self._client


class DarwinResults(foua.AnnotationResults):
    def __init__(
        self,
        samples,
        config,
        anno_key,
        id_map,
        item_sample_map=None,
        dataset_slug=None,
        backend=None,
        attributes=None,
        frame_id_map=None,
    ):
        super().__init__(samples, config, anno_key, id_map, backend=backend)
        self.dataset_slug = dataset_slug
        self.item_sample_map = item_sample_map
        self.atts = attributes
        self.frame_id_map = frame_id_map
        self.id_map = id_map
        self.anno_key = anno_key

    def launch_editor(self):
        """
        Launches the V7 Darwin tool
        """
        client = self.connect_to_api().client
        dataset = client.get_remote_dataset(self.backend.config.dataset_slug)
        url = f"{client.base_url}/datasets/{dataset.dataset_id}"
        webbrowser.open(url, new=2)

    def cleanup(self):
        """
        Cleans up annotations in V7 Darwin by deleting annotations and returning items to new status
        """
        api = self.connect_to_api()
        api._delete_dataset_with_workflow_detach(self.dataset_slug)

    
    def check_status(self):
        """
        Checks and prints the status of annotations in V7 Darwin.
        """
        client = self.connect_to_api().client
        dataset = client.get_remote_dataset(self.backend.config.dataset_slug)
        url = f"{client.base_url}/api/v2/teams/{dataset.team}/items/status_counts?dataset_ids[]={dataset.dataset_id}"
        response = requests.get(url, headers=self._get_headers())

        response.raise_for_status()

        annotation_statuses = []
        print(f"Annotation Run Status Counts for {self.anno_key}:")
        for status_obj in json.loads(response.text)["simple_counts"]:
            print(f"{status_obj['status']}: {status_obj['item_count']}")
            annotation_statuses.append(status_obj["status"])
        return annotation_statuses
    

    def _get_headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"ApiKey {self.backend.config.api_key}",
        }  


    @classmethod
    def _from_dict(cls, d, samples, config, anno_key):
        return cls(
            samples,
            config,
            anno_key,
            id_map = d["id_map"],
            item_sample_map = d.get("item_sample_map"),
            dataset_slug = d.get("dataset_slug"),
            frame_id_map = d.get("frame_id_map"),
        )


# Registering External Storage Items
def _register_items(samples, api_key, dataset_slug, team_slug, external_storage, base_url):
    """
    Registers external storage items in Darwin

    Only readwrite currently supported
    """

    logger.info("item registration started")

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"ApiKey {api_key}",
    }

    items = []
    item_list = []

    for sample in samples:
        external_path = sample.filepath
        path_list = external_path.split("/")
        name = path_list[-1]
        item_list.append(name)
        new_path = "/".join(path_list[3:])
        temp_dict = {
            "path": "/",
            "slots": [
                {
                    "as_frames": "false",
                    "slot_name": "0",
                    "storage_key": new_path,
                    "file_name": name,
                }
            ],
            "name": name,
        }
        items.append(temp_dict)

    payload = {
        "items": items,
        "dataset_slug": dataset_slug,
        "storage_slug": external_storage,
    }

    response = requests.post(
        f"{base_url}/{team_slug}/items/register_existing",
        headers=headers,
        json=payload,
    )

    logger.info("Item registration complete")

    return item_list


def _v7_basic_annotation(
    label,
    annotators: list = [],
    reviewers: list = [],
    confidence=None,
    atts: list = [],
    text: str = "",
    instance_id: str = "",
):
    """
    Creates a base V7 annotation
    """
    annot = {}
    # Adding annotators (if exist)
    annot_list = []
    if annotators:
        for annotator in annotators:
            new_annot = {}
            new_annot["email"] = annotator["email"]
            new_annot["full_name"] = annotator["full_name"]
            annot_list.append(new_annot)
    annot["annotators"] = annot_list

    if atts:
        annot["attributes"] = atts

    if confidence:
        model = {"id":str(uuid.uuid4()),"name":"Voxel51","type":"external"}
        annot["inference"] = {"confidence": confidence,"model": model}

    if instance_id:
        annot["instance_id"] = {"value": instance_id}

    annot["name"] = label

    annot["slot_names"] = ["0"]

    # Adding reviewers (if exist)
    reviewer_list = []
    if reviewers:
        for reviewer in reviewers:
            new_rev = {}
            new_rev["email"] = reviewer["email"]
            new_rev["full_name"] = reviewer["full_name"]
            reviewer_list.append(new_rev)
    annot["reviewers"] = reviewer_list

    if text:
        annot["text"] = {"text": text}

    return annot


# List Darwin items in order to obtain item ids for external storage
def _list_items(api_key, dataset_id, team_slug, base_url):
    """
    List items in Darwin dataset
    """
    url = f"{base_url}/{team_slug}/items?dataset_ids={dataset_id}"

    headers = {"accept": "application/json", "Authorization": f"ApiKey {api_key}"}
    response = requests.get(url, headers=headers)
    return json.loads(response.text)["items"]


def _51_to_v7_bbox(bbox_list, frame_size):
    """
    Converts 51 bounding box coordinates to V7 bounding box coordinates
    """
    width, height = frame_size
    new_bbox = {}
    new_bbox["x"] = bbox_list[0] * width
    new_bbox["y"] = bbox_list[1] * height
    new_bbox["w"] = bbox_list[2] * width
    new_bbox["h"] = bbox_list[3] * height

    return new_bbox


def _51_to_v7_keypoint(keypoint, frame_size):
    """
    Converts 51 keypoint coordinates to V7 keypoint coordinates
    """
    width, height = frame_size
    new_key = {}
    new_key["x"] = keypoint[0] * width
    new_key["y"] = keypoint[1] * height
    return new_key


def _v7_to_51_bbox(label, bbox_dict, height, width, attributes=None):
    """
    Converts V7 bounding box coordinates to 51 Detection
    """
    x = bbox_dict["x"] / width
    y = bbox_dict["y"] / height
    w = bbox_dict["w"] / width
    h = bbox_dict["h"] / height
    return fol.Detection(label=label, bounding_box=[x, y, w, h], **attributes)


def _v7_to_51_classification(label, attributes=None):
    """
    Converts a V7 classification to a 51 classification
    """
    return fol.Classification(label=label, **attributes)


def _51_to_v7_polygon(points, frame_size):
    """
    Converts a 51 polygon to a V7 polygon
    """
    width, height = frame_size
    # Need to convert to complex polygon format
    new_list = []
    for point in points[0]:
        new_key = {}
        new_key["x"] = point[0] * width
        new_key["y"] = point[1] * height
        new_list.append(new_key)

    new_poly = {"paths": [new_list]}

    return new_poly


def _51_to_v7_polyline(polyline, frame_size):
    """
    Converts a 51 polygon line to a V7 polygon
    """
    width, height = frame_size
    new_list = []
    for keypoint in polyline:
        new_key = {}
        new_key["x"] = keypoint[0] * width
        new_key["y"] = keypoint[1] * height
        new_list.append(new_key)

    new_poly = {"path": [new_list]}

    return new_poly


def _v7_to_51_polyline(polyline, frame_size):
    """
    Converts a V7 polygon to a 51 polygon

    Note: Open polylines are not currently supported by this integration
    """
    width, height = frame_size
    new_list = []
    for keypoint in polyline["path"]:
        new_keypoint = (keypoint["x"] / width, keypoint["y"] / height)
        new_list.append(new_keypoint)

    return new_list


def _v7_to_51_keypoint(label, keypoint, height, width, attributes=None):
    """
    Converts V7 keypoint coordinates to 51 keypoint coordinates
    """
    new_keypoint = (keypoint["x"] / width, keypoint["y"] / height)
    return fol.Keypoint(label=label, points=[new_keypoint], **attributes)


def _v7_to_51_polygon(label, polygon, height, width, attributes=None):
    """
    Converts a V7 polygon to a 51 polygon
    """
    # Need to add complex polygon support
    assert len(polygon["paths"]) == 1, "Complex polygons currently unsupported"
    new_list = []
    for keypoint in polygon["paths"][0]:
        new_keypoint = (keypoint["x"] / width, keypoint["y"] / height)
        new_list.append(new_keypoint)

    return fol.Polyline(
        label=label,
        points=[new_list],
        closed=True,
        filled=True,
        **attributes,
    )


_UNIQUE_TYPE_MAP = {
    "classification": "classifications",
    "classifications": "classifications",
    "instance": "segmentation",
    "instances": "segmentation",
    "polygons": "polylines",
    "polygon": "polylines",
    "polyline": "polylines",
}