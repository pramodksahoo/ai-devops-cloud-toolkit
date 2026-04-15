# Kubernetes

This directory contains the live Kubernetes runtime path for the MVP.

- `base/` is the composition layer that consumes workload-owned assets
- `overlays/local-kind/` is the canonical local overlay and stable script entrypoint

Ownership boundary:

- keep workload-specific manifests and content under `platform/workloads/demo-app/`
- keep overlay wiring and environment-specific composition under `platform/kubernetes/`
- keep namespace and baseline RBAC creation in Terraform

The namespace is intentionally created by Terraform in the live path.
