Dataset **LaboroTomato** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEzNTFfTGFib3JvVG9tYXRvL2xhYm9yb3RvbWF0by1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJFYzN6TGZjdFhySG9JTVpyU3ZjOG5NZ0pCV3JoMVBuaE5xT0dxYy92MU5nPSJ9)

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