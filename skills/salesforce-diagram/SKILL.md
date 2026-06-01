---
name: salesforce-diagram
version: 1.5.4
description: Use this skill whenever the user asks to create, draw, build, map, or generate a diagram or visual system map. Trigger for Salesforce architecture diagrams, Salesforce ERD/data model diagrams, Salesforce integrations, role hierarchy/security diagrams, metadata/component maps, and also general diagram requests such as architecture, ER/class diagrams, sequence diagrams, class diagrams, flowcharts, topology, and data-flow diagrams. If the user says diagram but no format, default to Draw.io artifacts (.drawio with optional PNG/SVG/PDF/JPG exports). Only produce Mermaid when the user explicitly asks for Mermaid.
compatibility: Requires draw.io desktop app CLI on PATH (macOS/Linux/Windows). Self-check step requires a vision-enabled model (e.g., Claude Sonnet/Opus); gracefully skipped if unavailable.

---

# Draw.io Diagrams

## Overview

Generate `.drawio` XML files and export to PNG/SVG/PDF/JPG locally using the native draw.io desktop app CLI.

Default behavior: create Draw.io artifacts only. Mermaid is opt-in and must be explicitly requested by the user.

## Activation Guardrails

Use this skill immediately when the user asks to create a diagram from a Salesforce project, Salesforce metadata, or a Salesforce org/system design.

Salesforce grounding requirement (mandatory):
- Before generating any Salesforce project diagram, execute the `salesforce-org-shape-analysis` skill first.
- Use `org-shape.data-model.json`, `org-shape.automation.json`, and `org-shape.architecture.json` as the primary grounding sources for diagram content.
- If these artifacts do not exist yet, run `salesforce-org-shape-analysis` before continuing. Do not skip this step.

Salesforce base template requirement (mandatory):
- For every Salesforce diagram type (architecture, integrations, capabilities, and data model/ERD), first copy `assets/templates/salesforce-blank.drawio` and use that copy as the working file.
- The template header area is authoritative and must remain present. Keep the structure intact while updating title/subtitle and legend labels for the current org/domain.
- Add all diagram elements below the header area. Do not place functional nodes/connectors inside or on top of the header region.
- This rule is unconditional: apply it for new diagrams, quick drafts, iterative revisions, and edits to existing diagrams.
- If an existing Salesforce diagram is not based on `salesforce-blank.drawio`, migrate content to a new copy of that template before continuing.
- Never deliver or export a Salesforce diagram variant that does not originate from `salesforce-blank.drawio`.

Salesforce first-pass generation requirement (mandatory):
- For Salesforce architecture diagrams, use template-first composition by copying `assets/templates/salesforce-blank.drawio` and applying `references/salesforce-architecture_shapes.md`.
- Keep architecture content below the inherited header and legend region from the template.
- Use Salesforce card patterns for capability/integration/external blocks; avoid fallback generic rectangle/cylinder styles unless explicitly requested.
- Use collapsible grouping containers for major domains (for example Product Signals, Integration Components, External Systems) unless the user asks for flat grouping.

Salesforce icon policy (mandatory):
- Icon choice must be semantic and neutral-first.
- Vendor/product-logo-like icons (for example MuleSoft-style integration logos) are allowed only when either:
  - metadata/evidence in org-shape outputs or retrieved metadata supports that product, or
  - the user explicitly requests that logo/product.
- If evidence is absent, use non-logo concept icons from Salesforce library (for example `mxgraph.salesforce.workflow2`, `mxgraph.salesforce.integration`, `mxgraph.salesforce.web2`, `mxgraph.salesforce.data2`).
- External systems should still use Salesforce card patterns, but with semantically relevant non-logo icons unless evidence/user request says otherwise.

Strong Salesforce triggers include requests mentioning one or more of:
- Salesforce org architecture, clouds/products, environments, tenants
- Metadata/component mapping (objects, fields, Apex, flows, LWCs, integrations)
- Data model / ERD for Salesforce entities
- Integration topology (Salesforce with external systems)
- Security and access model (profiles, permission sets, sharing/roles)

Format rules:
- Default output format is Draw.io (`.drawio`) and optional exports (PNG/SVG/PDF/JPG).
- Do not create Mermaid content (`.mmd`, Mermaid code blocks, or Mermaid sections in `.md`) unless the user explicitly asks for Mermaid.
- If the user asks for a "diagram" without format, proceed with Draw.io and do not ask a Mermaid-vs-Draw.io question unless needed.

