"""Operaton / Camunda 7 engine REST: the Deployment operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, resource_files


class Camunda7Deployment(ApiClientBase):
    """Deployment: 10 engine REST operation(s)."""

    def create_deployment(
        self,
        *,
        tenant_id: str | None = None,
        deployment_source: str | None = None,
        deploy_changed_only: bool | None = None,
        enable_duplicate_filtering: bool | None = None,
        deployment_name: str | None = None,
        deployment_activation_time: str | None = None,
        resources: dict[str, str] | None = None,
    ) -> Any:
        """Create.

        Creates a deployment. **Security Consideration** Deployments can contain
        custom code in form of scripts or EL expressions to customize process
        behavior. This may be abused for remote execution of arbitrary code.
        ``resources`` maps each file name (process.bpmn, decision.dmn, form.form) to
        its text content.

        POST /deployment/create
        """
        return self._call(
            "POST",
            "/deployment/create",
            form={
                "tenant-id": tenant_id,
                "deployment-source": deployment_source,
                "deploy-changed-only": deploy_changed_only,
                "enable-duplicate-filtering": enable_duplicate_filtering,
                "deployment-name": deployment_name,
                "deployment-activation-time": deployment_activation_time,
            },
            files=resource_files(resources),
        )

    def delete_deployment(
        self,
        id: str,
        *,
        cascade: bool | None = None,
        skip_custom_listeners: bool | None = None,
        skip_io_mappings: bool | None = None,
    ) -> Any:
        """Delete.

        Deletes a deployment by id.

        DELETE /deployment/{id}
        """
        return self._call(
            "DELETE",
            "/deployment/{id}",
            path={"id": id},
            params={
                "cascade": cascade,
                "skipCustomListeners": skip_custom_listeners,
                "skipIoMappings": skip_io_mappings,
            },
        )

    def get_deployment(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a deployment by id, according to the `Deployment` interface of the
        engine.

        GET /deployment/{id}
        """
        return self._call(
            "GET",
            "/deployment/{id}",
            path={"id": id},
        )

    def get_deployment_resource(
        self,
        id: str,
        resource_id: str,
    ) -> Any:
        """Get Resource.

        Retrieves a deployment resource by resource id for the given deployment.

        GET /deployment/{id}/resources/{resourceId}
        """
        return self._call(
            "GET",
            "/deployment/{id}/resources/{resourceId}",
            path={"id": id, "resourceId": resource_id},
        )

    def get_deployment_resource_data(
        self,
        id: str,
        resource_id: str,
    ) -> Any:
        """Get Resource (Binary).

        Retrieves the binary content of a deployment resource for the given
        deployment by id.

        GET /deployment/{id}/resources/{resourceId}/data
        """
        return self._call(
            "GET",
            "/deployment/{id}/resources/{resourceId}/data",
            path={"id": id, "resourceId": resource_id},
        )

    def get_deployment_resources(
        self,
        id: str,
    ) -> Any:
        """Get Resources.

        Retrieves all deployment resources of a given deployment.

        GET /deployment/{id}/resources
        """
        return self._call(
            "GET",
            "/deployment/{id}/resources",
            path={"id": id},
        )

    def get_deployments(
        self,
        *,
        id: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        source: str | None = None,
        without_source: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_deployments_without_tenant_id: bool | None = None,
        after: str | None = None,
        before: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for deployments that fulfill given parameters. Parameters may be the
        properties of deployments, such as the id or name or a range of the
        deployment time. The size of the result set can be retrieved by using the
        Get Deployment count method.

        GET /deployment
        """
        return self._call(
            "GET",
            "/deployment",
            params={
                "id": id,
                "name": name,
                "nameLike": name_like,
                "source": source,
                "withoutSource": without_source,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDeploymentsWithoutTenantId": include_deployments_without_tenant_id,
                "after": after,
                "before": before,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_deployments_count(
        self,
        *,
        id: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        source: str | None = None,
        without_source: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_deployments_without_tenant_id: bool | None = None,
        after: str | None = None,
        before: str | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of deployments that fulfill given parameters. Takes
        the same parameters as the Get Deployments method.

        GET /deployment/count
        """
        return self._call(
            "GET",
            "/deployment/count",
            params={
                "id": id,
                "name": name,
                "nameLike": name_like,
                "source": source,
                "withoutSource": without_source,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeDeploymentsWithoutTenantId": include_deployments_without_tenant_id,
                "after": after,
                "before": before,
            },
        )

    def get_registered_deployments(
        self,
    ) -> Any:
        """Get Registered Deployments.

        Queries the registered deployment IDs for the current application.

        GET /deployment/registered
        """
        return self._call(
            "GET",
            "/deployment/registered",
        )

    def redeploy(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Redeploy.

        Re-deploys an existing deployment. The deployment resources to re-deploy can
        be restricted by using the properties `resourceIds` or `resourceNames`. If
        no deployment resources to re-deploy are passed then all existing resources
        of the given deployment are re-deployed. **Warning**: Deployments can
        contain custom code in form of scripts or EL expressions to customize
        process behavior. Request body: an object with resourceIds, resourceNames,
        source.

        POST /deployment/{id}/redeploy
        """
        return self._call(
            "POST",
            "/deployment/{id}/redeploy",
            path={"id": id},
            body=body,
        )
