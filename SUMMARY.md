**LaboroTomato: Instance Segmentation Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agricultural industry. 

The dataset consists of 804 images with 10610 labeled objects belonging to 6 different classes including *b_green*, *l_green*, *l_fully_ripened*, and other: *b_half_ripened*, *l_half_ripened*, and *b_fully_ripened*.

Images in the LaboroTomato dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 2 splits in the dataset: *Test* (161 images) and *Train* (643 images). The dataset was released in 2020 by the Laboro.AI Inc, Japan.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/laboro-tomato/raw/main/visualizations/horizontal_grid.png">
