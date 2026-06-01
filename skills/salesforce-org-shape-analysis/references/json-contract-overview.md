# JSON Contract Overview

## Purpose

Define common fields and modeling rules shared by all output JSON bundles.

## Required Shared Fields

Each bundle must include:

- `schemaVersion`: fixed version string (for example `1.0.0`)
- `generatedAt`: ISO-8601 UTC timestamp
- `sourceRoots`: analyzed metadata roots
- `evidence`: object keyed by `evidenceId`
- `confidence`: domain confidence object

## Stable ID Rules

- IDs must be deterministic and repeatable for unchanged metadata.
- Use domain prefixes for readability, for example:
  - `object:Account`
  - `field:Account.OwnerId`
  - `flow:Lead_Intake`
  - `integration:NamedCredential:ERP_API`
- IDs must be unique within each bundle.

## Connection Rules

- Every connection entry must reference existing node IDs.
- Every connection entry must include `evidenceIds`.
- Use explicit `connectionType` values from the respective domain contract.

## Confidence Rules

- Use `High`, `Medium`, `Low` values.
- Domain-level confidence goes under `confidence`.
- If conflicting evidence exists, lower confidence and retain both observations.

## Related Contracts

- [Data model JSON contract](./json-contract-data-model.md)
- [Automation JSON contract](./json-contract-automation.md)
- [Architecture JSON contract](./json-contract-architecture.md)
- [Evidence model](./evidence-model.md)
