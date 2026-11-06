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

Every instance pair outside this table is refused. No instance edge has a guard.

The per-version map reads generation 7 `state` plus an open incident count and generation 8 `state` plus the incident flag, and returns one `InstanceState`: ACTIVE with an open incident is Incident; EXTERNALLY_TERMINATED and INTERNALLY_TERMINATED are Terminated; CANCELED is Canceled. Created is never read from an engine.

The user task machine has the closed states Created, Claimed (with the assignee), Completed, Canceled and Deleted; the last three are terminal.

| From | Event | Guard | To |
|---|---|---|---|
| Created | Claim | none | Claimed |
| Claimed | Unclaim | none | Created |
| Claimed | Complete | acting identity equals the assignee | Completed |
| Created, Claimed | Cancel | none | Canceled |
| Created, Claimed | Delete | none | Deleted |

Every other task pair is refused. Reasons: `AlreadyClaimed`, `NotClaimed`, `ClaimedByOther`, `NoActingIdentity`, `TerminalState`, `UnknownEngineState`.

Refusal. `IllegalTransition` (code `ILLEGAL_TRANSITION`) lives in `camunda_mcp/lifecycle.py` and carries machine (`process_instance` or `user_task`), from_state, event, reason, entity and id. A refusal happens before the engine write and sends no request.

Acting identity. Task completion acts as the signed-in user for human tasks and as the Arbora agent account for automated ones. `acting_identity(task, caller)` calls a task automated when its definition carries `automated` set to true; all other user tasks are human. A human task never falls back to the agent account. When no identity resolves, the call is refused with `NoActingIdentity`.

Persisted state. The one field is `lifecycleState` on the `ProcessInstance` node (`camunda_mcp/kg_ingest.py:181`) and on the user task node (`ingest_tasks`, `camunda_mcp/kg_ingest.py:200`). The engine flags and the incident count are inputs to the map, not stored state.

Transition functions. Owner: this repository. Locations: `camunda_mcp/lifecycle.py::instance_transition` and `camunda_mcp/lifecycle.py::task_transition`. No other module branches on a raw engine state string.

Ontology. `camunda_mcp/ontology/camunda.ttl` declares `ProcessInstanceLifecycle` and `UserTaskLifecycle` as subclasses of the core `StateMachine`, the `Instance*State` and `Task*State` classes as subclasses of the core `State` (`InstanceIncidentState` under `InstanceActiveState`), one transition class per table row as subclasses of `Transition`, the events as subclasses of `Event`, the Complete guard as a subclass of `Guard`, and `InstanceTransitionRefused` and `TaskTransitionRefused` as subclasses of `TransitionRefused`. The file does not import the core ontology (`CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004`).

Wiring. `Api` (`camunda_mcp/api_client.py:21`) applies `guarded(operation, event)` to the generated methods: `cancel_process_instance` (`api_client_camunda8.py:177`), `delete_process_instance` and `update_suspension_state` (`api/camunda7/process_instance.py:52`, `:603`), and the claim, unclaim and complete methods (`api/camunda7/task.py:11`, `:872`, `:32`; `api_client_camunda8.py:315`). `guarded` reads the record, calls `instance_state_of`, then `acting_identity` for a task, then the transition function, and only then the engine write. The hot-path proof is `CONN-CAMUNDA-MCP-R009.7`.

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
