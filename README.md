# salesforce-architect-skills

Repository for Salesforce-focused Copilot skills and supporting evaluation assets.

## Repository structure

```
skills/
  salesforce-diagram/
    SKILL.md
    README.md
    assets/
    evals/
    references/
    scripts/
    styles/
  salesforce-org-shape-analysis/
    SKILL.md

plugins/
  ai-architect-core/

artifacts/
  evaluation/
```

## Included skills

- `salesforce-diagram`: Generates Salesforce and general Draw.io diagrams with Salesforce-specific templates and references.
- `salesforce-org-shape-analysis`: Produces Salesforce org analysis artifacts used to ground diagram generation.

Skill manifests in this repository:

- `skills/salesforce-diagram/SKILL.md`
- `skills/salesforce-org-shape-analysis/SKILL.md`

## Skills installation (Salesforce CLI)

Pre-requisite: Salesforce CLI is installed.

1. Install the `sf-aidev` plugin for Salesforce CLI:

```bash
sf plugins install sf-aidev
```

2. For a project without AI configuration, initialize from this repository:

```bash
sf aidev init --source yurybond/salesforce-architect-skills --tool copilot
```

## Skill evaluation (salesforce-diagram)

### Where to edit evals and assertions

- Evals: `skills/salesforce-diagram/evals/evals.json`
- Per-eval metadata/assertions: `skills/salesforce-diagram/evals/metadata/`

Quick validation:

```bash
jq . skills/salesforce-diagram/evals/evals.json >/dev/null
for f in skills/salesforce-diagram/evals/metadata/*.json; do jq . "$f" >/dev/null; done
```

### Core evaluation commands

Create grading stubs from eval expectations (for run folders like `eval-01/with_skill`, `without_skill`, `old_skill`):

```bash
python3 skills/salesforce-diagram/scripts/generate_grading_stubs.py /path/to/iteration-1 --dry-run
python3 skills/salesforce-diagram/scripts/generate_grading_stubs.py /path/to/iteration-1
```

Recompute `grading.json` summary fields after grading:

```bash
python3 skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1 --dry-run
python3 skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1
python3 skills/salesforce-diagram/scripts/update_grading_summary.py /path/to/iteration-1 --check
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

## Notes

- `SKILL.md` is required and case-sensitive.
- Skill `name` should be lowercase kebab-case.
- Keep the skill directory name aligned with the skill `name`.
- `plugins/ai-architect-core/` currently exists as a folder, but no plugin manifest is checked in yet.