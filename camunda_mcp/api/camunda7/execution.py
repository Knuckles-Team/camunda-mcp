"""Operaton / Camunda 7 engine REST: the Execution operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, upload_part


class Camunda7Execution(ApiClientBase):
    """Execution: 16 engine REST operation(s)."""

    def create_incident(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create Incident.

        Creates a custom incident with given properties. Request body: an object
        with incidentType, configuration, message.

        POST /execution/{id}/create-incident
        """
        return self._call(
            "POST",
            "/execution/{id}/create-incident",
            path={"id": id},
            body=body,
        )

    def delete_local_execution_variable(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Delete Local Execution Variable.

        Deletes a variable in the context of a given execution by id. Deletion does
        not propagate upwards in the execution hierarchy.

        DELETE /execution/{id}/localVariables/{varName}
        """
        return self._call(
            "DELETE",
            "/execution/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
        )

    def get_execution(
        self,
        id: str,
    ) -> Any:
        """Get Execution.

        Retrieves an execution by id, according to the `Execution` interface in the
        engine.

        GET /execution/{id}
        """
        return self._call(
            "GET",
            "/execution/{id}",
            path={"id": id},
        )

    def get_executions(
        self,
        *,
        business_key: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        activity_id: str | None = None,
        signal_event_subscription_name: str | None = None,
        message_event_subscription_name: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        variables: str | None = None,
        process_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Executions.

        Queries for the executions that fulfill given parameters. Parameters may be
        static as well as dynamic runtime properties of executions. The size of the
        result set can be retrieved by using the Get Execution Count method.

        GET /execution
        """
        return self._call(
            "GET",
            "/execution",
            params={
                "businessKey": business_key,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "activityId": activity_id,
                "signalEventSubscriptionName": signal_event_subscription_name,
                "messageEventSubscriptionName": message_event_subscription_name,
                "active": active,
                "suspended": suspended,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "variables": variables,
                "processVariables": process_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_executions_count(
        self,
        *,
        business_key: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        activity_id: str | None = None,
        signal_event_subscription_name: str | None = None,
        message_event_subscription_name: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        variables: str | None = None,
        process_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
    ) -> Any:
        """Get Execution Count.

        Queries for the number of executions that fulfill given parameters. Takes
        the same parameters as the Get Executions method.

        GET /execution/count
        """
        return self._call(
            "GET",
            "/execution/count",
            params={
                "businessKey": business_key,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "activityId": activity_id,
                "signalEventSubscriptionName": signal_event_subscription_name,
                "messageEventSubscriptionName": message_event_subscription_name,
                "active": active,
                "suspended": suspended,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "variables": variables,
                "processVariables": process_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
            },
        )

    def get_local_execution_variable(
        self,
        id: str,
        var_name: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Local Execution Variable.

        Retrieves a variable from the context of a given execution by id. Does not
        traverse the parent execution hierarchy.

        GET /execution/{id}/localVariables/{varName}
        """
        return self._call(
            "GET",
            "/execution/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def get_local_execution_variable_binary(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Get Local Execution Variable (Binary).

        Retrieves a binary variable from the context of a given execution by id.
        Does not traverse the parent execution hierarchy. Applicable for byte array
        and file variables.

        GET /execution/{id}/localVariables/{varName}/data
        """
        return self._call(
            "GET",
            "/execution/{id}/localVariables/{varName}/data",
            path={"id": id, "varName": var_name},
        )

    def get_local_execution_variables(
        self,
        id: str,
        *,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Local Execution Variables.

        Retrieves all variables of a given execution by id.

        GET /execution/{id}/localVariables
        """
        return self._call(
            "GET",
            "/execution/{id}/localVariables",
            path={"id": id},
            params={
                "deserializeValues": deserialize_values,
            },
        )

    def get_message_event_subscription(
        self,
        id: str,
        message_name: str,
    ) -> Any:
        """Get Message Event Subscription.

        Retrieves a message event subscription for a given execution by id and a
        message name.

        GET /execution/{id}/messageSubscriptions/{messageName}
        """
        return self._call(
            "GET",
            "/execution/{id}/messageSubscriptions/{messageName}",
            path={"id": id, "messageName": message_name},
        )

    def modify_local_execution_variables(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update/Delete Local Execution Variables.

        Updates or deletes the variables in the context of an execution by id. The
        updates do not propagate upwards in the execution hierarchy. Updates precede
        deletions. So, if a variable is updated AND deleted, the deletion overrides
        the update. Request body: an object with modifications, deletions.

        POST /execution/{id}/localVariables
        """
        return self._call(
            "POST",
            "/execution/{id}/localVariables",
            path={"id": id},
            body=body,
        )

    def put_local_execution_variable(
        self,
        id: str,
        var_name: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Put Local Execution Variable.

        Sets a variable in the context of a given execution by id. Update does not
        propagate upwards in the execution hierarchy. Request body: an object with
        value, type, valueInfo.

        PUT /execution/{id}/localVariables/{varName}
        """
        return self._call(
            "PUT",
            "/execution/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
            body=body,
        )

    def query_executions(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Executions (POST).

        Queries for executions that fulfill given parameters through a JSON object.
        This method is slightly more powerful than the Get Executions method because
        it allows to filter by multiple instance and execution variables of types
        `String`, `Number` or `Boolean`. Request body: an object with businessKey,
        processDefinitionId, processDefinitionKey, processInstanceId, activityId,
        signalEventSubscriptionName, messageEventSubscriptionName, active,
        suspended, incidentId, incidentType, incidentMessage, incidentMessageLike,
        tenantIdIn, variables, processVariables, variableNamesIgnoreCase,
        variableValuesIgnoreCase, sorting.

        POST /execution
        """
        return self._call(
            "POST",
            "/execution",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_executions_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Execution Count (POST).

        Queries for the number of executions that fulfill given parameters. This
        method takes the same message body as the Get Executions POST method and
        therefore it is slightly more powerful than the Get Execution Count method.
        Request body: an object with businessKey, processDefinitionId,
        processDefinitionKey, processInstanceId, activityId,
        signalEventSubscriptionName, messageEventSubscriptionName, active,
        suspended, incidentId, incidentType, incidentMessage, incidentMessageLike,
        tenantIdIn, variables, processVariables, variableNamesIgnoreCase,
        variableValuesIgnoreCase, sorting.

        POST /execution/count
        """
        return self._call(
            "POST",
            "/execution/count",
            body=body,
        )

    def set_local_execution_variable_binary(
        self,
        id: str,
        var_name: str,
        *,
        data: str | None = None,
        value_type: str | None = None,
        filename: str | None = None,
    ) -> Any:
        """Post Local Execution Variable (Binary).

        Sets the serialized value for a binary variable or the binary value for a
        file variable in the context of a given execution by id.

        POST /execution/{id}/localVariables/{varName}/data
        """
        return self._call(
            "POST",
            "/execution/{id}/localVariables/{varName}/data",
            path={"id": id, "varName": var_name},
            form={
                "valueType": value_type,
            },
            files=upload_part("data", data, filename),
        )

    def signal_execution(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Trigger Execution.

        Signals an execution by id. Can for example be used to explicitly skip user
        tasks or signal asynchronous continuations. Request body: an object with
        variables.

        POST /execution/{id}/signal
        """
        return self._call(
            "POST",
            "/execution/{id}/signal",
            path={"id": id},
            body=body,
        )

    def trigger_event(
        self,
        id: str,
        message_name: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Trigger Message Event Subscription.

        Delivers a message to a specific execution by id, to trigger an existing
        message event subscription. Inject process variables as the message's
        payload. Request body: an object with variables.

        POST /execution/{id}/messageSubscriptions/{messageName}/trigger
        """
        return self._call(
            "POST",
            "/execution/{id}/messageSubscriptions/{messageName}/trigger",
            path={"id": id, "messageName": message_name},
            body=body,
        )
