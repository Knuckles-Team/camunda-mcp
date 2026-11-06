"""Operaton / Camunda 7 engine REST: the Decision Requirements Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7DecisionRequirementsDefinition(ApiClientBase):
    """Decision Requirements Definition: 11 engine REST operation(s)."""

    def get_decision_requirements_definition_by_id(
        self,
        id: str,
    ) -> Any:
        """Get Decision Requirements Definition by ID.

        Retrieves a decision requirements definition according to the
        `DecisionRequirementsDefinition` interface in the engine.

        GET /decision-requirements-definition/{id}
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/{id}",
            path={"id": id},
        )

    def get_decision_requirements_definition_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Decision Requirements Definition by Key.

        Retrieves a decision requirements definition according to the
        `DecisionRequirementsDefinition` interface in the engine. Returns the latest
        version of the decision requirements definition which belongs to no tenant.

        GET /decision-requirements-definition/key/{key}
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}",
            path={"key": key},
        )

    def get_decision_requirements_definition_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Decision Requirements Definition by Key and Tenant ID.

        Retrieves a decision requirements definition according to the
        `DecisionRequirementsDefinition` interface in the engine. Returns the latest
        version of the decision requirements definition for a tenant.

        GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}/tenant-id/{tenant-id}",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_requirements_definition_diagram_by_id(
        self,
        id: str,
    ) -> Any:
        """Get Decision Requirements Diagram by ID.

        Retrieves the diagram of a decision requirements definition.

        GET /decision-requirements-definition/{id}/diagram
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/{id}/diagram",
            path={"id": id},
        )

    def get_decision_requirements_definition_diagram_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Decision Requirements Diagram by Key.

        Retrieves the diagram of a decision requirements definition. Returns the
        diagram for the latest version of the decision requirements definition which
        belongs to no tenant.

        GET /decision-requirements-definition/key/{key}/diagram
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}/diagram",
            path={"key": key},
        )

    def get_decision_requirements_definition_diagram_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Decision Requirements Diagram by Key and Tenant ID.

        Retrieves the diagram of a decision requirements definition. Returns the
        diagram of the latest version of the decision requirements definition for a
        tenant.

        GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/diagram
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/diagram",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_requirements_definition_dmn_xml_by_id(
        self,
        id: str,
    ) -> Any:
        """Get DMN XML by ID.

        Retrieves the DMN XML of a decision requirements definition.

        GET /decision-requirements-definition/{id}/xml
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/{id}/xml",
            path={"id": id},
        )

    def get_decision_requirements_definition_dmn_xml_by_key(
        self,
        key: str,
    ) -> Any:
        """Get DMN XML by Key.

        Retrieves the DMN XML of a decision requirements definition. Returns the XML
        for the latest version of the decision requirements definition which belongs
        to no tenant.

        GET /decision-requirements-definition/key/{key}/xml
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}/xml",
            path={"key": key},
        )

    def get_decision_requirements_definition_dmn_xml_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get DMN XML by Key and Tenant ID.

        Retrieves the DMN XML of a decision requirements definition. Returns the XML
        of the latest version of the decision requirements definition for a tenant.

        GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/xml
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/xml",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_decision_requirements_definitions(
        self,
        *,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        key: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_decision_requirements_definitions_without_tenant_id: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Decision Requirements Definitions.

        Queries for decision requirements definitions that fulfill given parameters.
        Parameters may be the properties of decision requirements definitions, such
        as the name, key or version. The size of the result set can be retrieved by
        using the Get Decision Requirements Definition Count method.

        GET /decision-requirements-definition
        """
        return self._call(
            "GET",
            "/decision-requirements-definition",
            params={
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionIdIn": decision_requirements_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "key": key,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDecisionRequirementsDefinitionsWithoutTenantId": include_decision_requirements_definitions_without_tenant_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_decision_requirements_definitions_count(
        self,
        *,
        decision_requirements_definition_id: str | None = None,
        decision_requirements_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        key: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_decision_requirements_definitions_without_tenant_id: bool | None = None,
    ) -> Any:
        """Get Decision Requirements Definition Count.

        Requests the number of decision requirements definitions that fulfill the
        query criteria. Takes the same filtering parameters as the Get Decision
        Requirements Definitions method.

        GET /decision-requirements-definition/count
        """
        return self._call(
            "GET",
            "/decision-requirements-definition/count",
            params={
                "decisionRequirementsDefinitionId": decision_requirements_definition_id,
                "decisionRequirementsDefinitionIdIn": decision_requirements_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "key": key,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDecisionRequirementsDefinitionsWithoutTenantId": include_decision_requirements_definitions_without_tenant_id,
            },
        )
