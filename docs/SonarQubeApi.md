# sitreps_python_api.SonarQubeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sonarqube**](SonarQubeApi.md#create_sonarqube) | **POST** /api/v1/sonarqube/ | Create Sonarqube
[**read_sonarqube**](SonarQubeApi.md#read_sonarqube) | **GET** /api/v1/sonarqube/ | Read Sonarqube


# **create_sonarqube**
> bool, date, datetime, dict, float, int, list, str, none_type create_sonarqube(sonar_qube_create)

Create Sonarqube

Create new item.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import sonar_qube_api
from sitreps_python_api.model.sonar_qube_create import SonarQubeCreate
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
    api_instance = sonar_qube_api.SonarQubeApi(api_client)
    sonar_qube_create = SonarQubeCreate(
        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        vulnerabilities=1,
        code_smells=1,
        security_hotspots=1,
        bugs=1,
        repository_id=1,
    ) # SonarQubeCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Sonarqube
        api_response = api_instance.create_sonarqube(sonar_qube_create)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling SonarQubeApi->create_sonarqube: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonar_qube_create** | [**SonarQubeCreate**](SonarQubeCreate.md)|  |

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

# **read_sonarqube**
> bool, date, datetime, dict, float, int, list, str, none_type read_sonarqube()

Read Sonarqube

Retrieve items.

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import sonar_qube_api
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
    api_instance = sonar_qube_api.SonarQubeApi(api_client)
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Sonarqube
        api_response = api_instance.read_sonarqube(skip=skip, limit=limit)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling SonarQubeApi->read_sonarqube: %s\n" % e)
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

