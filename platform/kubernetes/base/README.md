# Kubernetes Base Composition

`platform/kubernetes/base/` is the composition layer for the live MVP.

It does **not** own the `demo-app` workload manifests directly.

- `platform/workloads/demo-app/` owns workload-specific runtime assets and manifest source
- `platform/kubernetes/base/` composes workload manifests into the live Kubernetes path
- `platform/kubernetes/overlays/local-kind/` remains the canonical local deployment entrypoint
