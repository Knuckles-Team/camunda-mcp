"""Operaton / Camunda 7 engine REST: the Process Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, upload_part


class Camunda7ProcessInstance(ApiClientBase):
    """Process Instance: 25 engine REST operation(s)."""

    def correlate_message_async_operation(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Correlate Message Async (POST).

        Correlates a message asynchronously to executions that are waiting for this
        message. Messages will not be correlated to process definition-level start
        message events to start process instances. Request body: an object with
        messageName, processInstanceIds, processInstanceQuery,
        historicProcessInstanceQuery, variables.

        POST /process-instance/message-async
        """
        return self._call(
            "POST",
            "/process-instance/message-async",
            body=body,
        )

    def delete_async_historic_query_based(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delete Async Historic Query Based (POST).

        Deletes a set of process instances asynchronously (batch) based on a
        historic process instance query. Request body: an object with
        processInstanceIds, deleteReason, skipCustomListeners, skipSubprocesses,
        skipIoMappings, processInstanceQuery, historicProcessInstanceQuery.

        POST /process-instance/delete-historic-query-based
        """
        return self._call(
            "POST",
            "/process-instance/delete-historic-query-based",
            body=body,
        )

    def delete_process_instance(
        self,
        id: str,
        *,
        skip_custom_listeners: bool | None = None,
        skip_io_mappings: bool | None = None,
        skip_subprocesses: bool | None = None,
        fail_if_not_exists: bool | None = None,
    ) -> Any:
        """Delete.

        Deletes a running process instance by id.

        DELETE /process-instance/{id}
        """
        return self._call(
            "DELETE",
            "/process-instance/{id}",
            path={"id": id},
            params={
                "skipCustomListeners": skip_custom_listeners,
                "skipIoMappings": skip_io_mappings,
                "skipSubprocesses": skip_subprocesses,
                "failIfNotExists": fail_if_not_exists,
            },
        )

    def delete_process_instance_variable(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Delete Process Variable.

        Deletes a variable of a process instance by id.

        DELETE /process-instance/{id}/variables/{varName}
        """
        return self._call(
            "DELETE",
            "/process-instance/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
        )

    def delete_process_instances_async_operation(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delete Async (POST).

        Deletes multiple process instances asynchronously (batch). Request body: an
        object with processInstanceIds, deleteReason, skipCustomListeners,
        skipSubprocesses, skipIoMappings, processInstanceQuery,
        historicProcessInstanceQuery.

        POST /process-instance/delete
        """
        return self._call(
            "POST",
            "/process-instance/delete",
            body=body,
        )

    def get_activity_instance_tree(
        self,
        id: str,
    ) -> Any:
        """Get Activity Instance.

        Retrieves an Activity Instance (Tree) for a given process instance by id.

        GET /process-instance/{id}/activity-instances
        """
        return self._call(
            "GET",
            "/process-instance/{id}/activity-instances",
            path={"id": id},
        )

    def get_process_instance(
        self,
        id: str,
    ) -> Any:
        """Get Process Instance.

        Retrieves a process instance by id, according to the `ProcessInstance`
        interface in the engine.

        GET /process-instance/{id}
        """
        return self._call(
            "GET",
            "/process-instance/{id}",
            path={"id": id},
        )

    def get_process_instance_variable(
        self,
        id: str,
        var_name: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Process Variable.

        Retrieves a variable of a given process instance by id.

        GET /process-instance/{id}/variables/{varName}
        """
        return self._call(
            "GET",
            "/process-instance/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def get_process_instance_variable_binary(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Get Process Variable (Binary).

        Retrieves the content of a Process Variable by the Process Instance id and
        the Process Variable name. Applicable for byte array or file Process
        Variables.

        GET /process-instance/{id}/variables/{varName}/data
        """
        return self._call(
            "GET",
            "/process-instance/{id}/variables/{varName}/data",
            path={"id": id, "varName": var_name},
        )

    def get_process_instance_variables(
        self,
        id: str,
        *,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Process Variables.

        Retrieves all variables of a given process instance by id.

        GET /process-instance/{id}/variables
        """
        return self._call(
            "GET",
            "/process-instance/{id}/variables",
            path={"id": id},
            params={
                "deserializeValues": deserialize_values,
            },
        )

    def get_process_instances(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        process_instance_ids: str | None = None,
        business_key: str | None = None,
        business_key_like: str | None = None,
        case_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_key_not_in: str | None = None,
        deployment_id: str | None = None,
        super_process_instance: str | None = None,
        sub_process_instance: str | None = None,
        super_case_instance: str | None = None,
        sub_case_instance: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        with_incident: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        process_definition_without_tenant_id: bool | None = None,
        activity_id_in: str | None = None,
        root_process_instances: bool | None = None,
        root_process_instance_id: str | None = None,
        leaf_process_instances: bool | None = None,
        variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
    ) -> Any:
        """Get List.

        Queries for process instances that fulfill given parameters. Parameters may
        be static as well as dynamic runtime properties of process instances. The
        size of the result set can be retrieved by using the Get Instance Count
        method.

        GET /process-instance
        """
        return self._call(
            "GET",
            "/process-instance",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "processInstanceIds": process_instance_ids,
                "businessKey": business_key,
                "businessKeyLike": business_key_like,
                "caseInstanceId": case_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionKeyNotIn": process_definition_key_not_in,
                "deploymentId": deployment_id,
                "superProcessInstance": super_process_instance,
                "subProcessInstance": sub_process_instance,
                "superCaseInstance": super_case_instance,
                "subCaseInstance": sub_case_instance,
                "active": active,
                "suspended": suspended,
                "withIncident": with_incident,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "processDefinitionWithoutTenantId": process_definition_without_tenant_id,
                "activityIdIn": activity_id_in,
                "rootProcessInstances": root_process_instances,
                "rootProcessInstanceId": root_process_instance_id,
                "leafProcessInstances": leaf_process_instances,
                "variables": variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
            },
        )

    def get_process_instances_count(
        self,
        *,
        process_instance_ids: str | None = None,
        business_key: str | None = None,
        business_key_like: str | None = None,
        case_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_key_not_in: str | None = None,
        deployment_id: str | None = None,
        super_process_instance: str | None = None,
        sub_process_instance: str | None = None,
        super_case_instance: str | None = None,
        sub_case_instance: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        with_incident: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        process_definition_without_tenant_id: bool | None = None,
        activity_id_in: str | None = None,
        root_process_instances: bool | None = None,
        root_process_instance_id: str | None = None,
        leaf_process_instances: bool | None = None,
        variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of process instances that fulfill given parameters.

        GET /process-instance/count
        """
        return self._call(
            "GET",
            "/process-instance/count",
            params={
                "processInstanceIds": process_instance_ids,
                "businessKey": business_key,
                "businessKeyLike": business_key_like,
                "caseInstanceId": case_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionKeyNotIn": process_definition_key_not_in,
                "deploymentId": deployment_id,
                "superProcessInstance": super_process_instance,
                "subProcessInstance": sub_process_instance,
                "superCaseInstance": super_case_instance,
                "subCaseInstance": sub_case_instance,
                "active": active,
                "suspended": suspended,
                "withIncident": with_incident,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "processDefinitionWithoutTenantId": process_definition_without_tenant_id,
                "activityIdIn": activity_id_in,
                "rootProcessInstances": root_process_instances,
                "rootProcessInstanceId": root_process_instance_id,
                "leafProcessInstances": leaf_process_instances,
                "variables": variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
            },
        )

    def modify_process_instance(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Modify Process Instance Execution State.

        Submits a list of modification instructions to change a process instance's
        execution state. Request body: an object with skipCustomListeners,
        skipIoMappings, instructions, annotation.

        POST /process-instance/{id}/modification
        """
        return self._call(
            "POST",
            "/process-instance/{id}/modification",
            path={"id": id},
            body=body,
        )

    def modify_process_instance_async_operation(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Modify Process Instance Execution State Async.

        Submits a list of modification instructions to change a process instance's
        execution state async. Request body: an object with skipCustomListeners,
        skipIoMappings, instructions, annotation.

        POST /process-instance/{id}/modification-async
        """
        return self._call(
            "POST",
            "/process-instance/{id}/modification-async",
            path={"id": id},
            body=body,
        )

    def modify_process_instance_variables(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update/Delete Process Variables.

        Updates or deletes the variables of a process instance by id. Updates
        precede deletions. So, if a variable is updated AND deleted, the deletion
        overrides the update. Request body: an object with modifications, deletions.

        POST /process-instance/{id}/variables
        """
        return self._call(
            "POST",
            "/process-instance/{id}/variables",
            path={"id": id},
            body=body,
        )

    def query_process_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for process instances that fulfill given parameters through a JSON
        object. This method is slightly more powerful than the Get Instances method
        because it allows filtering by multiple process variables of types `string`,
        `number` or `boolean`. Request body: an object with deploymentId,
        processDefinitionId, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionKeyNotIn, businessKey, businessKeyLike, caseInstanceId,
        superProcessInstance, subProcessInstance, superCaseInstance,
        subCaseInstance, active, suspended, processInstanceIds, withIncident,
        incidentId, incidentType, incidentMessage, incidentMessageLike, tenantIdIn,
        withoutTenantId, processDefinitionWithoutTenantId, activityIdIn,
        rootProcessInstances, leafProcessInstances, variables,
        variableNamesIgnoreCase, variableValuesIgnoreCase, orQueries, sorting.

        POST /process-instance
        """
        return self._call(
            "POST",
            "/process-instance",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_process_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Queries for the number of process instances that fulfill the given
        parameters. This method takes the same message body as the Get Instances
        (POST) method and therefore it is slightly more powerful than the Get
        Instance Count method. Request body: an object with deploymentId,
        processDefinitionId, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionKeyNotIn, businessKey, businessKeyLike, caseInstanceId,
        superProcessInstance, subProcessInstance, superCaseInstance,
        subCaseInstance, active, suspended, processInstanceIds, withIncident,
        incidentId, incidentType, incidentMessage, incidentMessageLike, tenantIdIn,
        withoutTenantId, processDefinitionWithoutTenantId, activityIdIn,
        rootProcessInstances, leafProcessInstances, variables,
        variableNamesIgnoreCase, variableValuesIgnoreCase, orQueries, sorting.

        POST /process-instance/count
        """
        return self._call(
            "POST",
            "/process-instance/count",
            body=body,
        )

    def set_process_instance_variable(
        self,
        id: str,
        var_name: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Process Variable.

        Sets a variable of a given process instance by id. Request body: an object
        with value, type, valueInfo.

        PUT /process-instance/{id}/variables/{varName}
        """
        return self._call(
            "PUT",
            "/process-instance/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
            body=body,
        )

    def set_process_instance_variable_binary(
        self,
        id: str,
        var_name: str,
        *,
        data: str | None = None,
        value_type: str | None = None,
        filename: str | None = None,
    ) -> Any:
        """Update Process Variable (Binary).

        Sets the serialized value for a binary variable or the binary value for a
        file variable.

        POST /process-instance/{id}/variables/{varName}/data
        """
        return self._call(
            "POST",
            "/process-instance/{id}/variables/{varName}/data",
            path={"id": id, "varName": var_name},
            form={
                "valueType": value_type,
            },
            files=upload_part("data", data, filename),
        )

    def set_retries_by_process(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Job Retries Async (POST).

        Create a batch to set retries of jobs associated with given processes
        asynchronously.

        POST /process-instance/job-retries
        """
        return self._call(
            "POST",
            "/process-instance/job-retries",
            body=body,
        )

    def set_retries_by_process_historic_query_based(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Job Retries Async Historic Query Based (POST).

        Create a batch to set retries of jobs asynchronously based on a historic
        process instance query.

        POST /process-instance/job-retries-historic-query-based
        """
        return self._call(
            "POST",
            "/process-instance/job-retries-historic-query-based",
            body=body,
        )

    def set_variables_async_operation(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Variables Async (POST).

        Update or create runtime process variables in the root scope of process
        instances. Request body: an object with processInstanceIds,
        processInstanceQuery, historicProcessInstanceQuery, variables.

        POST /process-instance/variables-async
        """
        return self._call(
            "POST",
            "/process-instance/variables-async",
            body=body,
        )

    def update_suspension_state(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Activate/Suspend In Group.

        Activates or suspends process instances by providing certain criteria: #
        Activate/Suspend Process Instance By Process Definition Id * `suspend` *
        `processDefinitionId` # Activate/Suspend Process Instance By Process
        Definition Key * `suspend` * `processDefinitionKey` *
        `processDefinitionTenantId` * `processDefinitionWithoutTenantId` #
        Activate/Suspend Process Instance In Group * `suspend` * `proces...

        PUT /process-instance/suspended
        """
        return self._call(
            "PUT",
            "/process-instance/suspended",
            body=body,
        )

    def update_suspension_state_async_operation(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Activate/Suspend In Batch.

        Activates or suspends process instances asynchronously with a list of
        process instance ids, a process instance query, and/or a historical process
        instance query.

        POST /process-instance/suspended-async
        """
        return self._call(
            "POST",
            "/process-instance/suspended-async",
            body=body,
        )

    def update_suspension_state_by_id(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend Process Instance By Id.

        Activates or suspends a given process instance by id. Request body: an
        object with suspended.

        PUT /process-instance/{id}/suspended
        """
        return self._call(
            "PUT",
            "/process-instance/{id}/suspended",
            path={"id": id},
            body=body,
        )
