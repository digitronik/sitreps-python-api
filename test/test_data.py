"""
    sitreps

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import sitreps_python_api
from sitreps_python_api.model.cloc_create import CLOCCreate
from sitreps_python_api.model.code_coverage_create import CodeCoverageCreate
from sitreps_python_api.model.integration_test_create import IntegrationTestCreate
from sitreps_python_api.model.jira_create import JiraCreate
from sitreps_python_api.model.project_create import ProjectCreate
from sitreps_python_api.model.project_group_create import ProjectGroupCreate
from sitreps_python_api.model.sonar_qube_create import SonarQubeCreate
from sitreps_python_api.model.unit_test_create import UnitTestCreate
globals()['CLOCCreate'] = CLOCCreate
globals()['CodeCoverageCreate'] = CodeCoverageCreate
globals()['IntegrationTestCreate'] = IntegrationTestCreate
globals()['JiraCreate'] = JiraCreate
globals()['ProjectCreate'] = ProjectCreate
globals()['ProjectGroupCreate'] = ProjectGroupCreate
globals()['SonarQubeCreate'] = SonarQubeCreate
globals()['UnitTestCreate'] = UnitTestCreate
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