import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from diagrams import Diagram, Cluster
from CustomDiagramIcons.module1 import octopusDeploy_icon
from CustomDiagramIcons.module1 import octopusDeployPipeline_icon
from CustomDiagramIcons.module1 import octopusDeployServerNode_icon
from CustomDiagramIcons.module1 import octopusDeployWorkerNode_icon
from CustomDiagramIcons.module1 import octopusDeployWorkerPool_icon
from CustomDiagramIcons.module1 import octpusDeployRelease_icon
from CustomDiagramIcons.module1 import softwareEngineer_icon
from CustomDiagramIcons.module1 import JIRA_icon
from CustomDiagramIcons.module1 import CRIM_icon
from CustomDiagramIcons.module1 import GitHub_icon
from CustomDiagramIcons.module1 import CRIMTools_icon
from CustomDiagramIcons.module1 import ReportPortal_icon

class TestCase(unittest.TestCase):
    def test_icon_map(self):
        with Diagram("All Icons", show=False):
            with Cluster("onprem"):
                with Cluster("cd"):
                    octopusDeploy_icon("Octopus Deploy")
                    octopusDeployPipeline_icon("Octopus Deploy Pipeline")
                    octopusDeployServerNode_icon("Octopus Deploy Server Node")
                    octopusDeployWorkerNode_icon("Octopus Deploy Worker Node")
                    octopusDeployWorkerPool_icon("Octopus Deploy Worker Pool")
                    octpusDeployRelease_icon("Octopus Deploy Release")
            with Cluster("generic"):
                softwareEngineer_icon("Software Engineer")
                JIRA_icon("JIRA")
                CRIM_icon("CRIM Team")
                GitHub_icon("GitHub")
                CRIMTools_icon("CRIM Tools")
                ReportPortal_icon("Report Portal")

if __name__ == "__main__":
    unittest.main()
    print(Test.assetEqual)