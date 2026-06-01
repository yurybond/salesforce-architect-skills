# Eval Metadata Pack

This folder contains assertion-ready metadata files for each eval in `evals/evals.json`.

## File naming

- `eval-01-...json` through `eval-12-...json`

## JSON shape

Each file contains:

- `eval_id`
- `eval_name`
- `prompt`
- `assertions` (grader-ready checklist statements)
- `focus_tags`

## Intended use

- Use `assertions` as the source for expectations in per-run grading.
- Keep prompts in sync with `evals/evals.json` when editing.
- If you add a new eval, add a matching metadata file here.