**Supported formats:** PNG, SVG, PDF, JPG — no browser automation needed.

PNG, SVG, and PDF exports support `--embed-diagram` (`-e`) — the exported file contains the full diagram XML, so opening it in draw.io recovers the editable diagram. Use double extensions (`name.drawio.png`) to signal embedded XML.

## Bundled resources

When the workflow references one of these, read it on demand — none of them need to be in context up front.

| File | Read it when |
|---|---|
| `references/diagram-types.md` | The user names a specific diagram type (ERD, UML class, sequence, architecture, ML/DL, flowchart) |
| `references/<platform>-diagram-types.md` | A platform/tech stack was identified and a platform-specific diagram-type mapping file exists |
| `references/<platform>-*.md` | A platform/tech stack was identified and you need platform-specific shape/style guidance (for example, Salesforce/AWS/Azure/GCP/SAP/Adobe/Oracle docs) |
| `references/salesforce-first-pass-checklist.md` | Platform is Salesforce and you need to enforce template-accurate first-pass generation and pre-export quality gates |
| `assets/templates/salesforce-blank.drawio` | Platform is Salesforce; copy this file first for every new or regenerated Salesforce diagram |
| `references/style-presets.md` | The user asks to learn / save / list / set-default / delete a style preset, or you've resolved an active preset and need the application rules |
| `references/style-extraction.md` | You're inside the Learn flow and need the extraction procedure (called from `style-presets.md`) |
| `references/troubleshooting.md` | An export fails, vision rejects a PNG, or a rendering looks wrong |
| `assets/templates/<platform>-*.drawio` | A platform/tech stack was identified and a platform-specific starter template exists for the requested diagram type |
| `styles/<platform>.json` | A platform/tech stack was identified and a platform baseline style exists |
| `scripts/repair_png.py` | After every `-e` PNG export — fixes draw.io's truncated IEND chunk (issue #8) |
| `scripts/encode_drawio_url.py` | The CLI is unavailable and you need a browser-fallback diagrams.net URL |

### Platform-first resource resolution

Always resolve platform/tech stack first, then load resources in this order:

1. Platform-specific file (prefix = normalized platform/stack, lowercase)
2. Existing unprefixed generic file (fallback)

Apply this rule across all resource types:

- Templates: `assets/templates/<platform>-*.drawio` -> generic generation without template
- References: `references/<platform>-*.md` -> matching unprefixed `references/*.md`
- Styles: `styles/<platform>.json` -> existing preset/default behavior

Do not fail generation only because a platform-specific file is missing; continue with unprefixed defaults.

## Prerequisites

The draw.io desktop app must be installed and the CLI accessible:

**macOS sandbox / sandbox isolation note (e.g., codex.app):** In some sandboxed macOS environments, invoking the draw.io desktop CLI (even `draw.io --version`) can crash the draw.io process or produce no output. If that happens, treat the CLI as **unavailable in this sandbox isolation** — do not keep retrying inside the sandbox. Prefer a **non-sandboxed host environment** (outside sandbox isolation) for any CLI export work, or use the browser fallback / XML-only outputs.

```bash
# macOS (Homebrew — recommended; CLI binary is `drawio`, not `draw.io`)
brew install --cask drawio
drawio --version

# macOS (full path if not in PATH)
/Applications/draw.io.app/Contents/MacOS/draw.io --version

# Windows
"C:\Program Files\draw.io\draw.io.exe" --version

# Linux
draw.io --version
```

Install draw.io desktop if missing:
- macOS: `brew install --cask drawio` or download from https://github.com/jgraph/drawio-desktop/releases
- Windows: download installer from https://github.com/jgraph/drawio-desktop/releases
- Linux: download `.deb`/`.rpm` from https://github.com/jgraph/drawio-desktop/releases — **do not use snap** (AppArmor sandbox denies secrets/keyring on servers, causes crash)

## Workflow

