# CONN-CAMUNDA-MCP-CONNECTOR-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R001` | `tests/test_default_content_surfaces.py` | The listings include the packaged skills, ontology and prompts. |

## Rows awaiting bound tests
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R002`: planned proof `tests/test_access_contracts.py::test_competency_contracts_certified`. Expected: Each entity has a contract whose operation is the existing tool and whose recording validates against it.. Refusal: A contract naming a column absent from the ontology properties or a missing recording fails certification..
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R003`: planned proof `tests/test_access_contracts.py::test_definition_document_contracts_certified`. Expected: Rollup closes when `.1` and `.2` are verified. Root test: `tests/test_access_contracts.py::test_definition_document_contracts_certified`.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R003.1`: planned proof `tests/test_access_contracts.py::test_definition_document_contracts_certified`. Expected: Each entity has a contract whose operation is a served tool.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R003.2`: planned proof `tests/test_access_contracts.py::test_definition_recordings_validate`. Expected: A recording with a column absent from the contract fails certification.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004`: planned proof `tests/test_ontology.py::test_every_class_reaches_a_core_class`. Expected: Rollup closes when its children are verified.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004.1`: planned proof `tests/test_ontology.py::test_every_class_reaches_a_core_class`. Expected: Every class reaches a core class by `rdfs:subClassOf`.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004.2`: planned proof `tests/test_ontology.py::test_ontology_states_and_transitions_equal_the_code_machines`. Expected: Ontology and code agree.
- `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004.3`: planned proof `tests/test_surface_contracts.py::test_lifecycle_guidance_names_legal_moves_and_refusal_reasons`. Expected: Guidance names the moves and the reasons.
