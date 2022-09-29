# sitreps_python_api.IntegrationTestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_test**](IntegrationTestsApi.md#create_integration_test) | **POST** /api/v1/integrationtest/ | Create Integration Test
[**read_integration_test**](IntegrationTestsApi.md#read_integration_test) | **GET** /api/v1/integrationtest/ | Read Integration Test


# **create_integration_test**
> bool, date, datetime, dict, float, int, list, str, none_type create_integration_test(integration_test_create)

Create Integration Test

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import integration_tests_api
from sitreps_python_api.model.integration_test_create import IntegrationTestCreate
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
    api_instance = integration_tests_api.IntegrationTestsApi(api_client)
    integration_test_create = IntegrationTestCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        repository_id=1,
        total_tests=1,
        customer_scenario=1,
        component="component_example",
        automated=1,
        not_automated=1,
        manual_only=1,
        critical=1,
        high=1,
        medium=1,
        low=1,
        ui=1,
        non_ui=1,
        negative=1,
        functional=1,
        non_functional=1,
        missing_assignee=1,
        missing_automation_status=1,
        missing_component=1,
        missing_importance=1,
        missing_interface_type=1,
        missing_requirements=1,
        missing_type=1,
        assignees={},
        requirements={},
    ) # IntegrationTestCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Integration Test
        api_response = api_instance.create_integration_test(integration_test_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling IntegrationTestsApi->create_integration_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_test_create** | [**IntegrationTestCreate**](IntegrationTestCreate.md)|  |

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

# **read_integration_test**
> bool, date, datetime, dict, float, int, list, str, none_type read_integration_test()

Read Integration Test

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import integration_tests_api
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
    api_instance = integration_tests_api.IntegrationTestsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Integration Test
        api_response = api_instance.read_integration_test(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling IntegrationTestsApi->read_integration_test: %s\n" % e)
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

