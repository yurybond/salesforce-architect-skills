# Evidence Model

## Purpose

Ensure every extracted node and connection is traceable to concrete metadata artifacts.

## Evidence Object Contract

`evidence` must be an object keyed by evidence ID. Each value must include:

- `path`: metadata file path
- `metadataType`
- `artifactName`
- `reason`: short statement explaining why the evidence supports the node or edge
- `observability`: `Observed` | `Inferred`

## Usage Rules

- Every domain object and connection must reference one or more `evidenceIds`.
- `Observed` must be used for direct metadata presence.
- `Inferred` must be used only for derived conclusions from strong signals.
- If no supporting evidence exists, do not emit the claim as fact.

## Traceability

- Keep evidence IDs stable when metadata paths and semantics are unchanged.
- Use evidence references to support confidence scoring and contradiction handling.
