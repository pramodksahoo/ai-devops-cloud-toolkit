# Kubernetes

This directory contains the live Kubernetes runtime path for the MVP.

- `base/` composes workload-owned manifests into the live path
- `overlays/local-kind/` defines the canonical local overlay

The demo workload itself lives under `platform/workloads/demo-app/`.

The namespace is intentionally created by Terraform in the live path.
