# Architecture

## MVP architecture in one view

The toolkit deliberately separates concerns:

1. **Terraform foundation**
   - creates the live demo namespace and baseline RBAC/service account resources
   - gives Terraform a real role in the MVP without introducing cloud-account friction

2. **Kubernetes deployment layer**
   - composes workload-owned manifests into the Terraform-created namespace
   - keeps runtime deployment assembly separate from workload ownership

3. **Workload runtime assets**
   - `platform/workloads/demo-app/` owns the demo page content and workload manifest source
   - keeps workload-specific changes close to the workload instead of scattering them across shared deployment folders

4. **Scripts and workflow contract**
   - `bootstrap.sh` verifies the local environment
   - `validate.sh` aggregates checks
   - `demo-up.sh` applies the canonical path
   - `demo-verify.sh` proves the app is healthy
   - `demo-down.sh` resets the environment

5. **GitHub Actions**
   - validates the repository structure and quality gates in CI
   - provides a demo-smoke lane for local-kind style verification

6. **AI-friendly guidance**
   - `AGENTS.md` defines safe repo-level guidance
   - `prompts/` gives models repo-specific tasks and boundaries
   - docs explain what AI may safely change in v1

## Why Terraform is in the live path

Terraform is not a token directory in this repo.

In the canonical story it manages a lightweight **demo foundation**:
- namespace bootstrap
- service account creation
- minimal RBAC

That keeps the toolkit credible as a platform starter while still remaining local-first and cloud-agnostic.

## Why Kubernetes stays separate

Kubernetes owns deployment composition concerns:
- reusable composition in `platform/kubernetes/base/`
- overlays for local-kind
- environment wiring around workload-owned manifests

This makes it easy for contributors to extend app/runtime behavior without blurring infrastructure and workload responsibilities.

## Why workload assets live under `platform/workloads/`

The demo workload should be discoverable as a real workload, not just implied through Kubernetes base files.

`platform/workloads/demo-app/` therefore owns:
- demo content/config
- workload-specific Deployment and Service manifest source
- workload-specific extension notes

This keeps the ownership boundary clear:
- Terraform owns shared foundation
- Kubernetes owns deployment assembly
- workload directories own workload-specific runtime assets

## Directory intent

| Directory | Intent |
|---|---|
| `platform/terraform/` | Live demo foundation |
| `platform/kubernetes/` | Live deployment composition and overlays |
| `platform/workloads/` | Demo app runtime assets and workload notes |
| `platform/policies/` | Baseline policy/security placeholders |
| `examples/` | Example-only extensions |
| `docs/examples/` | Example-only guidance |
| `prompts/` | AI task prompts scoped to repo conventions |

## Design constraints

- one obvious path must remain easy to follow
- live assets stay separate from example-only assets
- provider-specific depth stays out of the canonical path
- anything that threatens the one-hour experience should move out of live v1
