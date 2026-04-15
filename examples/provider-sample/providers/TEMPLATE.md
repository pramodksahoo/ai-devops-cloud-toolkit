# Provider template

Use this file as a neutral starting point for a future provider-oriented example.

## What belongs here

- provider-specific assumptions and prerequisites
- overlay or module choices that are unique to that provider
- optional variables, manifests, or docs that stay outside the live MVP path

## Naming guidance

- prefer neutral placeholders such as `provider-a`, `provider-b`, or a contributor-owned provider name
- keep provider-specific files grouped under one directory so they are easy to review or remove
- describe what is illustrative versus what would need real implementation later

## What must stay out

- changes to `platform/`
- changes to the canonical quickstart or live demo scripts
- wording that suggests this repository officially supports a provider workflow
