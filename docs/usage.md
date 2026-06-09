# Usage — API / CLI / MCP

`camunda-mcp` exposes the same capability three ways: as **MCP tools** an agent calls,
as a **Python API** (`Api`) you import, and as a **CLI**. The full Camunda 7 / Camunda
8 surface is described in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers ten action-dispatch tools. Each
tool takes a `platform` argument (`7` or `8`) and a `params_json` payload, so a single
server can target either deployment.

| Tool | Purpose |
|---|---|
| `camunda_process` | Process definitions: list, get, BPMN XML, start, statistics, suspend |
| `camunda_instance` | Process instances: list, get, delete, variables |
| `camunda_task` | User tasks: list, get, claim, complete |
| `camunda_deploy` | Create deployments (BPMN / DMN resources) |
| `camunda_message` | Correlate and deliver messages |
| `camunda_external_task` | Fetch, lock, and complete external tasks |
| `camunda_job` | Jobs and incidents |
| `camunda_history` | Historical process and activity data |
| `camunda_deployment` | Inspect and manage deployments |
| `camunda_ops` | Camunda 8 Operate search operations |

Example agent prompts that map onto these tools:

- *"List the latest process definitions on Camunda 7"* → `camunda_process`
- *"Start the `invoice` process with these variables"* → `camunda_process`
- *"Show the open user tasks and claim the first one"* → `camunda_task`
- *"Correlate the `payment-received` message"* → `camunda_message`

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

You can also construct the facade directly:

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
camunda-agent --help               # the A2A agent server
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
