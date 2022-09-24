# sitreps_python_api.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/projects/ | Create Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v1/projects/{id} | Delete Project
[**read_project**](ProjectsApi.md#read_project) | **GET** /api/v1/projects/ | Read Project
[**read_project_id**](ProjectsApi.md#read_project_id) | **GET** /api/v1/projects/{id} | Read Project Id
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v1/projects/{id} | Update Project


# **create_project**
> bool, date, datetime, dict, float, int, list, str, none_type create_project(project_create)

Create Project

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import projects_api
from sitreps_python_api.model.project_create import ProjectCreate
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_create = ProjectCreate(
        name="name_example",
        title="title_example",
        group_id=1,
    ) # ProjectCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_project(project_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  |

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

# **delete_project**
> bool, date, datetime, dict, float, int, list, str, none_type delete_project(id)

Delete Project

Delete an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Project
        api_response = api_instance.delete_project(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
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

# **read_project**
> bool, date, datetime, dict, float, int, list, str, none_type read_project()

Read Project

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Project
        api_response = api_instance.read_project(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectsApi->read_project: %s\n" % e)
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

# **read_project_id**
> bool, date, datetime, dict, float, int, list, str, none_type read_project_id(id)

Read Project Id

Get item by ID.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Read Project Id
        api_response = api_instance.read_project_id(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectsApi->read_project_id: %s\n" % e)
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

# **update_project**
> bool, date, datetime, dict, float, int, list, str, none_type update_project(id, project_group_update)

Update Project

Update an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = 1 # int | 
    project_group_update = ProjectGroupUpdate(
        name="name_example",
        title="title_example",
    ) # ProjectGroupUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update Project
        api_response = api_instance.update_project(id, project_group_update)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
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

