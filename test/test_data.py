"""
    sitreps

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import sitreps_python_api
from sitreps_python_api.model.jira_create import JiraCreate
from sitreps_python_api.model.project_create import ProjectCreate
from sitreps_python_api.model.project_group_create import ProjectGroupCreate
from sitreps_python_api.model.repo_data import RepoData
globals()['JiraCreate'] = JiraCreate
globals()['ProjectCreate'] = ProjectCreate
globals()['ProjectGroupCreate'] = ProjectGroupCreate
globals()['RepoData'] = RepoData
from sitreps_python_api.model.data import Data


class TestData(unittest.TestCase):
    """Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testData(self):
        """Test Data"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Data()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
