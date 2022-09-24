# sitreps_python_api.UnitTestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unittests**](UnitTestsApi.md#create_unittests) | **POST** /api/v1/unittests/ | Create Unittests
[**read_unittests**](UnitTestsApi.md#read_unittests) | **GET** /api/v1/unittests/ | Read Unittests


# **create_unittests**
> bool, date, datetime, dict, float, int, list, str, none_type create_unittests(unit_test_create)

Create Unittests

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import unit_tests_api
from sitreps_python_api.model.unit_test_create import UnitTestCreate
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
    api_instance = unit_tests_api.UnitTestsApi(api_client)
    unit_test_create = UnitTestCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        gh_action=1,
        jenkins=1,
        travis=1,
        repository_id=1,
    ) # UnitTestCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Unittests
        api_response = api_instance.create_unittests(unit_test_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling UnitTestsApi->create_unittests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_test_create** | [**UnitTestCreate**](UnitTestCreate.md)|  |

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

# **read_unittests**
> bool, date, datetime, dict, float, int, list, str, none_type read_unittests()

Read Unittests

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import unit_tests_api
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
    api_instance = unit_tests_api.UnitTestsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Unittests
        api_response = api_instance.read_unittests(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling UnitTestsApi->read_unittests: %s\n" % e)
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

