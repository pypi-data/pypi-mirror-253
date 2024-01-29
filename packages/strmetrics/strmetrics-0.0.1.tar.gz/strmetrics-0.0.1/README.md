# string-metrics
A Python package offering a suite of string distance metrics, including normalized Levenshtein distance and more, for efficient text comparison and analysis.



### Install from pypi
```sh
pip install -U strmetrics
```


### Levenshtein
```py
from strmetrics.levenshtein import Levenshtein

levenshtein = Levenshtein()
print(levenshtein.distance('Hi', 'Hello'))
```