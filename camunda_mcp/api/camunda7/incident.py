"""Operaton / Camunda 7 engine REST: the Incident operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Incident(ApiClientBase):
    """Incident: 6 engine REST operation(s)."""

    def clear_incident_annotation(
        self,
        id: str,
    ) -> Any:
        """Clear Incident Annotation.

        Clears the annotation of an incident with given id.

        DELETE /incident/{id}/annotation
        """
        return self._call(
            "DELETE",
            "/incident/{id}/annotation",
            path={"id": id},
        )

    def get_incident(
        self,
        id: str,
    ) -> Any:
        """Get Incident.

        Retrieves an incident by ID.

        GET /incident/{id}
        """
        return self._call(
            "GET",
            "/incident/{id}",
            path={"id": id},
        )

    def get_incidents(
        self,
        *,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key_in: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        incident_timestamp_before: str | None = None,
        incident_timestamp_after: str | None = None,
        activity_id: str | None = None,
        failed_activity_id: str | None = None,
        cause_incident_id: str | None = None,
        root_cause_incident_id: str | None = None,
        configuration: str | None = None,
        tenant_id_in: str | None = None,
        job_definition_id_in: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for incidents that fulfill given parameters. The size of the result
        set can be retrieved by using the Get Incident Count method.

        GET /incident
        """
        return self._call(
            "GET",
            "/incident",
            params={
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKeyIn": process_definition_key_in,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "incidentTimestampBefore": incident_timestamp_before,
                "incidentTimestampAfter": incident_timestamp_after,
                "activityId": activity_id,
                "failedActivityId": failed_activity_id,
                "causeIncidentId": cause_incident_id,
                "rootCauseIncidentId": root_cause_incident_id,
                "configuration": configuration,
                "tenantIdIn": tenant_id_in,
                "jobDefinitionIdIn": job_definition_id_in,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_incidents_count(
        self,
        *,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key_in: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        incident_timestamp_before: str | None = None,
        incident_timestamp_after: str | None = None,
        activity_id: str | None = None,
        failed_activity_id: str | None = None,
        cause_incident_id: str | None = None,
        root_cause_incident_id: str | None = None,
        configuration: str | None = None,
        tenant_id_in: str | None = None,
        job_definition_id_in: str | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of incidents that fulfill given parameters. Takes the
        same parameters as the Get Incidents method.

        GET /incident/count
        """
        return self._call(
            "GET",
            "/incident/count",
            params={
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKeyIn": process_definition_key_in,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "incidentTimestampBefore": incident_timestamp_before,
                "incidentTimestampAfter": incident_timestamp_after,
                "activityId": activity_id,
                "failedActivityId": failed_activity_id,
                "causeIncidentId": cause_incident_id,
                "rootCauseIncidentId": root_cause_incident_id,
                "configuration": configuration,
                "tenantIdIn": tenant_id_in,
                "jobDefinitionIdIn": job_definition_id_in,
            },
        )

    def resolve_incident(
        self,
        id: str,
    ) -> Any:
        """Resolve Incident.

        Resolves an incident with given id.

        DELETE /incident/{id}
        """
        return self._call(
            "DELETE",
            "/incident/{id}",
            path={"id": id},
        )

    def set_incident_annotation(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Incident Annotation.

        Sets the annotation of an incident with given id. Request body: an object
        with annotation.

        PUT /incident/{id}/annotation
        """
        return self._call(
            "PUT",
            "/incident/{id}/annotation",
            path={"id": id},
            body=body,
        )
