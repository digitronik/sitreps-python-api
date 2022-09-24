# sitreps_python_api.CodeCoverageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code_coverage**](CodeCoverageApi.md#create_code_coverage) | **POST** /api/v1/coverage/ | Create Code Coverage
[**read_code_coverage**](CodeCoverageApi.md#read_code_coverage) | **GET** /api/v1/coverage/ | Read Code Coverage


# **create_code_coverage**
> bool, date, datetime, dict, float, int, list, str, none_type create_code_coverage(code_coverage_create)

Create Code Coverage

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import code_coverage_api
from sitreps_python_api.model.code_coverage_create import CodeCoverageCreate
from sitreps_python_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sitreps_python_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sitreps_python_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = code_coverage_api.CodeCoverageApi(api_client)
    code_coverage_create = CodeCoverageCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        coverage=3.14,
        repository_id=1,
    ) # CodeCoverageCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Code Coverage
        api_response = api_instance.create_code_coverage(code_coverage_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling CodeCoverageApi->create_code_coverage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_coverage_create** | [**CodeCoverageCreate**](CodeCoverageCreate.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_code_coverage**
> bool, date, datetime, dict, float, int, list, str, none_type read_code_coverage()

Read Code Coverage

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import code_coverage_api
from sitreps_python_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sitreps_python_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sitreps_python_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = code_coverage_api.CodeCoverageApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Code Coverage
        api_response = api_instance.read_code_coverage(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling CodeCoverageApi->read_code_coverage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

