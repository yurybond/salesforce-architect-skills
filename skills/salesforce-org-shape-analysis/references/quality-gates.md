# Decision Points And Quality Gates

## Decision Points

- If multiple potential metadata roots exist:
  - Analyze each root and merge findings with root-specific evidence paths.
- If source is incomplete:
  - Continue analysis, mark affected areas as `Partial`, and list what is missing.
- If both SFDX and unpacked MDAPI structures are present:
  - Prefer artifact-level deduplication by normalized metadata identity.
- If evidence is contradictory:
  - Keep both observations and lower confidence instead of forcing one interpretation.

## Completion Criteria

A result is complete only if it:

- Covers all core domains for org shape analysis.
- Separates `Observed`, `Inferred`, and `Unknown` statements.
- Anchors material claims to concrete metadata evidence.
- Includes confidence values per relevant domain.
- Lists key risks, gaps, and next retrieval checks.
- Avoids assumptions not evidenced in metadata.
- Produces all three required JSON bundles with required attributes.
- Produces explicit connection arrays for ERD, automation, and architecture diagram generation.

## Final Validation Checklist

- JSON bundles are syntactically valid.
- Required top-level fields are present.
- IDs are stable and unique within each bundle.
- Every relationship or connection points to valid existing node IDs.
- Every material node and edge includes `evidenceIds`.
