# Terraform

Terraform is a live part of the canonical MVP path.

## Purpose in v1

The Terraform layer manages the **demo foundation** for the local platform path:
- namespace bootstrap
- service account creation
- minimal RBAC

It intentionally does **not** try to be a deep multi-cloud abstraction.

## Layout

- `modules/demo-foundation/` — reusable local platform foundation module
- `examples/local-demo/` — canonical local example used by the quickstart
