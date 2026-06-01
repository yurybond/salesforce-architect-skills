---
name: salesforce-org-shape-analysis
description: 'Analyze a Salesforce metadata source directory or perform requests to retrieve necessary data using Salesforce CLI, and then extract org shape, salesforce org capabilities(products), configuration, business workflow automations, role hierarchy, security model, and integration landscape. ALWAYS invoke this skill first for Salesforce project architecture, capabilities map, workflow automations, data model, security configuration, role hierarchy, and integrations questions. For any Salesforce diagram request, run this skill before diagram generation to ground outputs in metadata evidence.'
argument-hint: 'source directory path (required), optional output directory, optional depth (quick or thorough)'
user-invocable: true
---

# Salesforce Org Shape Analysis

## What This Skill Produces

This skill inspects a Salesforce metadata source directory and produces a structured, evidence-based org model in canonical JSON.

Primary output bundles:

- `org-shape.data-model.json` for ERD generation
- `org-shape.automation.json` for sequence and swimlane generation
- `org-shape.architecture.json` for solution architecture generation
- Optional `org-shape.summary.md` derived from JSON bundles

Core requirement:

- All extracted data must be normalized into JSON with required attributes and explicit connections.
- JSON bundles are the source of truth for downstream analysis and diagram creation.

## When To Use

Use this skill when you need to:

- Understand an unfamiliar Salesforce org from source metadata
- Generate diagram-ready ERD, automation, and architecture JSON
- Produce architecture discovery notes before implementation or migration

Mandatory triggers (always run this skill):

- Any user question about current Salesforce project architecture
- Any request for Salesforce capabilities/capability map
- Any request about Salesforce workflow automations
- Any request about Salesforce data model
- Any request about Salesforce security configuration
- Any request about Salesforce role hierarchy
- Any request about Salesforce integrations

Precedence rule:

- For any Salesforce project diagram request, execute this skill first and use its JSON outputs as grounding inputs for diagram generation skills.

## Inputs

Required:
- Metadata source directory path

Optional:
- Output directory for generated JSON bundles (and optional report)
- Analysis depth: `quick` or `thorough` (default: `thorough`)

Supported source layouts:
- SFDX source format (`force-app/...`)
- Metadata API unpacked format (`objects`, `profiles`, `settings`, etc.)

## Workflow Summary

1. Validate source roots and inventory metadata artifacts.
2. Normalize artifacts into a canonical internal graph with stable IDs and evidence lineage.
3. Build three JSON bundles for data model, automation, and architecture domains.
4. Apply decision and quality gates before finalizing outputs.
5. Write output files and optional summary.

Detailed procedure:

- [Full workflow](./references/workflow.md)

## Contracts And Rules

Read these references on demand:

- [Metadata API reference mapping](./references/salesforce-metadata-api-reference.md)
- [JSON contract overview](./references/json-contract-overview.md)
- [Data model JSON contract](./references/json-contract-data-model.md)
- [Automation JSON contract](./references/json-contract-automation.md)
- [Architecture JSON contract](./references/json-contract-architecture.md)
- [Evidence model](./references/evidence-model.md)
- [Decision points and quality gates](./references/quality-gates.md)

## Output Artifacts

- `org-shape.data-model.json`
- `org-shape.automation.json`
- `org-shape.architecture.json`
- Optional `org-shape.summary.md`

## Notes

- Keep inference conservative and evidence-backed.
- Use stable IDs for deterministic diffing and diagram regeneration.
