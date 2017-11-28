# zerobounce-python-api

[ZeroBounce](https://zerobounce.net "Zerobounce Homepage") Python API


```python
from zerobounce import ZeroBounceAPI

zba = ZeroBounceAPI('yourapikey____________')
print zba.get_credits()
print zba.validate('username@example.com')
print zba.validatewithip('username@example.com')
```
