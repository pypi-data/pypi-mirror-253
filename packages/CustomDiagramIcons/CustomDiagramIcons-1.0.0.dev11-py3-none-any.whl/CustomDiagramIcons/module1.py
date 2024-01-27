from diagrams import Diagram
from CustomDiagramIcons.onprem.cd.octopusDeploy import octopusDeployProgram
from CustomDiagramIcons.onprem.cd.octopusDeploy import octopusDeployPipeline
from CustomDiagramIcons.onprem.cd.octopusDeploy import octopusDeployServerNode
from CustomDiagramIcons.onprem.cd.octopusDeploy import octopusDeployWorkerNode
from CustomDiagramIcons.onprem.cd.octopusDeploy import octopusDeployWorkerPool
from CustomDiagramIcons.onprem.cd.octopusDeploy import octpusDeployRelease
from CustomDiagramIcons.generic import softwareEngineer
from CustomDiagramIcons.generic import JIRA
from CustomDiagramIcons.generic import GitHub
from CustomDiagramIcons.generic import DealerTrackCanada
from CustomDiagramIcons.generic import ReportPortal

def octopusDeploy_icon(val):
    return octopusDeployProgram(val)

def octopusDeployPipeline_icon(val):
    return octopusDeployPipeline(val)

def octopusDeployServerNode_icon(val):
    return octopusDeployServerNode(val)

def octopusDeployWorkerNode_icon(val):
    return octopusDeployServerNode(val)

def octopusDeployWorkerPool_icon(val):
    return octopusDeployServerNode(val)

def octpusDeployRelease_icon(val):
    return octpusDeployRelease(val)

def softwareEngineer_icon(val):
    return softwareEngineer(val)

def JIRA_icon(val):
    return JIRA(val)

def DealerTrackCanada_icon(val):
    return DealerTrackCanada(val)

def GitHub_icon(val):
    return GitHub(val)

def ReportPortal_icon(val):
    return ReportPortal(val)