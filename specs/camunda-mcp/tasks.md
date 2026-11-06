# CONN-CAMUNDA-MCP — Implementation tasks

Governing spec: [spec.md](spec.md). Design: [plan.md](plan.md). Rows: [requirements.md](requirements.md).

Each task line reads `- [ ] T001 [P] [US1] <ID>-R012.4 description`. Order is producer first.

- [x] T001 [US1] CONN-CAMUNDA-MCP-R001 Connector reports its released version.
- [x] T002 [US1] CONN-CAMUNDA-MCP-R002 One tool per engine REST operation.
- [x] T003 [US1] CONN-CAMUNDA-MCP-R003 No condensed or routed tools.
- [x] T004 [US1] CONN-CAMUNDA-MCP-R004 Engine wire values.
- [x] T005 [US1] CONN-CAMUNDA-MCP-R005 Tool-use contracts, links, data locations and roles.
- [x] T006 [US1] CONN-CAMUNDA-MCP-R006 Prompts are agent definitions; task skills.
- [x] T007 [US1] CONN-CAMUNDA-MCP-R007 BPMN ontology rolls up to core.
- [ ] T008 [US2] CONN-CAMUNDA-MCP-R008 Governed deploy sink for released process models (rollup).
- [ ] T009 [US2] CONN-CAMUNDA-MCP-R008.1 Deploy sink executes a released change set.
- [ ] T010 [US2] CONN-CAMUNDA-MCP-R008.2 Deploy sink refusal and evidence.
- [ ] T011 [US2] CONN-CAMUNDA-MCP-R008.3 Register the deploy sink and prove the path.
- [ ] T012 [US2] CONN-CAMUNDA-MCP-R009 Process instance and user task lifecycles are explicit state machines (rollup).
- [ ] T013 [US2] CONN-CAMUNDA-MCP-R009.1 Declare the instance machine and its transition function.
- [ ] T014 [US2] CONN-CAMUNDA-MCP-R009.2 Map both engine generations onto the one instance machine.
- [ ] T015 [US2] CONN-CAMUNDA-MCP-R009.3 Guard the instance operations before the engine call.
- [ ] T016 [US2] CONN-CAMUNDA-MCP-R009.4 Declare the user task machine and its transition function.
- [ ] T017 [US2] CONN-CAMUNDA-MCP-R009.8 Resolve the acting identity of task completion.
- [ ] T018 [US2] CONN-CAMUNDA-MCP-R009.5 Guard claim, unclaim and complete for user tasks.
- [ ] T019 [US2] CONN-CAMUNDA-MCP-R009.6 Lifecycle state is one typed field in the knowledge-graph mirror.
- [ ] T020 [US2] CONN-CAMUNDA-MCP-R009.7 Wiring and hot-path proof: an illegal move never reaches the engine.
