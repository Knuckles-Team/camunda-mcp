# camunda-mcp Overview

`camunda-mcp` wraps the Camunda process automation APIs with thin MCP tools,
supporting both platforms:

- **Camunda 7 / Operaton** — the whole engine REST API (`/engine-rest`), one tool
  per operation: deployments, process and decision definitions, instances,
  executions, user tasks, variables, external tasks, jobs, incidents, messages,
  signals, history, batches, migration, identity, authorization and tenants.
- **Camunda 8** — the Zeebe REST API (`/v2`), Operate REST API and Tasklist
  REST API, with optional OAuth `client_credentials` authentication.

Camunda 7 tools are named `camunda7_*` and Camunda 8 tools `camunda8_*`, so a
single server can target either deployment.
