"""Operaton / Camunda 7 engine REST: the Process Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7ProcessDefinition(ApiClientBase):
    """Process Definition: 46 engine REST operation(s)."""

    def delete_process_definition(
        self,
        id: str,
        *,
        cascade: bool | None = None,
        skip_custom_listeners: bool | None = None,
        skip_io_mappings: bool | None = None,
    ) -> Any:
        """Delete.

        Deletes a process definition by id.

        DELETE /process-definition/{id}
        """
        return self._call(
            "DELETE",
            "/process-definition/{id}",
            path={"id": id},
            params={
                "cascade": cascade,
                "skipCustomListeners": skip_custom_listeners,
                "skipIoMappings": skip_io_mappings,
            },
        )

    def delete_process_definitions_by_key(
        self,
        key: str,
        *,
        cascade: bool | None = None,
        skip_custom_listeners: bool | None = None,
        skip_io_mappings: bool | None = None,
    ) -> Any:
        """Delete By Key.

        Deletes process definitions by a given key which belong to no tenant id.

        DELETE /process-definition/key/{key}
        """
        return self._call(
            "DELETE",
            "/process-definition/key/{key}",
            path={"key": key},
            params={
                "cascade": cascade,
                "skipCustomListeners": skip_custom_listeners,
                "skipIoMappings": skip_io_mappings,
            },
        )

    def delete_process_definitions_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        cascade: bool | None = None,
        skip_custom_listeners: bool | None = None,
        skip_io_mappings: bool | None = None,
    ) -> Any:
        """Delete By Key.

        Deletes process definitions by a given key and which belong to a tenant id.

        DELETE /process-definition/key/{key}/tenant-id/{tenant-id}
        """
        return self._call(
            "DELETE",
            "/process-definition/key/{key}/tenant-id/{tenant-id}",
            path={"key": key, "tenant-id": tenant_id},
            params={
                "cascade": cascade,
                "skipCustomListeners": skip_custom_listeners,
                "skipIoMappings": skip_io_mappings,
            },
        )

    def get_activity_statistics(
        self,
        id: str,
        *,
        failed_jobs: bool | None = None,
        incidents: bool | None = None,
        incidents_for_type: str | None = None,
    ) -> Any:
        """Get Activity Instance Statistics.

        Retrieves runtime statistics of a given process definition, grouped by
        activities. These statistics include the number of running activity
        instances, optionally the number of failed jobs and also optionally the
        number of incidents either grouped by incident types or for a specific
        incident type. **Note**: This does not include historic data.

        GET /process-definition/{id}/statistics
        """
        return self._call(
            "GET",
            "/process-definition/{id}/statistics",
            path={"id": id},
            params={
                "failedJobs": failed_jobs,
                "incidents": incidents,
                "incidentsForType": incidents_for_type,
            },
        )

    def get_activity_statistics_by_process_definition_key(
        self,
        key: str,
        *,
        failed_jobs: bool | None = None,
        incidents: bool | None = None,
        incidents_for_type: str | None = None,
    ) -> Any:
        """Get Activity Instance Statistics.

        Retrieves runtime statistics of the latest version of the given process
        definition which belongs to no tenant, grouped by activities. These
        statistics include the number of running activity instances, optionally the
        number of failed jobs and also optionally the number of incidents either
        grouped by incident types or for a specific incident type. **Note**: This
        does not include historic data.

        GET /process-definition/key/{key}/statistics
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/statistics",
            path={"key": key},
            params={
                "failedJobs": failed_jobs,
                "incidents": incidents,
                "incidentsForType": incidents_for_type,
            },
        )

    def get_activity_statistics_by_process_definition_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        failed_jobs: bool | None = None,
        incidents: bool | None = None,
        incidents_for_type: str | None = None,
    ) -> Any:
        """Get Activity Instance Statistics.

        Retrieves runtime statistics of the latest version of the given process
        definition for a tenant, grouped by activities. These statistics include the
        number of running activity instances, optionally the number of failed jobs
        and also optionally the number of incidents either grouped by incident types
        or for a specific incident type. **Note**: This does not include historic
        data.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/statistics
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/statistics",
            path={"key": key, "tenant-id": tenant_id},
            params={
                "failedJobs": failed_jobs,
                "incidents": incidents,
                "incidentsForType": incidents_for_type,
            },
        )

    def get_deployed_start_form(
        self,
        id: str,
    ) -> Any:
        """Get Deployed Start Form.

        Retrieves the deployed form that can be referenced from a start event. For
        further information please refer to User Guide.

        GET /process-definition/{id}/deployed-start-form
        """
        return self._call(
            "GET",
            "/process-definition/{id}/deployed-start-form",
            path={"id": id},
        )

    def get_deployed_start_form_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Deployed Start Form.

        Retrieves the deployed form that can be referenced from a start event. For
        further information please refer to User Guide.

        GET /process-definition/key/{key}/deployed-start-form
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/deployed-start-form",
            path={"key": key},
        )

    def get_deployed_start_form_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Deployed Start Form.

        Retrieves the deployed form that can be referenced from a start event. For
        further information please refer to User Guide.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/deployed-start-form
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/deployed-start-form",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_latest_process_definition_by_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get.

        Retrieves the latest version of the process definition for tenant according
        to the `ProcessDefinition` interface in the engine.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_process_definition(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a process definition according to the `ProcessDefinition`
        interface in the engine.

        GET /process-definition/{id}
        """
        return self._call(
            "GET",
            "/process-definition/{id}",
            path={"id": id},
        )

    def get_process_definition_bpmn20_xml(
        self,
        id: str,
    ) -> Any:
        """Get XML.

        Retrieves the BPMN 2.0 XML of a process definition.

        GET /process-definition/{id}/xml
        """
        return self._call(
            "GET",
            "/process-definition/{id}/xml",
            path={"id": id},
        )

    def get_process_definition_bpmn20_xml_by_key(
        self,
        key: str,
    ) -> Any:
        """Get XML.

        Retrieves latest version the BPMN 2.0 XML of a process definition.

        GET /process-definition/key/{key}/xml
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/xml",
            path={"key": key},
        )

    def get_process_definition_bpmn20_xml_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get XML.

        Retrieves latest version the BPMN 2.0 XML of a process definition. Returns
        the XML for the latest version of the process definition for tenant.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/xml
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/xml",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_process_definition_by_key(
        self,
        key: str,
    ) -> Any:
        """Get.

        Retrieves the latest version of the process definition which belongs to no
        tenant according to the `ProcessDefinition` interface in the engine.

        GET /process-definition/key/{key}
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}",
            path={"key": key},
        )

    def get_process_definition_diagram(
        self,
        id: str,
    ) -> Any:
        """Get Diagram.

        Retrieves the diagram of a process definition. If the process definition's
        deployment contains an image resource with the same file name as the process
        definition, the deployed image will be returned by the Get Diagram endpoint.
        Example: `someProcess.bpmn` and `someProcess.png`. Supported file extentions
        for the image are: `svg`, `png`, `jpg`, and `gif`.

        GET /process-definition/{id}/diagram
        """
        return self._call(
            "GET",
            "/process-definition/{id}/diagram",
            path={"id": id},
        )

    def get_process_definition_diagram_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Diagram.

        Retrieves the diagram for the latest version of the process definition which
        belongs to no tenant. If the process definition's deployment contains an
        image resource with the same file name as the process definition, the
        deployed image will be returned by the Get Diagram endpoint. Example:
        `someProcess.bpmn` and `someProcess.png`.

        GET /process-definition/key/{key}/diagram
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/diagram",
            path={"key": key},
        )

    def get_process_definition_diagram_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Diagram.

        Retrieves the diagram for the latest version of the process definition for
        tenant. If the process definition's deployment contains an image resource
        with the same file name as the process definition, the deployed image will
        be returned by the Get Diagram endpoint. Example: `someProcess.bpmn` and
        `someProcess.png`. Supported file extentions for the image are: `svg`,
        `png`, `jpg`, and `gif`.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/diagram
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/diagram",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_process_definition_statistics(
        self,
        *,
        failed_jobs: bool | None = None,
        incidents: bool | None = None,
        incidents_for_type: str | None = None,
        root_incidents: bool | None = None,
    ) -> Any:
        """Get Process Instance Statistics.

        Retrieves runtime statistics of the process engine, grouped by process
        definitions. These statistics include the number of running process
        instances, optionally the number of failed jobs and also optionally the
        number of incidents either grouped by incident types or for a specific
        incident type. **Note**: This does not include historic data.

        GET /process-definition/statistics
        """
        return self._call(
            "GET",
            "/process-definition/statistics",
            params={
                "failedJobs": failed_jobs,
                "incidents": incidents,
                "incidentsForType": incidents_for_type,
                "rootIncidents": root_incidents,
            },
        )

    def get_process_definitions(
        self,
        *,
        process_definition_id: str | None = None,
        process_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        deployed_after: str | None = None,
        deployed_at: str | None = None,
        key: str | None = None,
        keys_in: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        startable_by: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_process_definitions_without_tenant_id: bool | None = None,
        version_tag: str | None = None,
        version_tag_like: str | None = None,
        without_version_tag: bool | None = None,
        startable_in_tasklist: bool | None = None,
        not_startable_in_tasklist: bool | None = None,
        startable_permission_check: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for process definitions that fulfill given parameters. Parameters
        may be the properties of process definitions, such as the name, key or
        version. The size of the result set can be retrieved by using the Get
        Definition Count method.

        GET /process-definition
        """
        return self._call(
            "GET",
            "/process-definition",
            params={
                "processDefinitionId": process_definition_id,
                "processDefinitionIdIn": process_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "deployedAfter": deployed_after,
                "deployedAt": deployed_at,
                "key": key,
                "keysIn": keys_in,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "startableBy": startable_by,
                "active": active,
                "suspended": suspended,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeProcessDefinitionsWithoutTenantId": include_process_definitions_without_tenant_id,
                "versionTag": version_tag,
                "versionTagLike": version_tag_like,
                "withoutVersionTag": without_version_tag,
                "startableInTasklist": startable_in_tasklist,
                "notStartableInTasklist": not_startable_in_tasklist,
                "startablePermissionCheck": startable_permission_check,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_process_definitions_count(
        self,
        *,
        process_definition_id: str | None = None,
        process_definition_id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        deployment_id: str | None = None,
        deployed_after: str | None = None,
        deployed_at: str | None = None,
        key: str | None = None,
        keys_in: str | None = None,
        key_like: str | None = None,
        category: str | None = None,
        category_like: str | None = None,
        version: int | None = None,
        latest_version: bool | None = None,
        resource_name: str | None = None,
        resource_name_like: str | None = None,
        startable_by: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        incident_id: str | None = None,
        incident_type: str | None = None,
        incident_message: str | None = None,
        incident_message_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_process_definitions_without_tenant_id: bool | None = None,
        version_tag: str | None = None,
        version_tag_like: str | None = None,
        without_version_tag: bool | None = None,
        startable_in_tasklist: bool | None = None,
        not_startable_in_tasklist: bool | None = None,
        startable_permission_check: bool | None = None,
    ) -> Any:
        """Get List Count.

        Requests the number of process definitions that fulfill the query criteria.
        Takes the same filtering parameters as the Get Definitions method.

        GET /process-definition/count
        """
        return self._call(
            "GET",
            "/process-definition/count",
            params={
                "processDefinitionId": process_definition_id,
                "processDefinitionIdIn": process_definition_id_in,
                "name": name,
                "nameLike": name_like,
                "deploymentId": deployment_id,
                "deployedAfter": deployed_after,
                "deployedAt": deployed_at,
                "key": key,
                "keysIn": keys_in,
                "keyLike": key_like,
                "category": category,
                "categoryLike": category_like,
                "version": version,
                "latestVersion": latest_version,
                "resourceName": resource_name,
                "resourceNameLike": resource_name_like,
                "startableBy": startable_by,
                "active": active,
                "suspended": suspended,
                "incidentId": incident_id,
                "incidentType": incident_type,
                "incidentMessage": incident_message,
                "incidentMessageLike": incident_message_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeProcessDefinitionsWithoutTenantId": include_process_definitions_without_tenant_id,
                "versionTag": version_tag,
                "versionTagLike": version_tag_like,
                "withoutVersionTag": without_version_tag,
                "startableInTasklist": startable_in_tasklist,
                "notStartableInTasklist": not_startable_in_tasklist,
                "startablePermissionCheck": startable_permission_check,
            },
        )

    def get_rendered_start_form(
        self,
        id: str,
    ) -> Any:
        """Get Rendered Start Form.

        Retrieves the rendered form for a process definition. This method can be
        used to get the HTML rendering of a Generated Task Form.

        GET /process-definition/{id}/rendered-form
        """
        return self._call(
            "GET",
            "/process-definition/{id}/rendered-form",
            path={"id": id},
        )

    def get_rendered_start_form_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Rendered Start Form.

        Retrieves the rendered form for the latest version of the process definition
        which belongs to no tenant. This method can be used to get the HTML
        rendering of a Generated Task Form.

        GET /process-definition/key/{key}/rendered-form
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/rendered-form",
            path={"key": key},
        )

    def get_rendered_start_form_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Rendered Start Form.

        Retrieves the rendered form for the latest version of the process definition
        for a tenant. This method can be used to get the HTML rendering of a
        Generated Task Form.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/rendered-form
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/rendered-form",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_start_form(
        self,
        id: str,
    ) -> Any:
        """Get Start Form Key.

        Retrieves the key of the start form for a process definition. The form key
        corresponds to the `FormData#formKey` property in the engine.

        GET /process-definition/{id}/startForm
        """
        return self._call(
            "GET",
            "/process-definition/{id}/startForm",
            path={"id": id},
        )

    def get_start_form_by_key(
        self,
        key: str,
    ) -> Any:
        """Get Start Form Key.

        Retrieves the key of the start form for the latest version of the process
        definition which belongs to no tenant. The form key corresponds to the
        `FormData#formKey` property in the engine.

        GET /process-definition/key/{key}/startForm
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/startForm",
            path={"key": key},
        )

    def get_start_form_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
    ) -> Any:
        """Get Start Form Key.

        Retrieves the key of the start form for the latest version of the process
        definition for a tenant. The form key corresponds to the `FormData#formKey`
        property in the engine.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/startForm
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/startForm",
            path={"key": key, "tenant-id": tenant_id},
        )

    def get_start_form_variables(
        self,
        id: str,
        *,
        variable_names: str | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Start Form Variables.

        Retrieves the start form variables for a process definition (only if they
        are defined via the Generated Task Form approach). The start form variables
        take form data specified on the start event into account. If form fields are
        defined, the variable types and default values of the form fields are taken
        into account.

        GET /process-definition/{id}/form-variables
        """
        return self._call(
            "GET",
            "/process-definition/{id}/form-variables",
            path={"id": id},
            params={
                "variableNames": variable_names,
                "deserializeValues": deserialize_values,
            },
        )

    def get_start_form_variables_by_key(
        self,
        key: str,
        *,
        variable_names: str | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Start Form Variables.

        Retrieves the start form variables for the latest process definition which
        belongs to no tenant (only if they are defined via the Generated Task Form
        approach). The start form variables take form data specified on the start
        event into account. If form fields are defined, the variable types and
        default values of the form fields are taken into account.

        GET /process-definition/key/{key}/form-variables
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/form-variables",
            path={"key": key},
            params={
                "variableNames": variable_names,
                "deserializeValues": deserialize_values,
            },
        )

    def get_start_form_variables_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        variable_names: str | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Start Form Variables.

        Retrieves the start form variables for the latest process definition for a
        tenant (only if they are defined via the Generated Task Form approach). The
        start form variables take form data specified on the start event into
        account. If form fields are defined, the variable types and default values
        of the form fields are taken into account.

        GET /process-definition/key/{key}/tenant-id/{tenant-id}/form-variables
        """
        return self._call(
            "GET",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/form-variables",
            path={"key": key, "tenant-id": tenant_id},
            params={
                "variableNames": variable_names,
                "deserializeValues": deserialize_values,
            },
        )

    def get_static_called_process_definitions(
        self,
        id: str,
    ) -> Any:
        """Get Static Called Process Definitions.

        For the given process, returns a list of called process definitions
        corresponding to the `CalledProcessDefinition` interface in the engine. The
        list contains all process definitions that are referenced statically by call
        activities in the given process. This endpoint does not resolve process
        definitions that are referenced with expressions.

        GET /process-definition/{id}/static-called-process-definitions
        """
        return self._call(
            "GET",
            "/process-definition/{id}/static-called-process-definitions",
            path={"id": id},
        )

    def restart_process_instance(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Restart Process Instance.

        Restarts process instances that were canceled or terminated synchronously.
        Can also restart completed process instances. It will create a new instance
        using the original instance information. To execute the restart
        asynchronously, use the Restart Process Instance Async method. Request body:
        an object with processInstanceIds, historicProcessInstanceQuery,
        skipCustomListeners, skipIoMappings, initialVariables, withoutBusinessKey,
        instructions.

        POST /process-definition/{id}/restart
        """
        return self._call(
            "POST",
            "/process-definition/{id}/restart",
            path={"id": id},
            body=body,
        )

    def restart_process_instance_async_operation(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Restart Process Instance Async.

        Restarts process instances that were canceled or terminated asynchronously.
        Can also restart completed process instances. It will create a new instance
        using the original instance information. To execute the restart
        asynchronously, use the Restart Process Instance method. Request body: an
        object with processInstanceIds, historicProcessInstanceQuery,
        skipCustomListeners, skipIoMappings, initialVariables, withoutBusinessKey,
        instructions.

        POST /process-definition/{id}/restart-async
        """
        return self._call(
            "POST",
            "/process-definition/{id}/restart-async",
            path={"id": id},
            body=body,
        )

    def start_process_instance(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Start Instance.

        Instantiates a given process definition. Process variables and business key
        may be supplied in the request body. Request body: an object with
        businessKey, variables, caseInstanceId, startInstructions,
        skipCustomListeners, skipIoMappings, withVariablesInReturn.

        POST /process-definition/{id}/start
        """
        return self._call(
            "POST",
            "/process-definition/{id}/start",
            path={"id": id},
            body=body,
        )

    def start_process_instance_by_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Start Instance.

        Instantiates a given process definition, starts the latest version of the
        process definition which belongs to no tenant. Process variables and
        business key may be supplied in the request body. Request body: an object
        with businessKey, variables, caseInstanceId, startInstructions,
        skipCustomListeners, skipIoMappings, withVariablesInReturn.

        POST /process-definition/key/{key}/start
        """
        return self._call(
            "POST",
            "/process-definition/key/{key}/start",
            path={"key": key},
            body=body,
        )

    def start_process_instance_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Start Instance.

        Instantiates a given process definition, starts the latest version of the
        process definition for tenant. Process variables and business key may be
        supplied in the request body. Request body: an object with businessKey,
        variables, caseInstanceId, startInstructions, skipCustomListeners,
        skipIoMappings, withVariablesInReturn.

        POST /process-definition/key/{key}/tenant-id/{tenant-id}/start
        """
        return self._call(
            "POST",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/start",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )

    def submit_form(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Submit Start Form.

        Starts a process instance using a set of process variables and the business
        key. If the start event has Form Field Metadata defined, the process engine
        will perform backend validation for any form fields which have validators
        defined. See Documentation on Generated Task Forms. Request body: an object
        with variables, businessKey.

        POST /process-definition/{id}/submit-form
        """
        return self._call(
            "POST",
            "/process-definition/{id}/submit-form",
            path={"id": id},
            body=body,
        )

    def submit_form_by_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Submit Start Form.

        Starts the latest version of the process definition which belongs to no
        tenant using a set of process variables and the business key. If the start
        event has Form Field Metadata defined, the process engine will perform
        backend validation for any form fields which have validators defined. See
        Documentation on Generated Task Forms. Request body: an object with
        variables, businessKey.

        POST /process-definition/key/{key}/submit-form
        """
        return self._call(
            "POST",
            "/process-definition/key/{key}/submit-form",
            path={"key": key},
            body=body,
        )

    def submit_form_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Submit Start Form.

        Starts the latest version of the process definition for a tenant using a set
        of process variables and the business key. If the start event has Form Field
        Metadata defined, the process engine will perform backend validation for any
        form fields which have validators defined. See Documentation on Generated
        Task Forms. Request body: an object with variables, businessKey.

        POST /process-definition/key/{key}/tenant-id/{tenant-id}/submit-form
        """
        return self._call(
            "POST",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/submit-form",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )

    def update_history_time_to_live_by_process_definition_id(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live.

        Updates history time to live for process definition. The field is used
        within History cleanup. The value of the update is mandatory by default and
        does not allow `null` values. To enable them, please set the feature flag
        `enforceHistoryTimeToLive` to `false`. Request body: an object with
        historyTimeToLive.

        PUT /process-definition/{id}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/process-definition/{id}/history-time-to-live",
            path={"id": id},
            body=body,
        )

    def update_history_time_to_live_by_process_definition_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live.

        Updates history time to live for the latest version of the process
        definition which belongs to no tenant. The field is used within History
        cleanup. The value of the update is mandatory by default and does not allow
        `null` values. To enable them, please set the feature flag
        `enforceHistoryTimeToLive` to `false`. Request body: an object with
        historyTimeToLive.

        PUT /process-definition/key/{key}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/process-definition/key/{key}/history-time-to-live",
            path={"key": key},
            body=body,
        )

    def update_history_time_to_live_by_process_definition_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update History Time to Live.

        Updates history time to live for the latest version of the process
        definition for a tenant. The field is used within History cleanup. Request
        body: an object with historyTimeToLive.

        PUT /process-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live
        """
        return self._call(
            "PUT",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )

    def update_process_definition_suspension_state(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend By Key.

        Activates or suspends process definitions with the given process definition
        key. Request body: an object with suspended, processDefinitionId,
        processDefinitionKey, includeProcessInstances, executionDate.

        PUT /process-definition/suspended
        """
        return self._call(
            "PUT",
            "/process-definition/suspended",
            body=body,
        )

    def update_process_definition_suspension_state_by_id(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend By Id.

        Activates or suspends a given process definition by id. Request body: an
        object with suspended, processDefinitionId, processDefinitionKey,
        includeProcessInstances, executionDate.

        PUT /process-definition/{id}/suspended
        """
        return self._call(
            "PUT",
            "/process-definition/{id}/suspended",
            path={"id": id},
            body=body,
        )

    def update_process_definition_suspension_state_by_key(
        self,
        key: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend by Id.

        Activates or suspends a given process definition by latest version of
        process definition key which belongs to no tenant. Request body: an object
        with suspended, processDefinitionId, processDefinitionKey,
        includeProcessInstances, executionDate.

        PUT /process-definition/key/{key}/suspended
        """
        return self._call(
            "PUT",
            "/process-definition/key/{key}/suspended",
            path={"key": key},
            body=body,
        )

    def update_process_definition_suspension_state_by_key_and_tenant_id(
        self,
        key: str,
        tenant_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend by Id.

        Activates or suspends a given process definition by the latest version of
        the process definition for tenant. Request body: an object with suspended,
        processDefinitionId, processDefinitionKey, includeProcessInstances,
        executionDate.

        PUT /process-definition/key/{key}/tenant-id/{tenant-id}/suspended
        """
        return self._call(
            "PUT",
            "/process-definition/key/{key}/tenant-id/{tenant-id}/suspended",
            path={"key": key, "tenant-id": tenant_id},
            body=body,
        )