Before starting the workflow, assess whether the user's request is specific enough. If key details are missing, ask 1-3 focused questions:
- **Diagram type** — which preset? (ERD, UML, Sequence, Architecture, ML/DL, Flowchart, or general)
- **Platform/tech stack** — AWS, Azure, Google Cloud, Salesforce, SAP, Adobe, Oracle, Kubernetes, etc. (if not already clear)
- **Output format** — Draw.io (default), PNG, SVG, PDF, or JPG. Use Mermaid only if explicitly requested.
- **Output location** — default is the user's working dir; honor any explicit path the user gives (e.g. "put it in `./artifacts/`"). Don't ask if they didn't mention one.
- **Scope/fidelity** — how many components? Any specific technologies or labels?

Skip clarification if the request already specifies these details or is clearly simple (e.g., "draw a flowchart of X"). Identify technology stack and domain to anticipate relevant shapes and style conventions (e.g., AWS/Azure/Google icons for cloud architecture, Salesforce/SAP/Adobe standards for diagramming, cylinders for databases, diamonds for decision points). Ask user for clarification if the request is vague and could lead to multiple interpretations.

**Step 0 — Resolve platform/stack resources.** Determine platform/tech stack first, then resolve matching templates/references/styles.

- Infer platform/stack from explicit user text first (for example: `salesforce`, `aws`, `azure`, `gcp`, `google cloud`, `oracle`, `sap`, `adobe`, `kubernetes`, `snowflake`).
- Normalize to lowercase slug for filenames (for example `Google Cloud` -> `google-cloud`).
- Use platform-prefixed files first, then fallback to existing unprefixed files when no platform-specific file exists.

Resource lookup rules:

1. **Diagram type reference**
  - Preferred: `references/<platform>-diagram-types.md`
  - Fallback: `references/diagram-types.md`
2. **Shape/style reference docs**
  - Preferred: relevant `references/<platform>-*.md` files for the requested diagram family
  - Fallback: existing unprefixed references already used by the skill
3. **Starter template**
  - Preferred: `assets/templates/<platform>-<diagram_type>.drawio` (or closest `<platform>-*.drawio` match)
  - Fallback: generate from scratch using the selected reference rules
4. **Platform baseline style**
  - Preferred: `styles/<platform>.json`
  - Fallback: no platform baseline style; continue with normal preset/default style path

If multiple platform candidates are plausible, ask one concise clarification question before generation.

**Step 0.5 — Resolve active preset.** Determine which (if any) user-defined style preset applies to this generation.

- Scan the user's message for a phrase that clearly names a style preset: "use my `<name>` style", "with my `<name>` style", "in `<name>` mode", "in the style of `<name>`". A bare `with <name>` does **not** count — "draw a diagram with redis" names a component, not a style. If a clear match is found → active preset = `<name>`.
- Else, check `~/.drawio-skill/styles/` for any file with `"default": true`. If found → active preset = that one.
- Else → no preset active; fall through to platform baseline style if available, otherwise built-in color/shape/edge conventions for the rest of the workflow.

Load the preset JSON from `~/.drawio-skill/styles/<name>.json`, falling back to `<this-skill-dir>/styles/built-in/<name>.json`. If the named preset exists in neither location, tell the user the name is unknown, list the available presets (user dir + built-in), and stop — do **not** silently fall back to defaults.

When both a platform baseline style (`styles/<platform>.json`) and an active preset are present:

- Apply platform baseline first.
- Apply active preset second (active preset wins on conflicts).
- Keep diagram-type structural keywords authoritative.

When a preset loads successfully, mention it in the first line of the reply: *"Using preset `<name>` (confidence: `<level>`)."* See the **Applying a preset** subsection below for how the preset changes color/shape/edge/font decisions.

**Step 0.6 — Salesforce base template and quality profile.** Apply this step when platform is Salesforce.

- Read and apply:
  - `assets/templates/salesforce-blank.drawio` (mandatory starting point for all Salesforce diagram types)
  - Diagram-type shapes reference:
    - `references/salesforce-data-model_shapes.md` for ERD/data model diagrams
    - `references/salesforce-architecture_shapes.md` for architecture/integration/capability diagrams (or closest Salesforce diagram-type specific reference)
  - `references/salesforce-first-pass-checklist.md`
- Treat the checklist as a blocking quality gate before showing first draft to user.
- If any checklist item fails, auto-fix in XML before export/review.
- Add a hard gate before export/review: confirm the working file is a copy of `salesforce-blank.drawio` and all non-header content is placed below the header area.
- Add a hard gate before export/review: confirm the legend/key section describes used elements, icon meanings, and connector styles.
- If either gate fails, stop and repair before any export.

