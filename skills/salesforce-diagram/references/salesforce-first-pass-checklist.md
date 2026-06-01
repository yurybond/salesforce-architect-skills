# Salesforce First-Pass Checklist

Use this checklist for Salesforce diagram generation before first user handoff.

Scope: applies to all Salesforce diagram families in this skill (architecture, integrations, capabilities, and data model/ERD).

## A. Template Fidelity (blocking)

- Header uses template structure:
  - Gray header container.
  - Left intro/title panel.
  - White legend box inside header.
- Legend rows are children of legend container (not floating in header root).
- Legend and header are fully visible in page bounds.
- For ERD/data model diagrams seeded from `assets/templates/salesforce-data_model.drawio`, preserve header cells and update only title/subtitle/legend content needed for the current diagram.

## B. Structural Fidelity (blocking)

Architecture/Integration/Capabilities:

- Major domains use collapsible grouping containers when diagram type supports grouped domains.
- Group container style uses `collapsible=1;container=1;recursiveResize=1` (use `alternateBounds` for collapsed state).
- Capability, integration, and external-system nodes use Salesforce card patterns (container + icon + title/text rows).
- Avoid generic fallback node styles (`rounded=1` plain rectangles, `shape=cylinder3`) for Salesforce architecture blocks unless user explicitly asks.

Data model / ERD:

- Standard vs custom object styling follows Salesforce ERD conventions.
- Relationship arrows use ER cardinality styles (not generic block arrows).
- Header structure remains present after entity/relationship edits.

## C. Icon Policy (blocking)

- Icon is semantically aligned with block meaning.
- Product/vendor-logo-like icons are used only when:
  - org evidence supports the product, or
  - user explicitly requested the product/logo.
- If no evidence/request exists, use neutral concept icons.

Neutral icon defaults (recommended):

| Block intent | Default icon |
|---|---|
| Core platform/capability | `mxgraph.salesforce.platform2` |
| Service/support capability | `mxgraph.salesforce.service2` |
| Commerce capability | `mxgraph.salesforce.commerce2` |
| Field work/operations | `mxgraph.salesforce.field_service2` |
| Automation/agent workflow | `mxgraph.salesforce.workflow2` |
| Integration concept (neutral) | `mxgraph.salesforce.workflow2` |
| External web endpoint | `mxgraph.salesforce.web2` |
| Data/extractor/search endpoint | `mxgraph.salesforce.data2` |

## D. Connection Hygiene (blocking)

- All edges connect to valid node IDs.
- Connector labels do not overlap icon/text areas.
- For dense rows, distribute edge entry/exit points or add waypoints.

## E. First-Pass Acceptance

A first draft is acceptable only when all blocking checks pass.
If any blocking check fails, fix XML and re-export before presenting to user.
