# Usage — API / CLI / MCP

`camunda-mcp` exposes the same capability three ways: as **MCP tools** an agent calls,
as a **Python API** (`Api`) the operator import, and as a **CLI**. The full Camunda 7 / Camunda
8 surface is described in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers 65 tools: one per API operation,
named `camunda7_<operation>` (39, Camunda 7 Engine REST) or `camunda8_<operation>`
(24, Camunda 8 Zeebe / Operate / Tasklist REST), plus `camunda_deploy` and
`camunda_ingest_processes`. Operation tools take the operation's typed arguments, so a
single server can target either deployment.

| Tool | Purpose |
|---|---|
| `camunda7_list_process_definitions` | Camunda 7 process definitions: list (also get, BPMN XML, statistics, suspend) |
| `camunda7_start_process_instance` | Start an instance of a Camunda 7 definition |
| `camunda7_list_tasks` | Camunda 7 user tasks: list (also get, claim, complete) |
| `camunda8_search_tasks` | Camunda 8 user tasks: search (also get, assign, complete) |
| `camunda_deploy` | Create deployments (BPMN / DMN resources) |
| `camunda_ingest_processes` | Ingest process definitions and instances into the knowledge graph |

Example agent prompts that map onto these tools:

- *"List the latest process definitions on Camunda 7"* → `camunda7_list_process_definitions`
- *"Start the `invoice` process with these variables"* → `camunda7_start_process_instance`
- *"Show the open user tasks and claim the first one"* → `camunda7_list_tasks`, `camunda7_claim_task`
- *"Correlate the `payment-received` message"* → `camunda7_correlate_message`

## As a Python API

`Api` is a facade holding both platform clients, each constructed lazily, so a server
configured for one platform never needs the other's URLs or credentials.

```python
from camunda_mcp.auth import get_client

api = get_client()        # reads CAMUNDA_* from the environment / .env

# Camunda 7 (Engine REST) reads
defs = api.v7.list_process_definitions({"latestVersion": "true"})
xml = api.v7.get_process_definition_xml(key="invoice")
tasks = api.v7.list_tasks()                # open user tasks

# Camunda 8 (Operate) reads
results = api.v8.search_process_definitions({})
```

The operator can also construct the facade directly:

```python
from camunda_mcp.api_client import Api

api = Api(
    platform="7",
    v7_kwargs={"base_url": "http://your-camunda:8080/engine-rest"},
)
c7 = api.v7
print(c7.list_process_definitions())
```

### Writes

Write operations (starting instances, completing tasks, creating deployments,
correlating messages) go through the same clients:

```python
api.v7.start_process_instance(key="invoice", body={"variables": {"amount": {"value": 100}}})
api.v7.complete_task(task_id, body={"variables": {}})
```

## As a CLI

The package installs two console scripts:

```bash
camunda-mcp --help                 # the MCP server
```

Run the MCP server over an HTTP transport:

```bash
CAMUNDA_PLATFORM=7 CAMUNDA7_URL=http://your-camunda:8080/engine-rest \
  camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Run the agent server against a deployed MCP endpoint:

```bash
MCP_URL=http://camunda-mcp:8000/mcp camunda-agent --host 0.0.0.0 --port 8001
```
