# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.2] - 2026-11-06

### Added
- Process instance and user task lifecycles are explicit state machines (`camunda_mcp/lifecycle.py`): one closed state set, one transition function and one typed `ILLEGAL_TRANSITION` refusal per machine. Cancel (delete), suspend, activate, claim, unclaim, complete and submit read the engine state first and refuse an illegal move before any engine write. Human tasks complete as the signed-in user, tasks whose definition carries `automated=true` as the Arbora agent account (`CAMUNDA_AGENT_ACCOUNT`).
- The ontology states both machines as classes extending the core state-machine vocabulary.

### Changed
- The graph mirror carries one `lifecycleState` field in place of `processState` and `suspended`.

## [3.0.1] - 2026-11-06

### Changed
- Raise scion-sdk to 0.9.0; the prompt links name their prompts by literal so the surface audit reads every prompt as linked to its tasks.

## [3.0.0] - 2026-11-06

### Changed
- The Camunda 7 tools now cover the whole Operaton 1.0.3 engine REST API: 386 typed
  `camunda7_<operation>` tools, one per REST operation, named from the upstream
  operation id (for example `camunda7_get_process_definitions`,
  `camunda7_start_process_instance_by_key`, `camunda7_claim`, `camunda7_complete`,
  `camunda7_evaluate_decision_by_key`). The 39 earlier `camunda7_*` names are gone.
- Query and form booleans are sent as lowercase `true`/`false` (fixes HTTP 400 on
  `latestVersion`), lists as comma-separated strings; failed calls carry the engine's
  error message.
- The ontology models BPMN 2.0 and DMN constructs for workflow-graph generation and the
  engine records with their data location; every class rolls up to core by subclassing.
  Ingested nodes use `CamundaDeployment` and `CamundaUserTask`.

### Added
- Tool-use contracts, prompt/skill/tool links, data locations and business roles,
  served as `ontology://camunda-mcp/contracts.ttl`.
- Agent prompts `camunda-process-operator`, `camunda-business-process-designer` and
  `camunda-human-task-worker`; skills `camunda-deploy-business-process`,
  `camunda-run-and-monitor-instance` and `camunda-work-human-task-queue`.
- Data sources for user tasks and incidents.

### Removed
- `camunda_deploy` (use `camunda7_create_deployment` or `camunda8_deploy_resources`),
  the `camunda-process-orchestration` and `camunda-task-operations` skills.

## [2.6.8] - 2026-10-30

### Changed
- Require `scion-sdk>=0.6.4,<0.7.0`; `uv.lock` relocked.

## [2.6.5] - 2026-10-24

### Changed
- Central connector migration: requires `agent-connector-sdk>=0.5.4`; server bootstrap, version, containers, ontology artifacts, security scaffold and pre-commit config are provided centrally.

## [Unreleased]

### Added
- Added a source-backed `camunda-mcp-development` skill with the rapid delivery
  contract and focused publication checks for `PIPE-CONNSPEC-R110.4`.

## [0.1.0] - 2026-06-01
### Added
- Initial project structure and standardization
- Standardized README, AGENTS, and `.env.example`
- Copied testing and script boilerplate from gitlab-api
