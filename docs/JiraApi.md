# sitreps_python_api.JiraApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jira**](JiraApi.md#create_jira) | **POST** /api/v1/jira/ | Create Jira
[**read_jira**](JiraApi.md#read_jira) | **GET** /api/v1/jira/ | Read Jira


# **create_jira**
> bool, date, datetime, dict, float, int, list, str, none_type create_jira(jira_create)

Create Jira

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import jira_api
from sitreps_python_api.model.http_validation_error import HTTPValidationError
from sitreps_python_api.model.jira_create import JiraCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sitreps_python_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sitreps_python_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jira_api.JiraApi(api_client)
    jira_create = JiraCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        project_name="project_name_example",
        todo=1,
        in_progress=1,
        code_review=1,
        blocked=1,
        on_qa=1,
        unresolved=1,
        resolved=1,
        rejected=1,
        created_last_month=1,
        resolved_last_month=1,
        todo_older_than_60d=1,
        project_id=1,
    ) # JiraCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Jira
        api_response = api_instance.create_jira(jira_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling JiraApi->create_jira: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jira_create** | [**JiraCreate**](JiraCreate.md)|  |

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

# **read_jira**
> bool, date, datetime, dict, float, int, list, str, none_type read_jira()

Read Jira

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import jira_api
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
    api_instance = jira_api.JiraApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Jira
        api_response = api_instance.read_jira(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling JiraApi->read_jira: %s\n" % e)
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

