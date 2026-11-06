"""Operaton / Camunda 7 engine REST: the Historic Decision Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricDecisionInstance(ApiClientBase):
    """Historic Decision Instance: 5 engine REST operation(s)."""

    def delete_async(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delete Async (POST).

        Delete multiple historic decision instances asynchronously (batch). At least
        `historicDecisionInstanceIds` or `historicDecisionInstanceQuery` has to be
        provided. If both are provided then all instances matching query criterion
        and instances from the list will be deleted. Request body: an object with
        historicDecisionInstanceIds, historicDecisionInstanceQuery, deleteReason.

        POST /history/decision-instance/delete
        """
        return self._call(
            "POST",
            "/history/decision-instance/delete",
            body=body,
        )

    def get_historic_decision_instance(
        self,
        id: str,
        *,
        include_inputs: bool | None = None,
        include_outputs: bool | None = None,
        disable_binary_fetching: bool | None = None,
        disable_custom_object_deserialization: bool | None = None,
    ) -> Any:
        """Get Historic Decision Instance.

        Retrieves a historic decision instance by id, according to the
        `HistoricDecisionInstance` interface in the engine.

        GET /history/decision-instance/{id}
        """
        return self._call(
            "GET",
            "/history/decision-instance/{id}",
            path={"id": id},
            params={
                "includeInputs": include_inputs,
                "includeOutputs": include_outputs,
                "disableBinaryFetching": disable_binary_fetching,
                "disableCustomObjectDeserialization": disable_custom_object_deserialization,
            },
        )

    def get_historic_decision_instances(
        self,
        *,
        decision_instance_id: str | None = None,
        decision_instance_id_in: str | None = None,
        decision_definition_id: str | None = None,
        decision_definition_id_in: str | None = None,
        decision_definition_key: str | None = None,
        decision_definition_key_in: str | None = None,
        decision_definition_name: str | None = None,
        decision_definition_name_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_instance_id: str | None = None,
        activity_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        evaluated_before: str | None = None,
        evaluated_after: str | None = None,
        user_id: str | None = None,
        root_decision_instance_id: str | None = None,
        root_decision_instances_only: bool | None = None,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_key: str | None = None,
        include_inputs: bool | None = None,
        include_outputs: bool | None = None,
        disable_binary_fetching: bool | None = None,
        disable_custom_object_deserialization: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Historic Decision Instances.

        Queries for historic decision instances that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get Historic
        Decision Instance Count method.

        GET /history/decision-instance
        """
        return self._call(
            "GET",
            "/history/decision-instance",
            params={
                "decisionInstanceId": decision_instance_id,
                "decisionInstanceIdIn": decision_instance_id_in,
                "decisionDefinitionId": decision_definition_id,
                "decisionDefinitionIdIn": decision_definition_id_in,
                "decisionDefinitionKey": decision_definition_key,
                "decisionDefinitionKeyIn": decision_definition_key_in,
                "decisionDefinitionName": decision_definition_name,
                "decisionDefinitionNameLike": decision_definition_name_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseInstanceId": case_instance_id,
                "activityIdIn": activity_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "evaluatedBefore": evaluated_before,
                "evaluatedAfter": evaluated_after,
                "userId": user_id,
                "rootDecisionInstanceId": root_decision_instance_id,
                "rootDecisionInstancesOnly": root_decision_instances_only,
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionKey": decision_requirements_definition_key,
                "includeInputs": include_inputs,
                "includeOutputs": include_outputs,
                "disableBinaryFetching": disable_binary_fetching,
                "disableCustomObjectDeserialization": disable_custom_object_deserialization,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_decision_instances_count(
        self,
        *,
        decision_instance_id: str | None = None,
        decision_instance_id_in: str | None = None,
        decision_definition_id: str | None = None,
        decision_definition_id_in: str | None = None,
        decision_definition_key: str | None = None,
        decision_definition_key_in: str | None = None,
        decision_definition_name: str | None = None,
        decision_definition_name_like: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_instance_id: str | None = None,
        activity_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        evaluated_before: str | None = None,
        evaluated_after: str | None = None,
        user_id: str | None = None,
        root_decision_instance_id: str | None = None,
        root_decision_instances_only: bool | None = None,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_key: str | None = None,
    ) -> Any:
        """Get Historic Decision Instance Count.

        Queries for the number of historic decision instances that fulfill the given
        parameters. Takes the same parameters as the Get Historic Decision Instances
        method.

        GET /history/decision-instance/count
        """
        return self._call(
            "GET",
            "/history/decision-instance/count",
            params={
                "decisionInstanceId": decision_instance_id,
                "decisionInstanceIdIn": decision_instance_id_in,
                "decisionDefinitionId": decision_definition_id,
                "decisionDefinitionIdIn": decision_definition_id_in,
                "decisionDefinitionKey": decision_definition_key,
                "decisionDefinitionKeyIn": decision_definition_key_in,
                "decisionDefinitionName": decision_definition_name,
                "decisionDefinitionNameLike": decision_definition_name_like,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseInstanceId": case_instance_id,
                "activityIdIn": activity_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "evaluatedBefore": evaluated_before,
                "evaluatedAfter": evaluated_after,
                "userId": user_id,
                "rootDecisionInstanceId": root_decision_instance_id,
                "rootDecisionInstancesOnly": root_decision_instances_only,
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionKey": decision_requirements_definition_key,
            },
        )

    def set_removal_time_async_historic_decision_instance(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Removal Time Async (POST).

        Sets the removal time to multiple historic decision instances asynchronously
        (batch). At least `historicDecisionInstanceIds` or
        `historicDecisionInstanceQuery` has to be provided. If both are provided,
        all instances matching query criterion and instances from the list will be
        updated with a removal time.

        POST /history/decision-instance/set-removal-time
        """
        return self._call(
            "POST",
            "/history/decision-instance/set-removal-time",
            body=body,
        )
