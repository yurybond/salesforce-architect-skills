# drawio-skill

This skill generates and iterates Draw.io diagrams using local CLI export, with optional style presets and domain-specific reference packs.

## Purpose

- Generate .drawio XML for multiple diagram types.
- Export to PNG, SVG, PDF, JPG using Draw.io desktop CLI.
- Run review loops on exported previews.
- Apply reusable visual style presets (built-in and user-defined).
- Provide fallback flows when CLI export is unavailable.

## How Files Are Mapped Into AI Context

The skill is entry-pointed by SKILL.md. It uses lazy, on-demand loading for most supporting files.

### 1) Entry point and routing

- Entry file: SKILL.md
- Triggering and workflow logic live in SKILL.md.
- Supporting files are loaded only when needed, not all at once.

### 2) Explicitly mapped on-demand files (declared in SKILL.md)

These are the files the workflow explicitly tells the agent to load for specific situations:

- references/diagram-types.md
  - Loaded when user requests specific diagram families (ERD, UML, sequence, architecture, ML/DL, flowchart).
- references/style-presets.md
  - Loaded for style preset learn/apply/manage/validate flows.
- references/style-extraction.md
  - Loaded by the Learn flow (through style-presets.md) for extraction/sample rendering.
- references/troubleshooting.md
  - Loaded for export/render/vision/layout issues.
- scripts/repair_png.py
  - Executed after final PNG export with -e to repair truncated IEND bug.
- scripts/encode_drawio_url.py
  - Executed for browser fallback when CLI is unavailable.

### 3) Style file mapping

Preset resolution chain used by the workflow:

1. ~/.drawio-skill/styles/<name>.json (user presets)
2. styles/built-in/<name>.json (shipped presets)

Also relevant:

- styles/schema.json
  - Schema contract for preset shape/palette/font/edge/extras structure.
- styles/salesforce.json
  - Repository-provided branded preset (not in built-in folder).

### 4) Assets and Salesforce references

- assets/templates/*.drawio
  - Source templates/examples used for Salesforce style extraction and reusable building blocks.
- references/salesforce-architecture_shapes.md
- references/salesforce-data-model_shapes.md
- references/salesforce-icons.md
  - Domain reference catalogs for Salesforce-specific shape/style patterns.

Note: the Salesforce reference files above are currently support docs and are not listed in SKILL.md's primary bundled-resource table. They are useful for targeted authoring and extension work.

## Directory Structure

- SKILL.md
  - Skill contract, workflow orchestration, CLI/export/self-check/review loop.
- README.md
  - This documentation.
- references/
  - Operational playbooks and domain shape references.
- scripts/
  - Utility scripts invoked by workflow for repair/fallback.
- styles/
  - Preset schema and shipped style preset JSON files.
- styles/built-in/
  - Built-in preset pack (default, corporate, handdrawn).
- assets/templates/
  - Draw.io source templates and examples.

## File Linkage And Execution Flow

1. User asks for a diagram.
2. SKILL.md selects workflow and decides which references to load.
3. If style is requested or default exists, preset is resolved from user folder first, then built-ins.
4. Diagram XML is generated.
5. CLI preview export is created (non-embedded PNG).
6. Review loop updates XML iteratively.
7. Final export uses embedded outputs; PNG gets repaired by scripts/repair_png.py.
8. If CLI is unavailable, scripts/encode_drawio_url.py provides viewer URL fallback.

## Contributor Guide: Extending With New Branded Styles

Use this process for AWS, Azure, Google Cloud, Adobe Cloud, Oracle Cloud, SAP, or any internal brand.

### A) Decide the extension type

- User-only preset:
  - Create JSON in ~/.drawio-skill/styles/<brand>.json.
  - Best for local experimentation.
- Repository preset:
  - Add JSON under styles/ (project-specific) or styles/built-in/ (general shipped preset pack).
  - If you want it treated like built-ins by current lookup wording, place it in styles/built-in/.

### B) Create the preset JSON

Required top-level keys:

- name
- version (must be 1)
- palette
- roles
- shapes
- font
- edges

Optional keys:

- default (user presets only)
- confidence
- source
- extras

Follow styles/schema.json exactly.

### C) Brand mapping recommendations

- Map brand colors to semantic slots:
  - primary, success, warning, accent, danger, neutral, secondary
- Keep role mapping semantic, not vendor-product-specific:
  - service, database, queue, gateway, error, external, security
- Keep shapes portable first:
  - rounded=1, shape=cylinder3, rhombus, swimlane
- Add vendor icon shape keys only when needed and documented:
  - For example mxgraph.aws4.* or mxgraph.azure.* if your environment supports that library.

### D) Add vendor shape references (recommended)

For each new brand, add a references/<brand>-<diagram-type>_shapes.md that includes:

- Verified shape keywords available in your Draw.io environment.
- Reusable XML snippets with placeholders.
- Notes on portability when icon libraries are missing.

If you also curate large examples, add templates to assets/templates/.

### E) Wire docs so AI can discover the new brand reliably

- Update references/diagram-types.md if the brand implies a specialized diagram mode.
- Update references/style-presets.md if you introduce new extraction/management rules.
- Update SKILL.md bundled resources table if the new reference should be explicitly loaded on demand.
- Update SKILL.md built-in preset list text if you add a preset to styles/built-in/.

### F) Test checklist

- Prompt-level lookup:
  - "Use my <brand> style" loads expected preset.
- Fallback lookup:
  - If user preset is missing, built-in preset is found (if present).
- Rendering:
  - Preview PNG exports correctly.
- Final PNG repair:
  - Embedded PNG is valid after scripts/repair_png.py.
- Diagram-type interaction:
  - Structural keywords from diagram-type presets remain intact while brand palette/fonts/edges are layered.

## Practical Examples For New Brands

- AWS style pack
  - Cool blues + strong accent orange, service role can use rounded boxes or AWS icon shapes.
- Azure style pack
  - Azure-blue primary with neutral greys for external systems, orthogonal edges.
- Google Cloud style pack
  - Balanced multi-slot palette with readable stroke contrast, lighter containers.
- Adobe Cloud style pack
  - Red-accent brand mapping, careful danger/accent differentiation to avoid ambiguity.
- Oracle Cloud style pack
  - Red-focused primary with stronger neutral containers to preserve readability.
- SAP style pack
  - Blue-centric enterprise palette with clean corporate geometry and compact typography.

## Maintenance Notes

- Keep preset names lowercase to satisfy schema constraints.
- Prefer adding new capabilities via references/*.md and style JSON, not by overloading SKILL.md with vendor details.
- Keep SKILL.md as orchestration; keep brand-specific details in references/ and styles/.
