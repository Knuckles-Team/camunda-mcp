# camunda-mcp Overview

`camunda-mcp` wraps the Camunda process automation APIs with thin MCP tools,
supporting both platforms:

- **Camunda 7** — the Engine REST API (`/engine-rest`): process definitions,
  process instances, user tasks, deployments, history, external tasks,
  messaging, incidents and jobs.
- **Camunda 8** — the Zeebe REST API (`/v2`), Operate REST API and Tasklist
  REST API, with optional OAuth `client_credentials` authentication.

Tools accept a `platform` argument (`7` or `8`) so a single server can target
either deployment.
