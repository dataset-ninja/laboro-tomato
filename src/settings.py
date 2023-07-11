from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "LaboroTomato"
PROJECT_NAME_FULL: str = "LaboroTomato: Instance Segmentation Dataset"

PROJECT_NAME_FULL = PROJECT_NAME if PROJECT_NAME_FULL is None else PROJECT_NAME_FULL
##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0()
APPLICATIONS: List[Industry] = [Industry.Agriculture()]
CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.ObjectDetection(),
    CVTask.SemanticSegmentation(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_YEAR: int = 2020
HOMEPAGE_URL: str = "https://github.com/laboroai/LaboroTomato#readme"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1636071
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/laboro-tomato"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "http://assets.laboro.ai/laborotomato/laboro_tomato.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "b_fully_ripened": [208, 2, 27],
    "b_half_ripened": [248, 231, 28],
    "b_green": [126, 211, 33],
    "l_fully_ripened": [250, 190, 212],
    "l_half_ripened": [255, 250, 200],
    "l_green": [170, 255, 195],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = None
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Laboro.AI Inc, Japan"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://laboro.ai/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL

    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


settings_assertions = {
    "project_name": str,
    "license": License,
    "industries": List[Industry],
    "cv_tasks": List[CVTask],
    "annotation_types": List[AnnotationType],
    "release_year": int,
    "homepage_url": str,
    "preview_image_id": int,
    "github_url": str,
    "project_name_full": Optional[str],
    "download_original_url": Optional[Union[str, dict]],
    "class2color": Optional[Dict[str, List[int]]],
    "paper": Optional[str],
    "citation_url": Optional[str],
    "organization_name": Optional[Union[str, List[str]]],
    "organization_url": Optional[Union[str, List[str]]],
    "tags": Optional[List[str]],
}


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    # for key, value in settings.items():
    #     expected_type = settings_assertions.get(key)
    #     assert isinstance(value, expected_type), f"Assertion failed for key: {key}"

    return settings
