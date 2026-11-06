"""Operaton / Camunda 7 engine REST: the Historic Incident operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricIncident(ApiClientBase):
    """Historic Incident: 2 engine REST operation(s)."""

    def get_historic_incidents(
        self,
        *,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        create_time_before: str | None = None,
        create_time_after: str | None = None,
        end_time_before: str | None = None,
        end_time_after: str | None = None,
        activity_id: str | None = None,
        failed_activity_id: str | None = None,
        cause_incident_id: str | None = None,
        root_cause_incident_id: str | None = None,
        configuration: str | None = None,
        history_configuration: str | None = None,
        open: bool | None = None,
        resolved: bool | None = None,
        deleted: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        job_definition_id_in: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Incidents.

        Queries for historic incidents that fulfill given parameters. The size of
        the result set can be retrieved by using the Get Incident Count method.

        GET /history/incident
        """
        return self._call(
            "GET",
            "/history/incident",
            params={
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "createTimeBefore": create_time_before,
                "createTimeAfter": create_time_after,
                "endTimeBefore": end_time_before,
                "endTimeAfter": end_time_after,
                "activityId": activity_id,
                "failedActivityId": failed_activity_id,
                "causeIncidentId": cause_incident_id,
                "rootCauseIncidentId": root_cause_incident_id,
                "configuration": configuration,
                "historyConfiguration": history_configuration,
                "open": open,
                "resolved": resolved,
                "deleted": deleted,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "jobDefinitionIdIn": job_definition_id_in,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_incidents_count(
        self,
        *,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        create_time_before: str | None = None,
        create_time_after: str | None = None,
        end_time_before: str | None = None,
        end_time_after: str | None = None,
        activity_id: str | None = None,
        failed_activity_id: str | None = None,
        cause_incident_id: str | None = None,
        root_cause_incident_id: str | None = None,
        configuration: str | None = None,
        history_configuration: str | None = None,
        open: bool | None = None,
        resolved: bool | None = None,
        deleted: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        job_definition_id_in: str | None = None,
    ) -> Any:
        """Get Incident Count.

        Queries for the number of historic incidents that fulfill the given
        parameters. Takes the same parameters as the Get Incidents method.

        GET /history/incident/count
        """
        return self._call(
            "GET",
            "/history/incident/count",
            params={
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "createTimeBefore": create_time_before,
                "createTimeAfter": create_time_after,
                "endTimeBefore": end_time_before,
                "endTimeAfter": end_time_after,
                "activityId": activity_id,
                "failedActivityId": failed_activity_id,
                "causeIncidentId": cause_incident_id,
                "rootCauseIncidentId": root_cause_incident_id,
                "configuration": configuration,
                "historyConfiguration": history_configuration,
                "open": open,
                "resolved": resolved,
                "deleted": deleted,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "jobDefinitionIdIn": job_definition_id_in,
            },
        )
