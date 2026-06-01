# ai-architect

AI customization repository that supports two distribution channels for GitHub Copilot:

1. Skills channel (direct skill install and usage)
2. Plugin marketplace channel (installable Copilot plugin bundles)

## Repository structure

```
skills/
  lucidchart-diagrams/
    SKILL.md

plugins/
  ai-architect-core/
    plugin.json

.github/
  plugin/
    marketplace.json
```

## Included manifests

- Skills manifest:
  - `skills/lucidchart-diagrams/SKILL.md`
- Plugin manifest:
  - `plugins/ai-architect-core/plugin.json`
- Marketplace manifest:
  - `.github/plugin/marketplace.json`

## Channel 1: Skills

Skill name: `lucidchart-diagrams`

Install with GitHub CLI skills tooling:

```bash
gh skill preview OWNER/REPO lucidchart-diagrams
gh skill install OWNER/REPO lucidchart-diagrams
```

Use in Copilot CLI:

```text
/skills list
/skills info lucidchart-diagrams
Use /lucidchart-diagrams to create a sequence diagram for checkout flow
```

Notes:

- `SKILL.md` is required and case-sensitive.
- Skill `name` must be lowercase kebab-case.
- Skill directory name should match the skill `name`.

## Channel 2: Plugin marketplace

Marketplace name: `ai-architect-marketplace`

Plugin name: `ai-architect-core`

Add marketplace and install plugin:

```bash
copilot plugin marketplace add OWNER/REPO
copilot plugin marketplace list
copilot plugin marketplace browse ai-architect-marketplace
copilot plugin install ai-architect-core@ai-architect-marketplace
```

Manage installed plugin:

```bash
copilot plugin list
copilot plugin update ai-architect-core
copilot plugin uninstall ai-architect-core
```

## Versioning and publishing checklist

When releasing updates:

1. Update plugin version in `plugins/ai-architect-core/plugin.json`.
2. Update matching plugin version in `.github/plugin/marketplace.json`.
3. Commit and push changes.
4. Consumers run `copilot plugin update ai-architect-core`.

For skills channel updates:

1. Update the skill in `skills/<skill-name>/SKILL.md`.
2. Publish/update via GitHub CLI skills workflow (`gh skill publish`, preview feature).

## Adding new skills

1. Create `skills/<new-skill-name>/SKILL.md`.
2. Use required YAML frontmatter fields:
   - `name`
   - `description`
3. Keep names kebab-case.
4. If the skill should ship in plugin installs, no extra mapping is needed as long as it is under `skills/` (the plugin manifest points to that directory).

## Skill evaluation (salesforce-diagram)

### Where to edit evals and assertions

- Evals: `.agents/skills/salesforce-diagram/evals/evals.json`
- Per-eval metadata/assertions: `.agents/skills/salesforce-diagram/evals/metadata/`

Quick validation:

```bash
jq . .agents/skills/salesforce-diagram/evals/evals.json >/dev/null
for f in .agents/skills/salesforce-diagram/evals/metadata/*.json; do jq . "$f" >/dev/null; done
```

### Core evaluation commands

Create grading stubs from eval expectations (for run folders like `eval-01/with_skill`, `without_skill`, `old_skill`):

```bash
python3 .agents/skills/salesforce-diagram/scripts/generate_grading_stubs.py /path/to/iteration-1 --dry-run
python3 .agents/skills/salesforce-diagram/scripts/generate_grading_stubs.py /path/to/iteration-1
```

Recompute `grading.json` summary fields after grading:

```bash
python3 .agents/skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1 --dry-run
python3 .agents/skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1
python3 .agents/skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1 --check
```

Aggregate benchmark (from skill-creator directory):

```bash
cd ~/.agents/skills/skill-creator
python -m scripts.aggregate_benchmark /path/to/iteration-1 --skill-name salesforce-diagram
```

### Where to see results

- Per-run grades: `/path/to/iteration-1/eval-*/<with_skill|without_skill|old_skill>/grading.json`
- Aggregated metrics: `/path/to/iteration-1/benchmark.json` and `/path/to/iteration-1/benchmark.md`

Open the evaluation viewer:

```bash
python ~/.agents/skills/skill-creator/eval-viewer/generate_review.py \
  /path/to/iteration-1 \
  --skill-name "salesforce-diagram" \
  --benchmark /path/to/iteration-1/benchmark.json
```

For iteration 2+, compare with previous run:

```bash
python ~/.agents/skills/skill-creator/eval-viewer/generate_review.py \
  /path/to/iteration-2 \
  --skill-name "salesforce-diagram" \
  --benchmark /path/to/iteration-2/benchmark.json \
  --previous-workspace /path/to/iteration-1
```

## References

- Add skills for Copilot CLI:
  - https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills
- Find/install plugins for Copilot CLI:
  - https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing
- Copilot CLI plugin/marketplace schema:
  - https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference

## Diagram Types

1. System Architecture Diagram
2. Sequence Diagram
3. C4 Context Diagram
4. Data Model Diagram
5. Product Map Diagram
6. Data Flow Diagram
7. Class Diagram
8. Component Diagram
9. Deployment Diagram