# BioDati COVID-19 Network

This folder contains BioDati's COVID-19 network.

Grab this data in your scripts with:

```python
import pybel
import requests

URL = 'https://github.com/CoronaWhy/bel4corona/raw/master/data/biodati/covid19-biodati-grounded.bel.nodelink.json'
res = requests.get(URL)
res_json = res.json()
graph = pybel.from_nodelink(res_json)
```
