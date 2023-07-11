Dataset **LaboroTomato** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/n/o/Rw/Wn57MXlzzOJym2ZzDeE4Riu3wAdvUFkTWGNqJ9oPkfo2fZYS7dLLVQ8MRevzcC2J9lQSFAjamMEpTbpQXZpk03ieygOEK7092CMFTMYKs0ElxWJ0OJJtfKhH3Om9.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='LaboroTomato', dst_path='~/dtools/datasets/LaboroTomato.tar')
```
The data in original format can be 🔗[downloaded here](http://assets.laboro.ai/laborotomato/laboro_tomato.zip)