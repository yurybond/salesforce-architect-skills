# Data Model JSON Contract

## Top-Level Shape

```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "2026-05-31T00:00:00Z",
  "sourceRoots": ["force-app/main/default"],
  "entities": [],
  "relationships": [],
  "evidence": {},
  "confidence": {"dataModel": "High"}
}
```

## Required Entities Attributes

Each `entities[]` item must include:

- `id`: stable ID (for example `object:Account`)
- `type`: `object`
- `apiName`
- `label`
- `objectKind`: `standard` | `custom` | `external` | `metadata`
- `fields`: array of field objects
- `isCustomizable`
- `evidenceIds`: list of evidence IDs

## Required Field Attributes

Each field in `fields[]` must include:

- `id`: stable ID (for example `field:Account.OwnerId`)
- `apiName`
- `label`
- `dataType`
- `required`
- `isCustom`
- `isCalculated`
- `references`: array of object API names

## Required Relationships Attributes

Each `relationships[]` item must include:

- `id`
- `fromEntityId`
- `toEntityId`
- `fieldId`
- `relationshipType`: `lookup` | `masterDetail` | `externalLookup` | `indirectLookup` | `hierarchy`
- `cardinalityFrom`: `1` | `0..1` | `many`
- `cardinalityTo`: `1` | `0..1` | `many`
- `onDelete`: `cascade` | `restrict` | `setNull` | `unknown`
- `evidenceIds`

## Diagram Intent

This contract is optimized for ERD generation. `entities` map to nodes and `relationships` map to links with cardinality and delete-behavior annotations.
