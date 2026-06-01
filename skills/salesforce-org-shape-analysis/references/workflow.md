# Workflow

## Goal

Convert Salesforce metadata source directories into canonical JSON bundles optimized for analysis and diagram generation.

## Steps

1. Validate source path
- Confirm the directory exists and is readable.
- Detect likely Salesforce metadata roots from folders like `objects`, `settings`, `profiles`, `permissionsets`, `flows`, `classes`, `triggers`, `namedCredentials`.

2. Build metadata inventory
- Enumerate `*-meta.xml` files and key folders.
- Build counts per metadata type and per object where relevant (for example `objects/*/fields`, `objects/*/validationRules`).
- Capture notable naming patterns (`__c`, `__mdt`, `__x`).

3. Normalize into canonical internal graph
- Convert metadata artifacts into normalized nodes and edges with stable IDs.
- Apply required attributes for each domain object.
- Track lineage for each node and edge via evidence IDs.

4. Map artifacts to architecture domains
- Use [Metadata API reference mapping](./salesforce-metadata-api-reference.md).
- Group findings into:
  - Data model
  - Role hierarchy
  - Security model
  - Business logic
  - Product signals
  - Integrations inbound
  - Integrations outbound

5. Extract evidence and infer posture
- For each domain, list direct evidence with file paths.
- Infer only when supported.
- Use explicit observability classification:
  - `Observed`
  - `Inferred`
  - `Unknown`

6. Build data model JSON for ERD
- Emit object, field, and relationship entities with required attributes.
- Emit relationship edges for lookup, master-detail, junction, and external-object references.
- Include cardinality and delete behavior when available.
- Contract: [Data model JSON contract](./json-contract-data-model.md)

7. Build automation JSON for sequence and swimlane diagrams
- Emit automation actors, entry events, processing steps, decisions, data touches, and callouts.
- Emit ordered control-flow and dependency edges across flows, Apex, validation, and duplicate management.
- Include swimlane hints (human, system, integration) for each step.
- Contract: [Automation JSON contract](./json-contract-automation.md)

8. Build products and integrations JSON for architecture diagrams
- Prioritize `settings/*.settings-meta.xml` and standard/system permission sets.
- Identify product footprints with confidence.
- Emit inbound and outbound integration components and their connections.
- Capture endpoint, auth model, and trust-boundary hints where available.
- Contract: [Architecture JSON contract](./json-contract-architecture.md)

9. Analyze security and sharing posture
- Summarize profile and permission set volume and breadth.
- Identify permission set groups and muting permission sets.
- Extract OWD and sharing signals from sharing settings and sharing rules.
- Report field- and record-level restriction artifacts when present.

10. Analyze automation and custom logic
- Inventory flows, Apex classes, triggers, validation rules, duplicate and matching rules.
- Highlight likely critical processes from naming and metadata structure.
- Capture extension footprint across LWC and Aura bundles.

11. Analyze hierarchy and access topology
- Inventory roles, groups, queues, and territory model artifacts.
- Report ETM v2 depth (types, territories, rules).

12. Analyze integration topology
- Inbound: connected apps.
- Outbound: named credentials, external credentials, remote site settings.
- Note authentication clues and endpoint governance indicators.

13. Write output artifacts
- `org-shape.data-model.json`
- `org-shape.automation.json`
- `org-shape.architecture.json`
- Optional `org-shape.summary.md` derived from JSON bundles.

Apply final checks from [Decision points and quality gates](./quality-gates.md).
