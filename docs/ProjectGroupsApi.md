# sitreps_python_api.ProjectGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_group**](ProjectGroupsApi.md#create_project_group) | **POST** /api/v1/projectgroups/ | Create Project Group
[**delete_project_group**](ProjectGroupsApi.md#delete_project_group) | **DELETE** /api/v1/projectgroups/{id} | Delete Project Group
[**read_project_group**](ProjectGroupsApi.md#read_project_group) | **GET** /api/v1/projectgroups/{id} | Read Project Group
[**read_project_groups**](ProjectGroupsApi.md#read_project_groups) | **GET** /api/v1/projectgroups/ | Read Project Groups
[**update_project_group**](ProjectGroupsApi.md#update_project_group) | **PUT** /api/v1/projectgroups/{id} | Update Project Group


# **create_project_group**
> bool, date, datetime, dict, float, int, list, str, none_type create_project_group(project_group_create)

Create Project Group

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import project_groups_api
from sitreps_python_api.model.project_group_create import ProjectGroupCreate
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
    api_instance = project_groups_api.ProjectGroupsApi(api_client)
    project_group_create = ProjectGroupCreate(
        name="name_example",
        title="title_example",
    ) # ProjectGroupCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Project Group
        api_response = api_instance.create_project_group(project_group_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectGroupsApi->create_project_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_group_create** | [**ProjectGroupCreate**](ProjectGroupCreate.md)|  |

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

# **delete_project_group**
> bool, date, datetime, dict, float, int, list, str, none_type delete_project_group(id)

Delete Project Group

Delete an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import project_groups_api
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
    api_instance = project_groups_api.ProjectGroupsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Project Group
        api_response = api_instance.delete_project_group(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectGroupsApi->delete_project_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **read_project_group**
> bool, date, datetime, dict, float, int, list, str, none_type read_project_group(id)

Read Project Group

Get item by ID.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import project_groups_api
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
    api_instance = project_groups_api.ProjectGroupsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Read Project Group
        api_response = api_instance.read_project_group(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectGroupsApi->read_project_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **read_project_groups**
> bool, date, datetime, dict, float, int, list, str, none_type read_project_groups()

Read Project Groups

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import project_groups_api
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
    api_instance = project_groups_api.ProjectGroupsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Project Groups
        api_response = api_instance.read_project_groups(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectGroupsApi->read_project_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 10

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

# **update_project_group**
> bool, date, datetime, dict, float, int, list, str, none_type update_project_group(id, project_group_update)

Update Project Group

Update an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import project_groups_api
from sitreps_python_api.model.project_group_update import ProjectGroupUpdate
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
    api_instance = project_groups_api.ProjectGroupsApi(api_client)
    id = 1 # int | 
    project_group_update = ProjectGroupUpdate(
        name="name_example",
        title="title_example",
    ) # ProjectGroupUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update Project Group
        api_response = api_instance.update_project_group(id, project_group_update)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectGroupsApi->update_project_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **project_group_update** | [**ProjectGroupUpdate**](ProjectGroupUpdate.md)|  |

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