1. **Check deps** — verify `draw.io --version` succeeds; note platform for correct CLI path
2. **Plan** — identify shapes, relationships, layout (LR or TB), group by tier/layer, and choose platform-specific references/templates when available
3. **Generate** — write `.drawio` XML file to disk, seeding from a platform-specific template when available; otherwise generate from scratch. Default output dir is the user's working dir; if the user specified an output path or directory (e.g. `./artifacts/`, `docs/images/`), use that instead — `mkdir -p` the target dir first. Apply the same dir choice to PNG/SVG/PDF exports in steps 4 and 7.
  - For all Salesforce diagram types: first copy `assets/templates/salesforce-blank.drawio` to the target output file and then modify that copy.
  - Place all generated nodes, groups, and connectors below the template header area.
  - For Salesforce architecture: enforce template-first card/group structure and evidence-gated icon selection before draft export.
  - For Salesforce ERD/data model: apply object/relationship content on the copied `salesforce-blank.drawio` file.
  - For Salesforce integration/security/capability diagrams: also start from `salesforce-blank.drawio`; do not switch to another Salesforce starter unless the user explicitly requests it.
4. **Export draft** — run CLI to produce a preview PNG. **Do NOT pass `-e`** at this step — the embedded `zTXt mxGraphModel` chunk it adds causes vision APIs (Claude included) to return 400 "Could not process image" in step 5. Save the clean preview as `<name>.png` (single extension). Embedding is for the final export only (step 7).
5. **Self-check** — use the agent's built-in vision capability to read the exported PNG, catch obvious issues, auto-fix before showing user (requires a vision-enabled model such as Claude Sonnet/Opus). If reading the PNG returns a 400 / "Could not process image" error, you almost certainly exported with `-e` by mistake — re-export without `-e` and retry once. If it still fails, skip self-check and continue to step 6.
6. **Review loop** — show image to user, collect feedback, apply targeted XML edits, re-export, repeat until approved
7. **Final export** — re-export the approved version to all requested formats. Use `-e` here (PNG/SVG/PDF) so the deliverable stays editable in draw.io; save as `<name>.drawio.png` to signal embedded XML. **For PNG with `-e`, run `python3 <this-skill-dir>/scripts/repair_png.py <name>.drawio.png` immediately after** — draw.io's CLI truncates the IEND chunk in `-e` PNG output (8 bytes missing), producing a corrupt file that vision APIs and strict PNG decoders reject (issue #8). Report file paths.

**If `draw.io --version` crashes or prints nothing (common in restricted macOS sandbox isolation like codex.app):**
- Do not keep retrying CLI invocations inside the sandbox.
- Skip steps 4, 5, 6, and 7 (CLI export + PNG-based review) and use **Browser fallback** (`scripts/encode_drawio_url.py`) or deliver the `.drawio` XML only.
- If the user needs PNG/SVG/PDF outputs, ask them to run the export commands in a **non-sandboxed host environment** (outside sandbox isolation) and share the resulting files.

Escalation rule:
- If the binary exists on PATH (or known app path exists) but execution fails with abnormal exit, empty output, Electron startup failure, display/session error, or likely sandbox restriction, prefer one escalated retry before falling back.
- If the binary is missing entirely, do not escalate just to search more aggressively; go to install guidance or fallback.

### Step 5: Self-Check

After exporting the draft PNG, use the agent's vision capability (e.g., Claude's image input) to read the image and check for these issues before showing the user. If the agent does not support vision, skip self-check and show the PNG directly.

**Important:** the draft PNG read here must have been exported **without** `-e`. Draw.io's `-e` flag emits a PNG with a truncated IEND chunk (8 bytes of type+CRC missing) that the Anthropic vision API rejects with 400 "Could not process image" (issue #8). The simplest fix for the preview step is to skip `-e` entirely; the final export in step 7 keeps `-e` and runs the repair snippet. If you see the 400 error here, re-export without `-e` and retry once; if it still fails (any other reason), skip self-check and proceed to step 6.

