# salesforce-diagram

This skill generates Draw.io diagrams with Salesforce-specific templates, references, styles, and evaluation assets.

## Purpose

- Default diagram output to Draw.io artifacts.
- Ground Salesforce diagrams in the shared Salesforce diagram workflow.
- Reuse checked-in templates, reference packs, and style presets.
- Support local export helpers and evaluation metadata for the skill.

## Directory Overview

- `SKILL.md`
  - Entry point for routing, generation rules, Salesforce guardrails, and export workflow.
- `README.md`
  - This file.
- `assets/templates/`
  - Salesforce starter `.drawio` templates used during diagram generation.
- `evals/`
  - Skill evaluation definitions and per-eval metadata.
- `references/`
  - Salesforce diagram guidance, shape catalogs, style docs, and troubleshooting notes.
- `scripts/`
  - Helper scripts for export repair, browser fallback URLs, and eval maintenance.
- `styles/`
  - Style schema, Salesforce baseline style, and built-in presets.

## Current File Layout

### `assets/templates/`

- `salesforce-blank.drawio`
- `salesforce-business_capabilities.drawio`
- `salesforce-data_model.drawio`
- `salesforce-system_integrations.drawio`
- `salesforce-system_overview.drawio`

### `evals/`

- `evals.json`
- `metadata/README.md`
- `metadata/eval-01-salesforce-org-architecture.json`
- `metadata/eval-02-salesforce-erd-cardinality.json`
- `metadata/eval-03-integration-sync-async.json`
- `metadata/eval-04-security-model.json`
- `metadata/eval-05-automation-flow.json`
- `metadata/eval-06-non-salesforce-generic-architecture.json`
- `metadata/eval-07-explicit-mermaid-opt-in.json`
- `metadata/eval-08-implicit-format-default-drawio.json`
- `metadata/eval-09-header-opt-out.json`
- `metadata/eval-10-style-preset-resolution.json`
- `metadata/eval-11-export-format-constraints.json`
- `metadata/eval-12-metadata-component-map.json`

### `references/`

- `diagram-types.md`
- `salesforce-architecture_shapes.md`
- `salesforce-data-model_shapes.md`
- `salesforce-diagram-types.md`
- `salesforce-first-pass-checklist.md`
- `salesforce-icons.md`
- `salesforce-shapes.md`
- `style-extraction.md`
- `style-presets.md`
- `troubleshooting.md`

### `scripts/`

- `encode_drawio_url.py`
- `generate_grading_stubs.py`
- `repair_png.py`
- `update_grading_summary.py`

### `styles/`

- `salesforce.json`
- `schema.json`
- `built-in/default.json`
- `built-in/corporate.json`
- `built-in/handdrawn.json`

## How The Skill Uses These Files

1. `SKILL.md` routes diagram requests and enforces the Salesforce-first workflow.
2. Salesforce diagram generation starts from `assets/templates/salesforce-blank.drawio`.
3. The workflow loads files from `references/` on demand for shape guidance, style behavior, and troubleshooting.
4. Styles come from `styles/salesforce.json` or `styles/built-in/` presets, depending on the request.
5. Export and fallback helpers in `scripts/` support local diagram delivery.
6. `evals/` defines the regression suite used to validate the skill behavior.

## Maintenance Notes

- Keep this README aligned with the checked-in directories under this skill.
- When adding or removing files in `assets/`, `evals/`, `references/`, `scripts/`, or `styles/`, update the corresponding section here.
- Keep workflow details in `SKILL.md`; keep this file focused on the structure and purpose of the packaged resources.
