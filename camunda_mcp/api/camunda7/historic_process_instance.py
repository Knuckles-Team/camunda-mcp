"""Operaton / Camunda 7 engine REST: the Historic Process Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricProcessInstance(ApiClientBase):
    """Historic Process Instance: 10 engine REST operation(s)."""

    def delete_historic_process_instance(
        self,
        id: str,
        *,
        fail_if_not_exists: bool | None = None,
    ) -> Any:
        """Delete.

        Deletes a process instance from the history by id.

        DELETE /history/process-instance/{id}
        """
        return self._call(
            "DELETE",
            "/history/process-instance/{id}",
            path={"id": id},
            params={
                "failIfNotExists": fail_if_not_exists,
            },
        )

    def delete_historic_process_instances_async(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delete Async (POST).

        Delete multiple historic process instances asynchronously (batch). At least
        `historicProcessInstanceIds` or `historicProcessInstanceQuery` has to be
        provided. If both are provided then all instances matching query criterion
        and instances from the list will be deleted. Request body: an object with
        historicProcessInstanceIds, historicProcessInstanceQuery, deleteReason,
        failIfNotExists.

        POST /history/process-instance/delete
        """
        return self._call(
            "POST",
            "/history/process-instance/delete",
            body=body,
        )

    def delete_historic_variable_instances_of_historic_process_instance(
        self,
        id: str,
    ) -> Any:
        """Delete Variable Instances.

        Deletes all variables of a process instance from the history by id.

        DELETE /history/process-instance/{id}/variable-instances
        """
        return self._call(
            "DELETE",
            "/history/process-instance/{id}/variable-instances",
            path={"id": id},
        )

    def get_historic_process_instance(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a historic process instance by id, according to the
        `HistoricProcessInstance` interface in the engine.

        GET /history/process-instance/{id}
        """
        return self._call(
            "GET",
            "/history/process-instance/{id}",
            path={"id": id},
        )

    def get_historic_process_instance_duration_report(
        self,
        *,
        report_type: str,
        period_unit: str,
        process_definition_id_in: str | None = None,
        process_definition_key_in: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
    ) -> Any:
        """Get Duration Report.

        Retrieves a report about the duration of completed process instances,
        grouped by a period. These reports include the maximum, minimum and average
        duration of all completed process instances which were started in a given
        period. **Note:** This only includes historic data.

        GET /history/process-instance/report
        """
        return self._call(
            "GET",
            "/history/process-instance/report",
            params={
                "reportType": report_type,
                "periodUnit": period_unit,
                "processDefinitionIdIn": process_definition_id_in,
                "processDefinitionKeyIn": process_definition_key_in,
                "startedBefore": started_before,
                "startedAfter": started_after,
            },
        )

    def get_historic_process_instances(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        process_instance_id: str | None = None,
        process_instance_ids: str | None = None,
        process_instance_id_not_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        process_definition_key_not_in: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        root_process_instances: bool | None = None,
        root_process_instance_id: str | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        with_jobs_retrying: bool | None = None,
        with_incidents: bool | None = None,
        with_root_incidents: bool | None = None,
        incident_id_in: str | None = None,
        incident_type: str | None = None,
        incident_status: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        executed_activity_after: str | None = None,
        executed_activity_before: str | None = None,
        executed_job_after: str | None = None,
        executed_job_before: str | None = None,
        started_by: str | None = None,
        super_process_instance_id: str | None = None,
        sub_process_instance_id: str | None = None,
        super_case_instance_id: str | None = None,
        sub_case_instance_id: str | None = None,
        case_instance_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        activity_id_in: str | None = None,
        executed_activity_id_in: str | None = None,
        active_activity_id_in: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        completed: bool | None = None,
        externally_terminated: bool | None = None,
        internally_terminated: bool | None = None,
        variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
    ) -> Any:
        """Get List.

        Queries for historic process instances that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get Process
        Instance Count method.

        GET /history/process-instance
        """
        return self._call(
            "GET",
            "/history/process-instance",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "processInstanceId": process_instance_id,
                "processInstanceIds": process_instance_ids,
                "processInstanceIdNotIn": process_instance_id_not_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "processDefinitionKeyNotIn": process_definition_key_not_in,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "rootProcessInstances": root_process_instances,
                "rootProcessInstanceId": root_process_instance_id,
                "finished": finished,
                "unfinished": unfinished,
                "withJobsRetrying": with_jobs_retrying,
                "withIncidents": with_incidents,
                "withRootIncidents": with_root_incidents,
                "incidentIdIn": incident_id_in,
                "incidentType": incident_type,
                "incidentStatus": incident_status,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "executedActivityAfter": executed_activity_after,
                "executedActivityBefore": executed_activity_before,
                "executedJobAfter": executed_job_after,
                "executedJobBefore": executed_job_before,
                "startedBy": started_by,
                "superProcessInstanceId": super_process_instance_id,
                "subProcessInstanceId": sub_process_instance_id,
                "superCaseInstanceId": super_case_instance_id,
                "subCaseInstanceId": sub_case_instance_id,
                "caseInstanceId": case_instance_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "activityIdIn": activity_id_in,
                "executedActivityIdIn": executed_activity_id_in,
                "activeActivityIdIn": active_activity_id_in,
                "active": active,
                "suspended": suspended,
                "completed": completed,
                "externallyTerminated": externally_terminated,
                "internallyTerminated": internally_terminated,
                "variables": variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
            },
        )

    def get_historic_process_instances_count(
        self,
        *,
        process_instance_id: str | None = None,
        process_instance_ids: str | None = None,
        process_instance_id_not_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        process_definition_key_not_in: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        root_process_instances: bool | None = None,
        root_process_instance_id: str | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        with_jobs_retrying: bool | None = None,
        with_incidents: bool | None = None,
        with_root_incidents: bool | None = None,
        incident_id_in: str | None = None,
        incident_type: str | None = None,
        incident_status: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        executed_activity_after: str | None = None,
        executed_activity_before: str | None = None,
        executed_job_after: str | None = None,
        executed_job_before: str | None = None,
        started_by: str | None = None,
        super_process_instance_id: str | None = None,
        sub_process_instance_id: str | None = None,
        super_case_instance_id: str | None = None,
        sub_case_instance_id: str | None = None,
        case_instance_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        activity_id_in: str | None = None,
        executed_activity_id_in: str | None = None,
        active_activity_id_in: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        completed: bool | None = None,
        externally_terminated: bool | None = None,
        internally_terminated: bool | None = None,
        variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of historic process instances that fulfill the given
        parameters. Takes the same parameters as the Get Process Instances method.

        GET /history/process-instance/count
        """
        return self._call(
            "GET",
            "/history/process-instance/count",
            params={
                "processInstanceId": process_instance_id,
                "processInstanceIds": process_instance_ids,
                "processInstanceIdNotIn": process_instance_id_not_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "processDefinitionKeyNotIn": process_definition_key_not_in,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "rootProcessInstances": root_process_instances,
                "rootProcessInstanceId": root_process_instance_id,
                "finished": finished,
                "unfinished": unfinished,
                "withJobsRetrying": with_jobs_retrying,
                "withIncidents": with_incidents,
                "withRootIncidents": with_root_incidents,
                "incidentIdIn": incident_id_in,
                "incidentType": incident_type,
                "incidentStatus": incident_status,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "executedActivityAfter": executed_activity_after,
                "executedActivityBefore": executed_activity_before,
                "executedJobAfter": executed_job_after,
                "executedJobBefore": executed_job_before,
                "startedBy": started_by,
                "superProcessInstanceId": super_process_instance_id,
                "subProcessInstanceId": sub_process_instance_id,
                "superCaseInstanceId": super_case_instance_id,
                "subCaseInstanceId": sub_case_instance_id,
                "caseInstanceId": case_instance_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "activityIdIn": activity_id_in,
                "executedActivityIdIn": executed_activity_id_in,
                "activeActivityIdIn": active_activity_id_in,
                "active": active,
                "suspended": suspended,
                "completed": completed,
                "externallyTerminated": externally_terminated,
                "internallyTerminated": internally_terminated,
                "variables": variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
            },
        )

    def query_historic_process_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for historic process instances that fulfill the given parameters.
        This method is slightly more powerful than the Get Process Instance because
        it allows filtering by multiple process variables of types `String`,
        `Number` or `Boolean`. Request body: an object with processInstanceId,
        processInstanceIds, processInstanceIdNotIn, processDefinitionId,
        processDefinitionKey, processDefinitionKeyIn, processDefinitionName,
        processDefinitionNameLike, processDefinitionKeyNotIn,
        processInstanceBusinessKey, processInstanceBusinessKeyIn,
        processInstanceBusinessKeyLike, rootProcessInstances, rootProcessInstanceId,
        finished, unfinished, withJobsRetrying, withIncidents, withRootIncidents,
        incidentIdIn, incidentType, incidentStatus, incidentMessage,
        incidentMessageLike, startedBefore, startedAfter, finishedBefore,
        finishedAfter, executedActivityAfter, executedActivityBefore,
        executedJobAfter, executedJobBefore, startedBy, superProcessInstanceId,
        subProcessInstanceId, superCaseInstanceId, subCaseInstanceId,
        caseInstanceId, tenantIdIn, withoutTenantId, activityIdIn,
        executedActivityIdIn, activeActivityIdIn, active, suspended, completed,
        externallyTerminated, internallyTerminated, variables,
        variableNamesIgnoreCase, variableValuesIgnoreCase, orQueries, sorting.

        POST /history/process-instance
        """
        return self._call(
            "POST",
            "/history/process-instance",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_historic_process_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Queries for the number of historic process instances that fulfill the given
        parameters. This method takes the same message body as the Get Process
        Instances (POST) method and therefore it is slightly more powerful than the
        Get Process Instance Count method. Request body: an object with
        processInstanceId, processInstanceIds, processInstanceIdNotIn,
        processDefinitionId, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionName, processDefinitionNameLike, processDefinitionKeyNotIn,
        processInstanceBusinessKey, processInstanceBusinessKeyIn,
        processInstanceBusinessKeyLike, rootProcessInstances, rootProcessInstanceId,
        finished, unfinished, withJobsRetrying, withIncidents, withRootIncidents,
        incidentIdIn, incidentType, incidentStatus, incidentMessage,
        incidentMessageLike, startedBefore, startedAfter, finishedBefore,
        finishedAfter, executedActivityAfter, executedActivityBefore,
        executedJobAfter, executedJobBefore, startedBy, superProcessInstanceId,
        subProcessInstanceId, superCaseInstanceId, subCaseInstanceId,
        caseInstanceId, tenantIdIn, withoutTenantId, activityIdIn,
        executedActivityIdIn, activeActivityIdIn, active, suspended, completed,
        externallyTerminated, internallyTerminated, variables,
        variableNamesIgnoreCase, variableValuesIgnoreCase, orQueries, sorting.

        POST /history/process-instance/count
        """
        return self._call(
            "POST",
            "/history/process-instance/count",
            body=body,
        )

    def set_removal_time_async(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Removal Time Async (POST).

        Sets the removal time to multiple historic process instances asynchronously
        (batch). At least `historicProcessInstanceIds` or
        `historicProcessInstanceQuery` has to be provided. If both are provided, all
        instances matching query criterion and instances from the list will be
        updated with a removal time.

        POST /history/process-instance/set-removal-time
        """
        return self._call(
            "POST",
            "/history/process-instance/set-removal-time",
            body=body,
        )