| Check | What to look for | Auto-fix action |
|-------|-----------------|-----------------|
| Overlapping shapes | Two or more shapes stacked on top of each other | Shift shapes apart by ≥200px |
| Clipped labels | Text cut off at shape boundaries | Increase shape width/height to fit label |
| Missing connections | Arrows that don't visually connect to shapes | Verify `source`/`target` ids match existing cells |
| Off-canvas shapes | Shapes at negative coordinates or far from the main group | Move to positive coordinates near the cluster |
| Edge-shape overlap | An edge/arrow visually crosses through an unrelated shape | Add waypoints (`<Array as="points">`) to route around the shape, or increase spacing between shapes |
| Stacked edges | Multiple edges overlap each other on the same path | Distribute entry/exit points across the shape perimeter (use different exitX/entryX values) |

- Max **2 self-check rounds** — if issues remain after 2 fixes, show the user anyway
- Re-export after each fix and re-read the new PNG

### Step 6: Review Loop

After self-check, show the exported image and ask the user for feedback.

**Targeted edit rules** — for each type of feedback, apply the minimal XML change:

| User request | XML edit action |
|-------------|----------------|
| Change color of X | Find `mxCell` by `value` matching X, update `fillColor`/`strokeColor` in `style` |
| Add a new node | Append a new `mxCell` vertex with next available `id`, position near related nodes |
| Remove a node | Delete the `mxCell` vertex and any edges with matching `source`/`target` |
| Move shape X | Update `x`/`y` in the `mxGeometry` of the matching `mxCell` |
| Resize shape X | Update `width`/`height` in the `mxGeometry` of the matching `mxCell` |
| Add arrow from A to B | Append a new `mxCell` edge with `source`/`target` matching A and B ids |
| Change label text | Update the `value` attribute of the matching `mxCell` |
| Change layout direction | **Full regeneration** — rebuild XML with new orientation |

**Rules:**
- For single-element changes: edit existing XML in place — preserves layout tuning from prior iterations
- For layout-wide changes (e.g., swap LR↔TB, "start over"): regenerate full XML
- Overwrite the same `{name}.png` (no `-e`) each iteration — do not create `v1`, `v2`, `v3` files. `-e` is reserved for the final export in step 7.
- After applying edits, re-export and show the updated image
- Loop continues until user says approved / done / LGTM
- **Safety valve:** after 5 iteration rounds, suggest the user open the `.drawio` file in draw.io desktop for fine-grained adjustments

### Step 7: Final Export

Once the user approves:
- Verify the legend/key section is complete and includes:
  - element descriptions
  - icon descriptions
  - connector style descriptions
- Export to all requested formats (PNG, SVG, PDF, JPG) — default to PNG if not specified
- Report file paths for both the `.drawio` source file and exported image(s)
- **Auto-launch:** offer to open the `.drawio` file in draw.io desktop for fine-tuning — `open diagram.drawio` (macOS), `xdg-open` (Linux), `start` (Windows)
- Confirm files are saved and ready to use

## Style Presets

A **style preset** is a named JSON file capturing a user's visual preferences (palette, shapes, font, edges). When active, it fully replaces the built-in color/shape conventions in this skill.

**Lookup order** when SKILL.md's step 0.5 resolves a preset name:
1. `~/.drawio-skill/styles/<name>.json` — user presets (survive `git pull`)
2. `<this-skill-dir>/styles/built-in/<name>.json` — shipped built-ins (`default`, `corporate`, `handdrawn`)

Platform baseline style lookup (from step 0) is separate:
1. `<this-skill-dir>/styles/<platform>.json`
2. none (fallback to normal preset/default behavior)

Always lowercase the user-provided name before any file operation — the schema enforces lowercase.

**For everything else — Learn flow (extracting a preset from a file), management ops (list/default/delete/rename), application rules (color lookup, shape keywords, edges, fonts, extras, interaction with diagram-type presets), and validation — read `references/style-presets.md`.** It's only needed when the user invokes those flows or when an active preset must be applied to the current generation.

## Draw.io XML Structure

