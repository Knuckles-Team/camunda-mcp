"""Operaton / Camunda 7 engine REST client, one module per REST area.

Each public method is one engine REST operation (named from its operation id)
and so one ``camunda7_<operation>`` MCP tool.
"""

from camunda_mcp.api.camunda7.authorization import Camunda7Authorization
from camunda_mcp.api.camunda7.batch import Camunda7Batch
from camunda_mcp.api.camunda7.condition import Camunda7Condition
from camunda_mcp.api.camunda7.decision_definition import Camunda7DecisionDefinition
from camunda_mcp.api.camunda7.decision_requirements_definition import (
    Camunda7DecisionRequirementsDefinition,
)
from camunda_mcp.api.camunda7.deployment import Camunda7Deployment
from camunda_mcp.api.camunda7.engine import Camunda7Engine
from camunda_mcp.api.camunda7.event_subscription import Camunda7EventSubscription
from camunda_mcp.api.camunda7.execution import Camunda7Execution
from camunda_mcp.api.camunda7.external_task import Camunda7ExternalTask
from camunda_mcp.api.camunda7.filter import Camunda7Filter
from camunda_mcp.api.camunda7.group import Camunda7Group
from camunda_mcp.api.camunda7.historic_activity_instance import (
    Camunda7HistoricActivityInstance,
)
from camunda_mcp.api.camunda7.historic_batch import Camunda7HistoricBatch
from camunda_mcp.api.camunda7.historic_decision_definition import (
    Camunda7HistoricDecisionDefinition,
)
from camunda_mcp.api.camunda7.historic_decision_instance import (
    Camunda7HistoricDecisionInstance,
)
from camunda_mcp.api.camunda7.historic_decision_requirements_definition import (
    Camunda7HistoricDecisionRequirementsDefinition,
)
from camunda_mcp.api.camunda7.historic_detail import Camunda7HistoricDetail
from camunda_mcp.api.camunda7.historic_external_task_log import (
    Camunda7HistoricExternalTaskLog,
)
from camunda_mcp.api.camunda7.historic_identity_link_log import (
    Camunda7HistoricIdentityLinkLog,
)
from camunda_mcp.api.camunda7.historic_incident import Camunda7HistoricIncident
from camunda_mcp.api.camunda7.historic_job_log import Camunda7HistoricJobLog
from camunda_mcp.api.camunda7.historic_process_definition import (
    Camunda7HistoricProcessDefinition,
)
from camunda_mcp.api.camunda7.historic_process_instance import (
    Camunda7HistoricProcessInstance,
)
from camunda_mcp.api.camunda7.historic_task_instance import Camunda7HistoricTaskInstance
from camunda_mcp.api.camunda7.historic_user_operation_log import (
    Camunda7HistoricUserOperationLog,
)
from camunda_mcp.api.camunda7.historic_variable_instance import (
    Camunda7HistoricVariableInstance,
)
from camunda_mcp.api.camunda7.history_cleanup import Camunda7HistoryCleanup
from camunda_mcp.api.camunda7.identity import Camunda7Identity
from camunda_mcp.api.camunda7.incident import Camunda7Incident
from camunda_mcp.api.camunda7.job import Camunda7Job
from camunda_mcp.api.camunda7.job_definition import Camunda7JobDefinition
from camunda_mcp.api.camunda7.message import Camunda7Message
from camunda_mcp.api.camunda7.metrics import Camunda7Metrics
from camunda_mcp.api.camunda7.migration import Camunda7Migration
from camunda_mcp.api.camunda7.modification import Camunda7Modification
from camunda_mcp.api.camunda7.process_definition import Camunda7ProcessDefinition
from camunda_mcp.api.camunda7.process_instance import Camunda7ProcessInstance
from camunda_mcp.api.camunda7.process_instance_comment import (
    Camunda7ProcessInstanceComment,
)
from camunda_mcp.api.camunda7.schema_log import Camunda7SchemaLog
from camunda_mcp.api.camunda7.signal import Camunda7Signal
from camunda_mcp.api.camunda7.task import Camunda7Task
from camunda_mcp.api.camunda7.task_attachment import Camunda7TaskAttachment
from camunda_mcp.api.camunda7.task_comment import Camunda7TaskComment
from camunda_mcp.api.camunda7.task_identity_link import Camunda7TaskIdentityLink
from camunda_mcp.api.camunda7.task_local_variable import Camunda7TaskLocalVariable
from camunda_mcp.api.camunda7.task_variable import Camunda7TaskVariable
from camunda_mcp.api.camunda7.telemetry import Camunda7Telemetry
from camunda_mcp.api.camunda7.tenant import Camunda7Tenant
from camunda_mcp.api.camunda7.user import Camunda7User
from camunda_mcp.api.camunda7.variable_instance import Camunda7VariableInstance
from camunda_mcp.api.camunda7.version import Camunda7Version

__all__ = [
    "Camunda7Authorization",
    "Camunda7Batch",
    "Camunda7Condition",
    "Camunda7DecisionDefinition",
    "Camunda7DecisionRequirementsDefinition",
    "Camunda7Deployment",
    "Camunda7Engine",
    "Camunda7EventSubscription",
    "Camunda7Execution",
    "Camunda7ExternalTask",
    "Camunda7Filter",
    "Camunda7Group",
    "Camunda7HistoricActivityInstance",
    "Camunda7HistoricBatch",
    "Camunda7HistoricDecisionDefinition",
    "Camunda7HistoricDecisionInstance",
    "Camunda7HistoricDecisionRequirementsDefinition",
    "Camunda7HistoricDetail",
    "Camunda7HistoricExternalTaskLog",
    "Camunda7HistoricIdentityLinkLog",
    "Camunda7HistoricIncident",
    "Camunda7HistoricJobLog",
    "Camunda7HistoricProcessDefinition",
    "Camunda7HistoricProcessInstance",
    "Camunda7HistoricTaskInstance",
    "Camunda7HistoricUserOperationLog",
    "Camunda7HistoricVariableInstance",
    "Camunda7HistoryCleanup",
    "Camunda7Identity",
    "Camunda7Incident",
    "Camunda7Job",
    "Camunda7JobDefinition",
    "Camunda7Message",
    "Camunda7Metrics",
    "Camunda7Migration",
    "Camunda7Modification",
    "Camunda7ProcessDefinition",
    "Camunda7ProcessInstance",
    "Camunda7ProcessInstanceComment",
    "Camunda7SchemaLog",
    "Camunda7Signal",
    "Camunda7Task",
    "Camunda7TaskAttachment",
    "Camunda7TaskComment",
    "Camunda7TaskIdentityLink",
    "Camunda7TaskLocalVariable",
    "Camunda7TaskVariable",
    "Camunda7Telemetry",
    "Camunda7Tenant",
    "Camunda7User",
    "Camunda7VariableInstance",
    "Camunda7Version",
]
