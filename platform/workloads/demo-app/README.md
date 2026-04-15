# Demo App

The live demo workload is a deliberately small NGINX-based application that serves a static page.

It is simple on purpose:
- fast to pull and run on `kind`
- easy to verify with a port-forward
- easy to extend for workshops or examples

## Ownership boundary

`platform/workloads/demo-app/` is the single source of truth for workload-specific runtime assets:

- `manifests/index.html` owns the demo page content
- `manifests/` owns the `demo-app` Deployment, Service, and ConfigMap generation

`platform/kubernetes/` stays responsible for deployment composition and overlays:

- `platform/kubernetes/base/` composes workload-owned manifests into the live runtime path
- `platform/kubernetes/overlays/local-kind/` remains the canonical local-kind entrypoint used by `./scripts/demo-up.sh`

## Safe ways to extend the demo

- edit `manifests/index.html` when changing demo page content
- edit `manifests/deployment.yaml` or `manifests/service.yaml` when changing workload runtime behavior
- avoid reintroducing workload-specific manifest copies under `platform/kubernetes/base/`