### File skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- user shapes start at id="2" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Rules:**
- `id="0"` and `id="1"` are required root cells — never omit them
- User shapes start at `id="2"` and increment sequentially
- All shapes have `parent="1"` (unless inside a container — then use container's id)
- All text uses `html=1` in style for proper rendering
- **Never use `--` inside XML comments** — it's illegal per XML spec and causes parse errors
- Escape special characters in attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`
- **Multi-line text in labels:** use `&#xa;` for line breaks inside `value` attributes (not literal `\n`). Example: `value="Line 1&#xa;Line 2"`

### Shape types (vertex)

| Style keyword | Use for |
|--------------|---------|
| `rounded=0` | plain rectangle (default) |
| `rounded=1` | rounded rectangle — services, modules |
| `ellipse;` | circles/ovals — start/end, databases |
| `rhombus;` | diamond — decision points |
| `shape=mxgraph.aws4.resourceIcon;` | AWS icons |
| `shape=cylinder3;` | cylinder — databases |
| `swimlane;` | group/container with title bar |

### Required properties

```xml
<!-- Rectangle / rounded box -->
<mxCell id="2" value="Label" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>

<!-- Cylinder (database) -->
<mxCell id="3" value="DB" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
  <mxGeometry x="350" y="100" width="120" height="80" as="geometry" />
</mxCell>

<!-- Diamond (decision) -->
<mxCell id="4" value="Check?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
  <mxGeometry x="100" y="220" width="160" height="80" as="geometry" />
</mxCell>
```

### Containers and groups

For architecture diagrams with nested elements, use draw.io's parent-child containment — do **not** just place shapes on top of larger shapes.

| Type | Style | When to use |
|------|-------|-------------|
| **Group** (invisible) | `group;pointerEvents=0;` | No visual border needed, container has no connections |
| **Swimlane** (titled) | `swimlane;startSize=30;` | Container needs a visible title bar, or container itself has connections |
| **Custom container** | Add `container=1;pointerEvents=0;` to any shape | Any shape acting as a container without its own connections |

**Key rules:**
- Add `pointerEvents=0;` to container styles that should not capture connections between children
- Children set `parent="containerId"` and use coordinates **relative to the container**

```xml
<!-- Swimlane container -->
<mxCell id="svc1" value="User Service" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
<!-- Child inside container — coordinates relative to parent -->
<mxCell id="api1" value="REST API" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="db1" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="160" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

### Connector (edge)

**CRITICAL:** Every edge `mxCell` must contain a `<mxGeometry relative="1" as="geometry" />` child element. Self-closing edge cells (`<mxCell ... edge="1" ... />`) are **invalid** and will not render. Always use the expanded form.

```xml
<!-- Directed arrow — always include rounded, orthogonalLoop, jettySize for clean routing -->
<mxCell id="10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Arrow with label + explicit entry/exit points to control direction -->
<mxCell id="11" value="HTTP/REST" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="4">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Arrow with waypoints — use when edge must route around other shapes -->
<mxCell id="12" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="3" target="5">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="500" y="50" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Edge style rules:**
- **Animated connectors:** add `flowAnimation=1;` to any edge style to show a moving dot animation along the arrow. Works in SVG export and draw.io desktop — ideal for data-flow and pipeline diagrams. Example: `style="edgeStyle=orthogonalEdgeStyle;flowAnimation=1;rounded=1;..."`
- **Always** include `rounded=1;orthogonalLoop=1;jettySize=auto` — these enable smart routing that avoids overlaps
- Pin `exitX/exitY/entryX/entryY` on every edge when a node has 2+ connections — distributes lines across the shape perimeter
- Add `<Array as="points">` waypoints when an edge must detour around an intermediate shape
- **Leave room for arrowheads:** the final straight segment between the last bend and the target shape must be ≥20px long. If too short, the arrowhead overlaps the bend and looks broken. Fix by increasing node spacing or adding explicit waypoints

### Distributing connections on a shape

When multiple edges connect to the same shape, assign different entry/exit points to prevent stacking:

| Position | exitX/entryX | exitY/entryY | Use when |
|----------|-------------|-------------|----------|
| Top center | 0.5 | 0 | connecting to node above |
| Top-left | 0.25 | 0 | 2nd connection from top |
| Top-right | 0.75 | 0 | 3rd connection from top |
| Right center | 1 | 0.5 | connecting to node on right |
| Bottom center | 0.5 | 1 | connecting to node below |
| Left center | 0 | 0.5 | connecting to node on left |

**Rule:** if a shape has N connections on one side, space them evenly (e.g., 3 connections on bottom → exitX = 0.25, 0.5, 0.75)

### Color palette (fillColor / strokeColor)

*Used only when no preset is active (see "Applying a preset" above).*

| Color name | fillColor | strokeColor | Use for |
|-----------|-----------|-------------|---------|
| Blue | `#dae8fc` | `#6c8ebf` | services, clients |
| Green | `#d5e8d4` | `#82b366` | success, databases |
| Yellow | `#fff2cc` | `#d6b656` | queues, decisions |
| Orange | `#ffe6cc` | `#d79b00` | gateways, APIs |
| Red/Pink | `#f8cecc` | `#b85450` | errors, alerts |
| Grey | `#f5f5f5` | `#666666` | external/neutral |
| Purple | `#e1d5e7` | `#9673a6` | security, auth |

### Layout tips

**Spacing — scale with complexity:**

| Diagram complexity | Nodes | Horizontal gap | Vertical gap |
|-------------------|-------|----------------|--------------|
| Simple | ≤5 | 200px | 150px |
| Medium | 6–10 | 280px | 200px |
| Complex | >10 | 350px | 250px |

**Routing corridors:** between shape rows/columns, leave an extra ~80px empty corridor where edges can route without crossing shapes. Never place a shape in a gap that edges need to traverse.

**Grid alignment:** snap all `x`, `y`, `width`, `height` values to **multiples of 10** — this ensures shapes align cleanly on draw.io's default grid and makes manual editing easier.

**General rules:**
- Plan a grid before assigning x/y coordinates — sketch node positions on paper/mentally first
- Group related nodes in the same horizontal or vertical band
- Use `swimlane` cells for logical grouping with visible borders
- Place heavily-connected "hub" nodes centrally so edges radiate outward instead of crossing
- To force straight vertical connections, pin entry/exit points explicitly on edges:
  `exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0`
- Always center-align a child node under its parent (same center x) to avoid diagonal routing
- **Event bus pattern**: place Kafka/bus nodes in the **center of the service row**, not below — services on either side can reach it with short horizontal arrows (`exitX=1` left side, `exitX=0` right side), eliminating all line crossings
- Horizontal connections (`exitX=1` or `exitX=0`) never cross vertical nodes in the same row; use them for peer-to-peer and publish connections

**Avoiding edge-shape overlap:**
- Before finalizing coordinates, trace each edge path mentally — if it must cross an unrelated shape, either move the shape or add waypoints
- For tree/hierarchical layouts: assign nodes to layers (rows), connect only between adjacent layers to minimize crossings
- For star/hub layouts: place the hub center, satellites around it — edges stay short and radial
- When an edge must span multiple rows/columns, route it along the outer corridor, not through the middle of the diagram

## Export

### Commands

There are **two** export modes:

- **Preview / self-check** (step 4 of the workflow) — no `-e`. Output `diagram.png`. Required for vision self-check; using `-e` here triggers a 400 "Could not process image" error from the vision API (issue #8).
- **Final / deliverable** (step 7) — pass `-e`. Output `diagram.drawio.png`. The embedded XML keeps the file editable in draw.io.

```bash
# Preview PNG (use this in step 4, before self-check) — NO -e
draw.io -x -f png -s 2 -o diagram.png input.drawio

# Final PNG (step 7, after user approval) — WITH -e, double extension
draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# macOS — full path (if not in PATH); preview / final variants
/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -s 2 -o diagram.png input.drawio
/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# Windows
"C:\Program Files\draw.io\draw.io.exe" -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# Linux (headless — requires xvfb-run; on servers add HOME and --disable-gpu)
export HOME=${HOME:-/tmp}
xvfb-run -a --server-args="-screen 0 1280x1024x24" \
  draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio --disable-gpu
# Running as root (CI / Docker)? Append --no-sandbox AT THE END (placing it earlier makes drawio treat it as the input filename)

# SVG export (final — -e is safe; SVG is text)
draw.io -x -f svg -e -o diagram.svg input.drawio

# PDF export (final)
draw.io -x -f pdf -e -o diagram.pdf input.drawio

# Custom output directory (e.g. CI artifacts dir) — create if missing, then export there
mkdir -p ./artifacts && draw.io -x -f png -e -s 2 -o ./artifacts/diagram.drawio.png input.drawio
```

### Post-export PNG repair (required after `-e` PNG export)

draw.io CLI truncates the IEND chunk when emitting `-e` PNGs — the file ends with the 4-byte IEND length field but the `IEND` type + CRC (8 bytes) are missing. Result: vision APIs return 400 "Could not process image" and strict PNG decoders error out. SVG/PDF are unaffected.

Run this immediately after every `-e` PNG export:

```bash
python3 <this-skill-dir>/scripts/repair_png.py diagram.drawio.png
```

The script's `endswith(IEND)` guard makes it a no-op once draw.io fixes the bug upstream — safe to run unconditionally.

**Key flags:**
- `-x` — export mode (required)
- `-f` — format: `png`, `svg`, `pdf`, `jpg`
- `-e` — embed diagram XML in output (PNG, SVG, PDF) — exported file remains editable in draw.io. **Skip for the preview PNG used in step 5 self-check** — `-e` PNGs have a truncated IEND chunk that vision APIs reject (issue #8). For final PNG export, keep `-e` and run `scripts/repair_png.py` (see Post-export PNG repair). SVG/PDF unaffected.
- `-s` — scale: `1`, `2`, `3` (2 recommended for PNG)
- `-o` — output file path; accepts any directory (e.g. `./artifacts/diagram.drawio.png`) — `mkdir -p` the target dir first. Use `.drawio.png` double extension when embedding.
- `-b` — border width around diagram (default: 0, recommend 10)
- `-t` — transparent background (PNG only)
- `--page-index 0` — export specific page (default: all)

### Browser fallback (no CLI needed)

When the draw.io desktop CLI is unavailable, generate a client-side viewer URL:

```bash
python3 <this-skill-dir>/scripts/encode_drawio_url.py input.drawio
```

Prints a `https://viewer.diagrams.net/...` URL with the diagram XML deflate-compressed and base64-encoded into the URL fragment. The fragment (after `#`) is never sent to the server, so nothing is uploaded — the diagram opens client-side for viewing and editing. Useful when the user cannot install the desktop app.

### Fallback chain

When tools are unavailable, degrade gracefully:

| Scenario | Behavior |
|----------|----------|
| draw.io CLI missing, Python available | Use browser fallback (diagrams.net URL) |
| draw.io CLI missing, Python missing | Generate `.drawio` XML only; instruct user to open in draw.io desktop or diagrams.net manually |
| draw.io CLI crashes / no output in macOS sandbox isolation | Treat CLI as unavailable in-sandbox; use browser fallback / XML-only; ask user to run CLI exports in a non-sandboxed host environment |
| Vision unavailable for self-check | Skip self-check (step 5); proceed directly to showing user the exported PNG |
| Export fails (Chromium/display issues) | On Linux, retry with `xvfb-run -a`; if still failing, deliver `.drawio` XML and suggest manual export |
| Export fails on Linux server (headless) | Try in order: (1) `xvfb-run -a`, (2) append `--no-sandbox` at the very end if root, (3) add `--disable-gpu`, (4) `export HOME=/tmp`, (5) install apt deps (`libgtk-3-0 libnotify4 libnss3 libgbm1 libasound2t64` etc.), (6) fall back to [tomkludy/drawio-renderer](https://hub.docker.com/r/tomkludy/drawio-renderer) Docker (REST API for headless export) |

### Checking if draw.io is in PATH

```bash
# Try short command first
if command -v draw.io &>/dev/null; then
  DRAWIO="draw.io"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
else
  echo "draw.io not found — install from https://github.com/jgraph/drawio-desktop/releases"
fi
```

## Common Mistakes

When something looks wrong (export fails, vision rejects a PNG, layout broken, edges misroute), see `references/troubleshooting.md` for a row-by-row mistake → fix table.

## Diagram Type Presets

When the user requests a specific diagram type, first try platform-specific mapping, then fallback to generic:

1. `references/<platform>-diagram-types.md` (if platform/stack was resolved and file exists)
2. `references/diagram-types.md` (fallback)

Pick by user phrasing:

| User says | Section in `references/diagram-types.md` |
|---|---|
| "ER diagram", "schema diagram", "data model" | ERD |
| "UML class diagram", "class diagram" | UML Class |
| "sequence diagram", "interaction diagram", "lifeline" | Sequence |
| "architecture", "system diagram", "service diagram" | Architecture |
| "neural network", "model architecture", "ML diagram", "deep learning" | ML / Deep Learning Model |
| "flowchart", "decision tree", "process flow" | Flowchart |

The diagram-type preset sets **structural** style keywords. If a user style preset is also active (see `## Style Presets`), keep the structural keywords and layer color/font/edge/extras on top — read `references/style-presets.md` → "Interaction with diagram-type presets" for the merge rules.
