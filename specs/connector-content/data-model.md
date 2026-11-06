# CONN-CAMUNDA-MCP-CONNECTOR-CONTENT — Data model

Entities, classes and tables this spec adds, one section per row.

## CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R002

Row title: Declare access contracts for the competency reads of camunda-mcp.

Definition from the row: Entities: entity `process_definition` (class process definition, key `key`, columns name, deployed); entity `incident` (class incident, key `id`, columns processInstanceId, activityId).

## CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004.1

Row title: State, transition and machine classes roll up to the core vocabulary.

Definition from the row: classes ProcessInstanceLifecycle, UserTaskLifecycle (machines); ActiveState, IncidentState, SuspendedState, CompletedState, CanceledState, TerminatedState, CreatedState, ClaimedState, DeletedState (states); one transition class per table row.

## CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004.2

Row title: The ontology states equal the code enums and replace the raw state fields.

Definition from the row: property lifecycleState (object property, range: the state classes of the owning machine) replaces datatype properties processState and suspended.
