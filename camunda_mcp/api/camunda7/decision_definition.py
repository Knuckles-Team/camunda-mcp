"""Operaton / Camunda 7 engine REST: the Decision Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7DecisionDefinition(ApiClientBase):
    """Decision Definition: 17 engine REST operation(s)."""

    def evaluate_decision_by_id(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Evaluate By Id.

        Evaluates a given decision and returns the result. The input values of the
        decision have to be supplied in the request body. Request body: an object
        with variables.

        POST /decision-definition/{id}/evaluate
        """
        return self._call(
            "POST",
            "/decision-definition/{id}/evaluate",
            path={"id": id},
            body=body,
        )

    def evaluate_decision_by_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Evaluate By Key.

        Evaluates the latest version of the decision definition which belongs to no
        tenant. The input values of the decision have to be supplied in the request
        body. Request body: an object with variables.

        POST /decision-definition/key/{key}/evaluate
        """
        return self._call(
            "POST",
            "/decision-definition/key/{key}/evaluate",
            path={"key": key},
            body=body,
        )

    def evaluate_decision_by_key_and_tenant(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Evaluate By Key And Tenant.

        Evaluates the latest version of the decision definition for tenant. The
        input values of the decision have to be supplied in the request body.
        Request body: an object with variables.

        POST /decision-definition/key/{key}/tenant-id/{tenant-id}/evaluate
        """
        return self._call(
            "POST",
            "/decision-definition/key/{key}/tenant-id/{tenant-id}/evaluate",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )

    def get_decision_definition_by_id(
        self,
        id: str,
    ) -> Any:
        """Get Decision Definition By Id.

        Retrieves a decision definition by id, according to the `DecisionDefinition`
        interface in the engine.

        GET /decision-definition/{id}
        """
        return self._call(
            "GET",
            "/decision-definition/{id}",
            path={"id": id},
        )

    def get_decision_definition_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Decision Definition By Key.

        Retrieves the latest version of the decision definition which belongs to no
        tenant.

        GET /decision-definition/key/{key}
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}",
            path={"key": key},
        )

    def get_decision_definition_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Decision Definition By Key And Tenant Id.

        Retrieves the latest version of the decision definition for tenant

        GET /decision-definition/key/{key}/tenant-id/{tenant-id}
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}/tenant-id/{tenant-id}",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_definition_diagram(
        self,
        id: str,
    ) -> Any:
        """Get Diagram.

        Retrieves the diagram of a decision definition.

        GET /decision-definition/{id}/diagram
        """
        return self._call(
            "GET",
            "/decision-definition/{id}/diagram",
            path={"id": id},
        )

    def get_decision_definition_diagram_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Diagram By Key.

        Returns the diagram for the latest version of the decision definition which
        belongs to no tenant

        GET /decision-definition/key/{key}/diagram
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}/diagram",
            path={"key": key},
        )

    def get_decision_definition_diagram_by_key_and_tenant(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Diagram By Key And Tenant.

        Returns the XML of the latest version of the decision definition for tenant.

        GET /decision-definition/key/{key}/tenant-id/{tenant-id}/diagram
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}/tenant-id/{tenant-id}/diagram",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_definition_dmn_xml_by_id(
        self,
        id: str,
    ) -> Any:
        """Get XML By Id.

        Retrieves the DMN XML of a decision definition.

        GET /decision-definition/{id}/xml
        """
        return self._call(
            "GET",
            "/decision-definition/{id}/xml",
            path={"id": id},
        )

    def get_decision_definition_dmn_xml_by_key(
        self,
        key: str,
    ) -> Any:
        """Get XML By Key.

        Retrieves the XML for the latest version of the decision definition which
        belongs to no tenant.

        GET /decision-definition/key/{key}/xml
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}/xml",
            path={"key": key},
        )

    def get_decision_definition_dmn_xml_by_key_and_tenant(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get XML By Key and Tenant.

        Retrieves the XML of the latest version of the decision definition for
        tenant

        GET /decision-definition/key/{key}/tenant-id/{tenant-id}/xml
        """
        return self._call(
            "GET",
            "/decision-definition/key/{key}/tenant-id/{tenant-id}/xml",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_definitions(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        decision_definition_id: str | None = None,
        decision_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        deployed_after: str | None = None,
        deployed_at: str | None = None,
        key: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_key: str | None = None,
        without_decision_requirements_definition: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_decision_definitions_without_tenant_id: bool | None = None,
        version_tag: str | None = None,
        version_tag_like: str | None = None,
    ) -> Any:
        """Get List.

        Queries for decision definitions that fulfill given parameters. Parameters
        may be the properties of decision definitions, such as the name, key or
        version. The size of the result set can be retrieved by using the Get
        Decision Definition Count method.

        GET /decision-definition
        """
        return self._call(
            "GET",
            "/decision-definition",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "decisionDefinitionId": decision_definition_id,
                "decisionDefinitionIdIn": decision_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "deployedAfter": deployed_after,
                "deployedAt": deployed_at,
                "key": key,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionKey": decision_requirements_definition_key,
                "withoutDecisionRequirementsDefinition": without_decision_requirements_definition,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDecisionDefinitionsWithoutTenantId": include_decision_definitions_without_tenant_id,
                "versionTag": version_tag,
                "versionTagLike": version_tag_like,
            },
        )

    def get_decision_definitions_count(
        self,
        *,
        decision_definition_id: str | None = None,
        decision_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        deployed_after: str | None = None,
        deployed_at: str | None = None,
        key: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_key: str | None = None,
        without_decision_requirements_definition: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_decision_definitions_without_tenant_id: bool | None = None,
        version_tag: str | None = None,
        version_tag_like: str | None = None,
    ) -> Any:
        """Get List Count.

        Requests the number of decision definitions that fulfill the query criteria.
        Takes the same filtering parameters as the Get Decision Definition method.

        GET /decision-definition/count
        """
        return self._call(
            "GET",
            "/decision-definition/count",
            params={
                "decisionDefinitionId": decision_definition_id,
                "decisionDefinitionIdIn": decision_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "deployedAfter": deployed_after,
                "deployedAt": deployed_at,
                "key": key,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionKey": decision_requirements_definition_key,
                "withoutDecisionRequirementsDefinition": without_decision_requirements_definition,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDecisionDefinitionsWithoutTenantId": include_decision_definitions_without_tenant_id,
                "versionTag": version_tag,
                "versionTagLike": version_tag_like,
            },
        )

    def update_history_time_to_live_by_decision_definition_id(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live.

        Updates history time to live for decision definition. The field is used
        within History cleanup. Request body: an object with historyTimeToLive.

        PUT /decision-definition/{id}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/decision-definition/{id}/history-time-to-live",
            path={"id": id},
            body=body,
        )

    def update_history_time_to_live_by_decision_definition_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live By Key.

        Updates the latest version of the decision definition which belongs to no
        tenant. The field is used within History cleanup. Request body: an object
        with historyTimeToLive.

        PUT /decision-definition/key/{key}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/decision-definition/key/{key}/history-time-to-live",
            path={"key": key},
            body=body,
        )

    def update_history_time_to_live_by_decision_definition_key_and_tenant(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live By Key And Tenant.

        Updates the latest version of the decision definition for tenant. The field
        is used within History cleanup. The value of the update is mandatory by
        default and does not allow `null` values. To enable them, please set the
        feature flag `enforceHistoryTimeToLive` to `false`. Request body: an object
        with historyTimeToLive.

        PUT /decision-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/decision-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )
