# CONN-CAMUNDA-MCP — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

This plan delivers connector identity and release metadata, the whole Operaton engine REST surface as typed tools, correct wire values, and the business-process content tier (ontology, tool-use contracts, skills, agent prompts), reusing the SDK for shared capabilities.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 7 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
camunda_mcp/__init__.py  existing
camunda_mcp/mcp/mcp_camunda.py  existing
camunda_mcp/mcp_server.py  existing
camunda_mcp/api/api_client_base.py  existing
camunda_mcp/api/api_client_camunda7.py  existing
camunda_mcp/api/camunda7/  new (one module per engine REST area)
camunda_mcp/connector_contracts.py  new
camunda_mcp/_surface.py  new
camunda_mcp/ontology/camunda.ttl  existing
camunda_mcp/prompts/  new
camunda_mcp/skills/  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

The rows are delivered in place; the design is the caller chain below.

### Governed deploy sink (R008)

`CamundaDeploySink` executes a released governed change set: one deployment per change set, named by the model id, with duplicate filtering so a re-release creates no new version. A change set that is not released, or a payload whose digest differs, refuses before any API call. The interactive deploy business task stays as it is.

### Instance and user task machines (CONN-CAMUNDA-MCP-R009)

The engine reports instance state as a string and a suspension flag, and the two engine generations use different words. `camunda_mcp/lifecycle.py` maps both onto one `InstanceState` and decides every move in `instance_transition`.

| From | Event | To |
|---|---|---|
| Created | Start | Active |
| Active | Suspend | Suspended |
| Suspended | Activate | Active |
| Active | RaiseIncident | Incident (sub-state of Active) |
| Incident | ResolveIncident | Active |
| Incident | Suspend | Suspended |
| Active, Incident | Complete | Completed |
| Active, Suspended, Incident | Cancel | Canceled |
| Active, Suspended, Incident | Terminate | Terminated |

The user task machine has Created, Claimed (with the assignee), Completed, Canceled and Deleted. Complete needs Claimed by the acting user. The guards run inside the existing generated tools through one `guarded` wrapper, so the tool surface of `CONN-CAMUNDA-MCP-R002` does not change.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff-format`, `connector-standard`, `secrets`, `tests-fast`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-CAMUNDA-MCP-R001`: the installed `camunda-mcp` distribution metadata (`pyproject.toml` line 7) -> `__version__ = _v("camunda-mcp")` in `camunda_mcp/api_client.py:18`, imported by the code that builds `Api`; `camunda_mcp/__init__.py` defines no `__version__`.
2. `CONN-CAMUNDA-MCP-R002`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) loads `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`); its `verbose_targets` prefixes `camunda7` and `camunda8` yield one tool per client method, and `camunda_mcp/mcp/mcp_camunda.py` registers `camunda_deploy` (line 50) and `camunda_ingest_processes` (line 83).
3. `CONN-CAMUNDA-MCP-R003`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) -> `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`) -> SDK `build_server` -> the tools in `camunda_mcp/mcp/mcp_camunda.py` and the generated `camunda7_*` and `camunda8_*` tools.
4. `CONN-CAMUNDA-MCP-R009`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) loads `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`) -> SDK `build_server` -> the generated tools -> `Api` (`camunda_mcp/api_client.py:21`) applies `guarded` -> `instance_transition` or `task_transition` in `camunda_mcp/lifecycle.py` -> the engine call.

## Cross-repo seams

none

### Amendments

- 2026-11-06: lifecycle state machines (organization constitution Article XXXI). Row `CONN-CAMUNDA-MCP-R009` and children R009.1 to R009.7 add guards to the existing instance and user task tools. The ontology half is `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004`.
