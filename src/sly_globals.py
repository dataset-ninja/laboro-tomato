import os
import sys
from collections import defaultdict
from pathlib import Path

import supervisely as sly

# my_app = sly.AppService()
# api: sly.Api = my_app.public_api

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

# TASK_ID = int(os.environ["TASK_ID"])
# TEAM_ID = sly.env.team_id()
# WORKSPACE_ID = sly.env.workspace_id()

logger = sly.logger

# train_ds = os.environ["modal.state.train"]
# test_ds = os.environ["modal.state.test"]

datasets = ["Train", "Test"]

# for ds in [train_ds, test_ds]:
#     if len(ds) != 2:
#         datasets.append(ds[1:-1].replace('\'', ''))

# if len(datasets) == 0:
#     logger.warn('You have not selected a dataset to import')
#     my_app.stop()

train_percent = 100
test_percent = 100

sample_img_count = {"Train": round(6.43 * train_percent), "Test": round(1.61 * test_percent)}

# project_name = "LaboroTomato"
work_dir = "tomato_data"
apple_url = "http://assets.laboro.ai/laborotomato/laboro_tomato.zip"

arch_name = "laboro_tomato.zip"

folder_name = "laboro_tomato"
anns_folder = "annotations"
batch_size = 30
class_name = "tomato"

class_names = [
    "b_fully_ripened",
    "b_half_ripened",
    "b_green",
    "l_fully_ripened",
    "l_half_ripened",
    "l_green",
]

obj_classes = [sly.ObjClass(class_name, sly.Polygon) for class_name in class_names]

cls_to_obj_classes = {cls_name: obj_class for cls_name, obj_class in zip(class_names, obj_classes)}


# tag_meta_collection = sly.TagMetaCollection(tag_metas)
meta = sly.ProjectMeta(obj_classes=obj_classes)

# storage_dir = sly.app.get_data_dir()
storage_dir = "./APP_DATA"
work_dir_path = os.path.join(storage_dir, work_dir)
sly.io.fs.mkdir(work_dir_path)
archive_path = os.path.join(work_dir_path, arch_name)

image_name_to_id = {}
id_to_segm_anns = defaultdict(list)
id_to_tag = defaultdict(list)
name_to_size = {}
category_id_to_name = {}
