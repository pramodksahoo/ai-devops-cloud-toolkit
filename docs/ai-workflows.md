# AI Workflows

This repository is intentionally structured to work well with AI models.

## Before using AI on this repo

Always give the model these sources first:
1. `AGENTS.md`
2. `README.md`
3. the relevant prompt under `prompts/`
4. the nearest docs page for the area you want to change

## What AI may safely do in v1

Safe extension classes:
1. duplicate or lightly adapt the demo workload overlay
2. add one small example under `examples/`
3. improve docs or validation guidance without changing the canonical runtime path

## What AI should not do by default

- move example-only content into the live path
- add provider-specific complexity to the canonical demo
- replace the Terraform role with app deployment logic
- introduce enterprise-scale abstractions into v1

## Suggested prompts

- Use `prompts/extend-toolkit.md` when adding a bounded feature or example
- Use `prompts/validate-change.md` when checking a diff against repo contracts
- Use `prompts/add-example.md` when adding example-only content

## Validation contract for AI changes

Every AI-generated change should preserve:
- the canonical path
- clear live/example/docs-only boundaries
- docs consistency
- validation entrypoints
