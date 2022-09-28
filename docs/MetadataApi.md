# sitreps_python_api.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata**](MetadataApi.md#create_metadata) | **POST** /api/v1/metadata/ | Create Metadata
[**read_metadata**](MetadataApi.md#read_metadata) | **GET** /api/v1/metadata/ | Read Metadata


# **create_metadata**
> bool, date, datetime, dict, float, int, list, str, none_type create_metadata(metadata_create)

Create Metadata

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import metadata_api
from sitreps_python_api.model.metadata_create import MetadataCreate
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
    api_instance = metadata_api.MetadataApi(api_client)
    metadata_create = MetadataCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        repository_id=1,
        metadata=[
            None,
        ],
    ) # MetadataCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Metadata
        api_response = api_instance.create_metadata(metadata_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling MetadataApi->create_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_create** | [**MetadataCreate**](MetadataCreate.md)|  |

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

# **read_metadata**
> bool, date, datetime, dict, float, int, list, str, none_type read_metadata()

Read Metadata

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import metadata_api
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
    api_instance = metadata_api.MetadataApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Metadata
        api_response = api_instance.read_metadata(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling MetadataApi->read_metadata: %s\n" % e)
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

