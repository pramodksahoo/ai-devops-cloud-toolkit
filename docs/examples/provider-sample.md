# Provider-oriented sample (Example-only)

This page explains the neutral provider-oriented scaffold under [`examples/provider-sample/`](../../examples/provider-sample/README.md).

It is optional, illustrative, and intentionally outside the canonical local-first path.
Nothing here should be read as official support for AWS, Azure, GCP, or any other provider workflow.

## Why this exists

The repository stays strongest when it keeps one clear live MVP path while still giving contributors room to explore.
The provider sample establishes a reusable pattern for future examples without moving provider-specific material into the live demo path.

## Directory shape

```text
examples/provider-sample/
├── README.md
├── providers/
│   └── TEMPLATE.md
├── modules/
│   └── README.md
├── manifests/
│   └── README.md
└── docs/
    └── extension-notes.md
```

## How to extend it safely

1. Start with the boundary rules in [`prompts/add-example.md`](../../prompts/add-example.md).
2. Add provider-specific assumptions under `examples/provider-sample/providers/`.
3. Keep optional modules and manifests inside the sample tree instead of under `platform/`.
4. Document what is illustrative, incomplete, or contributor-owned.
5. Update this page when the example grows so readers can still tell what is optional.

## What must stay out of the live MVP path

- provider-specific changes under `platform/`
- edits that reframe the root quickstart as a provider path
- script changes that make provider material part of `bootstrap`, `validate`, `demo-up`, `demo-verify`, or `demo-down`
- wording that turns the example into an endorsed deployment target

## Anti-patterns

- adding a real cloud account dependency to the first-run experience
- copying provider-specific files into the canonical local-kind overlay
- leaving provider-specific assumptions undocumented
- mixing example-only guidance with live MVP instructions

## Contributor note

If you turn this scaffold into a concrete provider example later, keep the change easy to review:

- prefer small, clearly named additions
- keep documentation adjacent to the example
- preserve the root README and quickstart as the single recommended starting point
