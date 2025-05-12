# doge

# api docs

- https://www.ecfr.gov/reader-aids/ecfr-developer-resources/rest-api-interactive-documentation

# api endpoints

- https://www.ecfr.gov/developers/documentation/api/v1

# install

```shell
/bin/bash install-requirements.sh
```

# run

```shell
python run_me.py
```

# test

```shell
pytest -s api/tests/test_get_agencies.py
```

Example:

```shell
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.13.0, pytest-8.3.5, pluggy-1.5.0
plugins: anyio-4.9.0, ddtrace-3.7.0, cov-6.1.1
collected 1 item                                                                                                                                                                                                                       

api/tests/test_get_agencies.py 
EcfrClient :: get_agencies :: 153 agencies
EcfrClient :: get_versioner_full :: title=1 :: versioner_full["size_megabytes"]=0.45 MB
EcfrClient :: get_versioner_full :: title=2 :: versioner_full["size_megabytes"]=2.65 MB
EcfrClient :: get_versioner_full :: title=3 :: versioner_full["size_megabytes"]=0.03 MB
EcfrClient :: get_versioner_full :: title=4 :: versioner_full["size_megabytes"]=0.39 MB
EcfrClient :: get_versioner_full :: title=5 :: versioner_full["size_megabytes"]=11.8 MB
.

========================================================================================================== 1 passed in 35.90s ==========================================================================================================
```