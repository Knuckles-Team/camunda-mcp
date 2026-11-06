---
name: camunda-mcp-operations
skill_type: skill
description: >-
  Operate any camunda-mcp tool: the full Operaton / Camunda 7 engine REST surface
  (one camunda7_<operation> tool per REST operation, grouped by area), the Camunda 8
  REST tools and the knowledge-graph ingest. Use to find the right tool for an
  engine operation that the task skills do not cover (identity, authorizations,
  tenants, filters, batches, migration, history cleanup, metrics) or to mirror
  processes into the knowledge graph. For the business workflows prefer
  camunda-deploy-business-process, camunda-run-and-monitor-instance,
  camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest, catalog, knowledge-graph]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# camunda-mcp operations

Every engine REST operation is its own typed tool named `camunda7_<operation id in
snake case>`; [the catalog](references/catalog.md) lists them by REST area with
verb and path. Each tool's description carries the upstream summary, the request
body fields and the `VERB /path` it calls.

## Conventions

- Path parameters are required arguments (`id`, `key`, `var_name`, `tenant_id`).
- Query filters are typed optional arguments in snake case (`latestVersion` ->
  `latest_version`, `processInstanceId` -> `process_instance_id`). List filters
  ending in `_in` take a comma-separated string. Booleans are sent as the engine
  expects.
- A JSON request body is the `body` argument, exactly as the engine REST API
  documents it. Variables are typed: `{"name": {"value": ..., "type": "String"}}`.
- Most lists have a `*_count` tool and a `query_*` tool (POST, filters in the body).
- Paging: `first_result`, `max_results`; ordering: `sort_by`, `sort_order`.
- Destructive tools (DELETE) ask the caller to confirm; a client that cannot
  answer passes `confirm=true` after the approval was given.
- A failed call returns the engine's own error type and message.

## Knowledge graph

`camunda_ingest_processes(platform="7", params_json="{}", include_instances=true)`
mirrors process definitions and running instances into the knowledge graph as
`:BusinessProcess` / `:ProcessInstance` nodes. The ontology
(`ontology://camunda-mcp/camunda.ttl`) models BPMN constructs for workflow-graph
generation; `ontology://camunda-mcp/contracts.ttl` holds the tool-use contracts,
links, data locations and business roles.

## Guardrails

- Never change identity, authorization, tenant or history-cleanup settings
  without approval.
- Never delete or modify business data you did not create; test objects are named
  `zz-validation-<date>`.
