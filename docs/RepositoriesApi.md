# sitreps_python_api.RepositoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoriesApi.md#create_repository) | **POST** /api/v1/repositories/ | Create Repository
[**delete_repository**](RepositoriesApi.md#delete_repository) | **DELETE** /api/v1/repositories/{id} | Delete Repository
[**read_repository**](RepositoriesApi.md#read_repository) | **GET** /api/v1/repositories/ | Read Repository
[**read_repository_id**](RepositoriesApi.md#read_repository_id) | **GET** /api/v1/repositories/{id} | Read Repository Id
[**update_repository**](RepositoriesApi.md#update_repository) | **PUT** /api/v1/repositories/{id} | Update Repository


# **create_repository**
> bool, date, datetime, dict, float, int, list, str, none_type create_repository(repository_create)

Create Repository

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import repositories_api
from sitreps_python_api.model.repository_create import RepositoryCreate
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
    api_instance = repositories_api.RepositoriesApi(api_client)
    repository_create = RepositoryCreate(
        name="name_example",
        title="title_example",
        type="type_example",
        url="url_example",
        project_id=1,
    ) # RepositoryCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Repository
        api_response = api_instance.create_repository(repository_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling RepositoriesApi->create_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_create** | [**RepositoryCreate**](RepositoryCreate.md)|  |

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

# **delete_repository**
> bool, date, datetime, dict, float, int, list, str, none_type delete_repository(id)

Delete Repository

Delete an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import repositories_api
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
    api_instance = repositories_api.RepositoriesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Repository
        api_response = api_instance.delete_repository(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling RepositoriesApi->delete_repository: %s\n" % e)
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

# **read_repository**
> bool, date, datetime, dict, float, int, list, str, none_type read_repository()

Read Repository

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import repositories_api
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
    api_instance = repositories_api.RepositoriesApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Repository
        api_response = api_instance.read_repository(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling RepositoriesApi->read_repository: %s\n" % e)
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

# **read_repository_id**
> bool, date, datetime, dict, float, int, list, str, none_type read_repository_id(id)

Read Repository Id

Get item by ID.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import repositories_api
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
    api_instance = repositories_api.RepositoriesApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Read Repository Id
        api_response = api_instance.read_repository_id(id)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling RepositoriesApi->read_repository_id: %s\n" % e)
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

# **update_repository**
> bool, date, datetime, dict, float, int, list, str, none_type update_repository(id, repository_update)

Update Repository

Update an item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import repositories_api
from sitreps_python_api.model.repository_update import RepositoryUpdate
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
    api_instance = repositories_api.RepositoriesApi(api_client)
    id = 1 # int | 
    repository_update = RepositoryUpdate(
        name="name_example",
        title="title_example",
        type="type_example",
        url="url_example",
        project_id=1,
    ) # RepositoryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update Repository
        api_response = api_instance.update_repository(id, repository_update)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling RepositoriesApi->update_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **repository_update** | [**RepositoryUpdate**](RepositoryUpdate.md)|  |

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

