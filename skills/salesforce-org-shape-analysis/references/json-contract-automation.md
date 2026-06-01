# Automation JSON Contract

## Top-Level Shape

```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "2026-05-31T00:00:00Z",
  "sourceRoots": ["force-app/main/default"],
  "automations": [],
  "actors": [],
  "steps": [],
  "connections": [],
  "evidence": {},
  "confidence": {"automation": "Medium"}
}
```

## Required Actors Attributes

Each `actors[]` item must include:

- `id`
- `name`
- `laneType`: `human` | `salesforce-system` | `external-system`

## Required Automations Attributes

Each `automations[]` item must include:

- `id`
- `name`
- `automationType`: `flow` | `apexTrigger` | `apexClass` | `validationRule` | `duplicateRule` | `matchingRule`
- `entryEvent`: `record-create` | `record-update` | `record-delete` | `schedule` | `manual` | `api` | `unknown`
- `primaryObject`
- `stepIds`
- `evidenceIds`

## Required Steps Attributes

Each `steps[]` item must include:

- `id`
- `automationId`
- `name`
- `stepType`: `start` | `read` | `write` | `decision` | `callout` | `invoke-subflow` | `invoke-apex` | `notify` | `end`
- `laneActorId`
- `sequenceOrder`
- `touchedEntities`: entity IDs
- `evidenceIds`

## Required Connections Attributes

Each `connections[]` item must include:

- `id`
- `fromStepId`
- `toStepId`
- `connectionType`: `controlFlow` | `dataDependency` | `integrationCall`
- `condition`: branch condition or `always`
- `evidenceIds`

## Diagram Intent

This contract is optimized for sequence and swimlane diagrams. `actors` define lanes, `steps` define ordered activities, and `connections` define flow and dependencies.
