**LaboroTomato** (LaboroTomato: instance segmentation dataset) is a dataset for instance segmentation, object detection, and semantic segmentation tasks. It is used in the agriculture industry.

The dataset consists of 804 images with 10610 labeled objects belonging to 1 single class (*tomato*).

Each image in the LaboroTomato dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 2 splits in the dataset: *Test* (161 images) and *Train* (643 images). The dataset was released in 2020 by the [Laboro.AI Inc](https://laboro.ai/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/laboro-tomato/raw/main/visualizations/side_annotations_grid.png">
