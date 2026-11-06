# Usage — API / CLI / MCP

`camunda-mcp` exposes the same capability three ways: as **MCP tools** an agent calls,
as a **Python API** (`Api`) the operator import, and as a **CLI**. The full Camunda 7 / Camunda
8 surface is described in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers 411 tools: one per API operation,
named `camunda7_<operation>` (386: the whole Operaton / Camunda 7 engine REST API, one
tool per REST operation, named from its operation id) or `camunda8_<operation>` (24,
Camunda 8 Zeebe / Operate / Tasklist REST), plus `camunda_ingest_processes`. Operation
tools take the operation's typed arguments (path parameters, typed query filters, and
the JSON `body` or multipart fields). The full list by REST area is the packaged skill
catalog `camunda_mcp/skills/camunda-mcp-operations/references/catalog.md`.

| Tool | Purpose |
|---|---|
| `camunda7_create_deployment` | Deploy BPMN / DMN / form resources (`resources`: file name to text) |
| `camunda7_get_process_definitions` | Process definitions (filters such as `latest_version`, `key`) |
| `camunda7_start_process_instance_by_key` | Start the latest version of a process |
| `camunda7_get_tasks` | Human task queue (`assignee`, `candidate_user`, `candidate_group`) |
| `camunda7_claim`, `camunda7_complete` | Claim and complete a user task |
| `camunda7_fetch_and_lock`, `camunda7_complete_external_task_resource` | External-task worker |
| `camunda7_evaluate_decision_by_key` | Evaluate a DMN decision |
| `camunda7_get_historic_process_instance` | Instance history |
| `camunda8_search_tasks` | Camunda 8 user tasks: search (also get, assign, complete) |
| `camunda_ingest_processes` | Ingest process definitions and instances into the knowledge graph |

The server also serves three agent prompts (`camunda-process-operator`,
`camunda-business-process-designer`, `camunda-human-task-worker`), the task skills
(`camunda-deploy-business-process`, `camunda-run-and-monitor-instance`,
`camunda-work-human-task-queue`, `camunda-incident-recovery`), the BPMN ontology
`ontology://camunda-mcp/camunda.ttl` and the tool-use contracts
`ontology://camunda-mcp/contracts.ttl`.

Example agent prompts that map onto these tools:

- *"Deploy this approval process"* → `camunda7_create_deployment`
- *"Start the `invoice` process for INV-1001"* → `camunda7_start_process_instance_by_key`
- *"Show the open approvals and approve the first one"* → `camunda7_get_tasks`, `camunda7_claim`, `camunda7_complete`
- *"Correlate the `payment-received` message"* → `camunda7_deliver_message`

## As a Python API

`Api` is a facade holding both platform clients, each constructed lazily, so a server
configured for one platform never needs the other's URLs or credentials.

```python
from camunda_mcp.auth import get_client

api = get_client()        # reads CAMUNDA_* from the environment / .env

# Camunda 7 (Engine REST) reads
defs = api.v7.get_process_definitions(latest_version=True)
xml = api.v7.get_process_definition_bpmn20_xml_by_key("invoice")
tasks = api.v7.get_tasks(candidate_group="finance")   # open user tasks

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
print(c7.get_process_definitions())
```

### Writes

Write operations (starting instances, completing tasks, creating deployments,
correlating messages) go through the same clients:

```python
api.v7.start_process_instance_by_key(
    "invoice", body={"businessKey": "INV-1001", "variables": {"amount": {"value": 100, "type": "Double"}}}
)
api.v7.complete(task_id, body={"variables": {"approved": {"value": True, "type": "Boolean"}}})
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
