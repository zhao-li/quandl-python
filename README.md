# Daas Python Client

This is the official documentation for Daas's Python Package. The package can be used to interact with the latest version of the Daas API. This package is a fork of [Quandl's Python Client](https://github.com/quandl/quandl-python). The API of this package will adhere closely to the [Quandl's Python Client](https://github.com/quandl/quandl-python). Please refer to the the [Quandl's Python Client](https://github.com/quandl/quandl-python) documentation for advance usage or contact the maintainer of this package.

Installation
------------
Add to your project's `requirements.txt`:
```
-e git://github.com/zhao-li/quandl-python.git#egg=quandl 
```

Usage
-----
```python
import quandl as daas
daas.ApiConfig.api_key = 'tEsTkEy123456789'
daas.ApiConfig.api_version = '0.0.1'
daas.ApiConfig.api_base = 'http://localhost/'
data = daas.get('vendor/dataset')
```

Test
----
To test custom code using Python:
```shell
python -m unittest discover /usr/src/quandl-python/test/test_operations/
```
To test custom code using Django:
```shell
./manage.py test /usr/src/quandl-python/test/test_operations/
```

Notes
-----
For development, add to `requirements.txt`:
```
-e file:///usr/src/quandl-python#egg=quandl  
```
Ensure the library source code is located in the correct directory (e.g. /usr/src/quandl-python)

