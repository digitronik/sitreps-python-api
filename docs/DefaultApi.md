# sitreps_python_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dump_data**](DefaultApi.md#dump_data) | **POST** /api/v1/ | Dump Data


# **dump_data**
> bool, date, datetime, dict, float, int, list, str, none_type dump_data(data)

Dump Data

### Example


```python
import time
import sitreps_python_api
from sitreps_python_api.api import default_api
from sitreps_python_api.model.data import Data
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
    api_instance = default_api.DefaultApi(api_client)
    data = Data(
        project_group=ProjectGroupCreate(
            name="name_example",
            title="title_example",
        ),
        project=ProjectCreate(
            name="name_example",
            title="title_example",
            group_id=1,
        ),
        repos=[
            RepoData(
                repository=RepositoryCreate(
                    name="name_example",
                    title="title_example",
                    type="type_example",
                    url="url_example",
                    project_id=1,
                ),
                integrationtests=IntegrationTestCreate(
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
                ),
                metadata=MetadataCreate(
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    repository_id=1,
                    meta=[
                        None,
                    ],
                ),
                sonarqube=SonarQubeCreate(
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    vulnerabilities=1,
                    code_smells=1,
                    security_hotspots=1,
                    bugs=1,
                    repository_id=1,
                ),
                cloc=CLOCCreate(
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    cloc=1,
                    repository_id=1,
                ),
                codecoverage=CodeCoverageCreate(
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    coverage=3.14,
                    repository_id=1,
                ),
                unittests=UnitTestCreate(
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    gh_action=1,
                    jenkins=1,
                    travis=1,
                    repository_id=1,
                ),
            ),
        ],
        jira=JiraCreate(
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
        ),
    ) # Data | 

    # example passing only required values which don't have defaults set
    try:
        # Dump Data
        api_response = api_instance.dump_data(data)
        pprint(api_response)
    except sitreps_python_api.ApiException as e:
        print("Exception when calling DefaultApi->dump_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  |

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

