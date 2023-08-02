from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

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
APPLICATIONS: List[Industry] = [Industry.Agricultural()]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.ObjectDetection(),
    CVTask.SemanticSegmentation(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2020-07-14"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

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
    "b_fully_ripened": [255, 0, 255],
    "b_half_ripened": [0, 0, 255],
    "b_green": [0, 255, 255],
    "l_fully_ripened": [255, 20, 147],
    "l_half_ripened": [30, 144, 255],
    "l_green": [127, 255, 212],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Roman Trigubenko", "hfujihara"]


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Laboro.AI Inc, Japan"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://laboro.ai/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
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
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
