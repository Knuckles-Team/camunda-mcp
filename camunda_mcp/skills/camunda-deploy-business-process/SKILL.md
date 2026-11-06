---
name: camunda-deploy-business-process
skill_type: skill
description: >-
  Deploy a business process to the Operaton / Camunda 7 engine through camunda-mcp:
  write or check the BPMN 2.0 and DMN XML, deploy them as one named deployment,
  read back the process and decision definitions, evaluate a decision, and retire
  an old deployment. Use when the agent must put a new or changed business process
  or business rule into the engine. Do NOT use to start or monitor instances (use
  camunda-run-and-monitor-instance) or to work human tasks (use
  camunda-work-human-task-queue).
license: MIT
tags: [camunda, operaton, bpmn, dmn, deployment, business-process]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Deploy a business process

Contracts: `deploy-business-process`, `evaluate-decision`, `retire-deployment`
(`ontology://camunda-mcp/contracts.ttl`). Data location: `process-models`.

## 1. Write the model so the engine accepts it

The engine rejects a model without these; check before deploying.

- Root: `<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
  xmlns:operaton="http://operaton.org/schema/1.0/bpmn" targetNamespace="...">`.
- Each `<bpmn:process>` has a stable `id` (the process key used to start it),
  `isExecutable="true"` and `operaton:historyTimeToLive` (for example `P30D`).
  Without a history time to live the deployment fails with ENGINE-12018.
- Every flow node is joined by `sequenceFlow` elements (`sourceRef`, `targetRef`).
  Conditions on an exclusive gateway's outgoing flows use
  `<bpmn:conditionExpression>${amount &lt; 1000}</bpmn:conditionExpression>`;
  mark one flow as the gateway's `default`.
- Human step: `<bpmn:userTask operaton:candidateGroups="finance">` (or
  `operaton:candidateUsers`, `operaton:assignee`).
- Agent step: `<bpmn:serviceTask operaton:type="external" operaton:topic="<topic>">`.
  The topic is the contract between the process and the agent worker that does
  the work (see camunda-run-and-monitor-instance).
- Rule step: `<bpmn:businessRuleTask operaton:decisionRef="<decision key>"
  operaton:mapDecisionResult="singleEntry" operaton:resultVariable="approved">`.
- Waits: timer `<bpmn:timerEventDefinition><bpmn:timeDuration>P3D</bpmn:timeDuration>`,
  message `<bpmn:messageEventDefinition messageRef="..."/>` with a
  `<bpmn:message name="...">` at the root.
- DMN: namespace `https://www.omg.org/spec/DMN/20191111/MODEL/` plus
  `xmlns:operaton="http://operaton.org/schema/1.0/dmn"`; each `<decision>` needs
  `operaton:historyTimeToLive` too, else ENGINE-22004 / ENGINE-12018.

The ontology (`ontology://camunda-mcp/camunda.ttl`) lists every BPMN construct,
the graph node it becomes (`:dagNodeKind`) and the tools that run it
(`:executedByTool`).

## 2. Deploy

1. `camunda7_get_deployments(name=<deployment name>)`: see what is already there.
2. `camunda7_create_deployment(deployment_name=..., deployment_source="camunda-mcp",
   enable_duplicate_filtering=true, resources={"<file>.bpmn": "<xml>", "<file>.dmn": "<xml>"})`.
   With duplicate filtering an unchanged model is not deployed again. The result
   lists `deployedProcessDefinitions` and `deployedDecisionDefinitions`.
   An HTTP 500 carries the parse error in its message: fix the XML and retry.
3. `camunda7_get_process_definitions(deployment_id=<id>)` and
   `camunda7_get_decision_definitions(deployment_id=<id>)`: confirm key and version.
   `latest_version=true` lists only the newest version of each key.

## 3. Evaluate a decision

`camunda7_evaluate_decision_by_key(key=<decision key>, body={"variables": {"amount":
{"value": 250, "type": "Double"}}})` returns one entry per matched rule, for
example `[{"approved": {"type": "Boolean", "value": true}}]`. Every variable is
`{"value": ..., "type": "String|Integer|Long|Double|Boolean|Date|Json"}`.
`camunda7_get_historic_decision_instances(decision_definition_key=...,
include_inputs=true, include_outputs=true)` is the audit trail.

## 4. Retire a deployment

1. `camunda7_get_process_instances(deployment_id=<id>)`: live instances?
2. Only with approval: `camunda7_delete_deployment(id=<id>, cascade=true)`. Cascade
   deletes the instances and history of that deployment as well. The tool asks the
   caller to confirm; a client that cannot answer passes `confirm=true` after the
   approval was given. Without cascade the call fails while instances exist.

## Guardrails

- Never delete a deployment you did not create or that has live business
  instances without explicit approval. Test deployments are named
  `zz-validation-<date>`.
- Deploying new versions never changes running instances; they finish on the
  version they started on.
