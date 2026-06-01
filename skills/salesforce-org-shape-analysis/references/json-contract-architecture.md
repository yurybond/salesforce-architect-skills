# Architecture JSON Contract

## Top-Level Shape

```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "2026-05-31T00:00:00Z",
  "sourceRoots": ["force-app/main/default"],
  "products": [],
  "integrationComponents": [],
  "connections": [],
  "evidence": {},
  "confidence": {"products": "Medium", "integrations": "High"}
}
```

## Required Products Attributes

Each `products[]` item must include:

- `id`
- `name`
- `category`: `core-cloud` | `industry-cloud` | `add-on` | `platform-feature`
- `signalType`: `setting` | `permissionSet` | `licenseProxy`
- `enabled`: boolean
- `confidence`: `High` | `Medium` | `Low`
- `evidenceIds`

## Required Integration Components Attributes

Each `integrationComponents[]` item must include:

- `id`
- `componentType`: `connectedApp` | `namedCredential` | `externalCredential` | `remoteSiteSetting` | `externalSystem`
- `name`
- `direction`: `inbound` | `outbound` | `bidirectional`
- `authType`: `oauth2` | `jwt` | `basic` | `anonymous` | `unknown`
- `endpointHost`
- `trustBoundary`: `internal` | `partner` | `public-internet` | `unknown`
- `evidenceIds`

## Required Connections Attributes

Each `connections[]` item must include:

- `id`
- `fromComponentId`
- `toComponentId`
- `connectionType`: `auth` | `api-call` | `event` | `data-sync`
- `protocol`: `https` | `soap` | `rest` | `bulk` | `platform-event` | `unknown`
- `evidenceIds`

## Diagram Intent

This contract is optimized for solution architecture diagrams. `products` define capability blocks, `integrationComponents` define system and security surfaces, and `connections` define communication paths.
