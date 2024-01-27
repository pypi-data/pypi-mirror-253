## vihub-python

### install

```sh
pip install vihub
```

### usage

```python
import os

os.environ["API_KEY"] = "<YOUR_API_KEY>"

import vihub

monitoringId = "<YOUR_MONITORING_ID>"
imageBytes = open("/Users/rikimac22/Desktop/cancun.jpeg", "rb")
imageTitle = "cancun.jpeg"
imageType = "image/jpeg"

vihub.addImage(
    monitoringId,
    imageBytes,
    imageTitle,
    imageType,
)
```

### for developers

install local package

```sh
pip install wheel
pip uninstall vihub
rm -rf dist/*
python setup.py sdist bdist_wheel
pip install dist/*.whl
```
