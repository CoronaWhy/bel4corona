# covid19kg

This folder contains Fraunhofer's COVID-19 knowledge graph as well as
the script that downloads/pre-processes it. This graph was manually curated,
with some additional content added from Pathway Commons.

Graph this data in your scripts with:

```python
import pybel
import requests

URL = 'https://github.com/CoronaWhy/bel4corona/raw/master/data/covid19kg/covid19kg-grounded.bel.nodelink.json'
res = requests.get(URL)
res_json = res.json()
graph = pybel.from_nodelink(res_json)
```
