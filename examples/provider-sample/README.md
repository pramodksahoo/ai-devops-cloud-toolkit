# Provider sample

This directory is an example-only scaffold for future provider-oriented examples.

It is intentionally neutral and does **not** represent official provider support.
The canonical local-first path still lives in the root quickstart and the scripts under `scripts/`.

## Suggested structure

```text
provider-sample/
├── README.md
├── docs/
│   └── extension-notes.md
├── manifests/
│   └── README.md
├── modules/
│   └── README.md
└── providers/
    └── TEMPLATE.md
```

## How to use this scaffold

- add provider-specific context under `providers/`
- keep optional example modules under `modules/`
- place illustrative manifests or overlays under `manifests/`
- capture contributor notes or caveats under `docs/`

## Guardrails

- keep everything here removable and example-only
- do not change `platform/`, the root quickstart, or the live demo scripts from this scaffold
- avoid naming or copy that implies this repository officially supports a cloud provider

For the canonical explanation page, see [`docs/examples/provider-sample.md`](../../docs/examples/provider-sample.md).
