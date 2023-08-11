Dataset **LaboroTomato** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/s/J/3x/LbTrXilFgrEAfJ9L6kKtxHQHwnLhDwBNndCLutla9U0BSLkUAKO2Svo56654eNDDkDNky7SWzbZdXDBApDSdhJW6oABp9Jm9cefvNZxxTlB6CKmPx1ayZ47T42zu.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='LaboroTomato', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](http://assets.laboro.ai/laborotomato/laboro_tomato.zip).