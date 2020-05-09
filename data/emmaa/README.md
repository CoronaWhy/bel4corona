# EMMMA Covid-19

This folder contains the EMMAA Covid-19 graph, which is generated
from the INDRA database on a (weekly?) basis. It's downloaded
using the PyBEL `pybel.from_emmaa()` function and output for direct use.
This graph is created from text mining and some addition of PPIs from
structured databases.

Graph this data in your scripts with:

```python
import pybel
import requests

URL = 'https://github.com/CoronaWhy/bel4corona/raw/master/data/emmaa/covid19-indra-grounded.bel.nodelink.json'
res = requests.get(URL)
res_json = res.json()
graph = pybel.from_nodelink(res_json)
```
