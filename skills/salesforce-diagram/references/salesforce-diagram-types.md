# Diagram Type Presets

When the user requests a specific diagram type, apply the matching preset below for shapes, styles, and layout conventions. These presets set **structural** style keywords (e.g. ERD's `shape=table;childLayout=tableLayout`); a user style preset (see `references/style-presets.md`) layers color/font/edge/extras on top.

Read this file when:
- The user names one of these diagram types (ERD, UML class, sequence, architecture, ML/DL model, flowchart)
- You're choosing shape vocabulary or layout direction for a new diagram

## Salesforce Data Model (Salesforce Objects, ERD)

For Salesforce ERD and logical data model diagrams.

| Element | Style | Notes |
|---------|-------|-------|
| Standard object | `rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#e3e4e6;strokeColor=#2b2b2f;strokeWidth=3;fontStyle=1;fontFamily=Helvetica;fontSize=20;fontColor=#2d2e33;` | API name does not end with `__c` |
| Custom / licensed object | `rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontStyle=1;fontFamily=Helvetica;fontSize=20;fontColor=#003366;` | API name ends with `__c` |
| Object label format | `Label [ApiName]` | Do not append relationship counts, source paths, or other generation metadata |
| Relationship edge | `edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;` | Default connector style for Salesforce ERD |
| One-to-many | `startArrow=ERone;startFill=0;endArrow=ERzeroToMany;endFill=0;` | Parent to child relationship |
| Many-to-one | `startArrow=ERzeroToMany;startFill=0;endArrow=ERone;endFill=0;` | Child to parent lookup/master-detail |
| Optional-one to many | `startArrow=ERzeroToOne;startFill=0;endArrow=ERzeroToMany;endFill=0;` | Optional parent cardinality |
| MasterDetail mapping | `startArrow=ERone;endArrow=ERzeroToMany;` | Required parent to child cardinality |
| Lookup mapping | `startArrow=ERzeroToOne;endArrow=ERzeroToMany;` | Optional parent to child cardinality |
| Many-to-many bridge | `startArrow=ERzeroToMany;startFill=0;endArrow=ERmandOne;endFill=0;` | Use junction object between peers |
| Off-center anchor | `exitX=<0..1>;exitY=<0..1>;entryX=<0..1>;entryY=<0..1>;exitPerimeter=0;entryPerimeter=0;` | Attach to object sides instead of center when needed |
| Layout | LR with anchor object vertical spine and dependent objects on both sides | Prefer orthogonal routes; add waypoints to avoid label overlap |


## Salesforce Business Workflow (Automations)


## Salesforce Role Hierarchy

## Salesforce Architecture Diagram, Salesforce Integrations, Salesfroce Capabilities

For Salesforce solution and integration blueprints (platform, clouds, external systems, and data flow).

| Element | Style | Notes |
|---------|-------|-------|
| Salesforce cloud / product | `verticalLabelPosition=bottom;aspect=fixed;html=1;shape=mxgraph.salesforce.commerce2;` | Prefer Salesforce icon shapes when available |
| Salesforce platform service | `rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;` | Use for generic platform services (Apex, Flow, APIs) |
| Data / object store | `shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;` | For data layers, object groups, or storage |
| Integration middleware | `rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;` | MuleSoft, ETL, iPaaS, event hubs |
| External system | `rounded=1;dashed=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;` | ERP, payment providers, legacy platforms |
| User channel | `rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;` | Sales, service, commerce, partner, mobile/web |
| Sync integration edge | `edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeWidth=2;` | Request/response and API calls |
| Async/event edge | `edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;endArrow=open;strokeWidth=2;` | Platform events, CDC, streaming, batch |
| Layout | TB by domain tiers (Channels → Salesforce → Integration → External) | Keep Salesforce core centered |



