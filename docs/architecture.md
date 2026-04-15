# Architecture

## MVP architecture in one view

The toolkit deliberately separates concerns:

1. **Terraform foundation**
   - creates the live demo namespace and baseline RBAC/service account resources
   - gives Terraform a real role in the MVP without introducing cloud-account friction

2. **Kubernetes deployment layer**
   - deploys the demo workload into the Terraform-created namespace
   - keeps app deployment and infrastructure foundation visibly separate

3. **Scripts and workflow contract**
   - `bootstrap.sh` verifies the local environment
   - `validate.sh` aggregates checks
   - `demo-up.sh` applies the canonical path
   - `demo-verify.sh` proves the app is healthy
   - `demo-down.sh` resets the environment

4. **GitHub Actions**
   - validates the repository structure and quality gates in CI
   - provides a demo-smoke lane for local-kind style verification

5. **AI-friendly guidance**
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

Kubernetes manifests own runtime deployment concerns:
- app deployment
- service exposure
- overlays for local-kind

This makes it easy for contributors to extend app/runtime behavior without blurring infrastructure and workload responsibilities.

## Directory intent

| Directory | Intent |
|---|---|
| `platform/terraform/` | Live demo foundation |
| `platform/kubernetes/` | Live runtime deployment path |
| `platform/workloads/` | Demo app assets and workload notes |
| `platform/policies/` | Baseline policy/security placeholders |
| `examples/` | Example-only extensions |
| `docs/examples/` | Example-only guidance |
| `prompts/` | AI task prompts scoped to repo conventions |

## Design constraints

- one obvious path must remain easy to follow
- live assets stay separate from example-only assets
- provider-specific depth stays out of the canonical path
- anything that threatens the one-hour experience should move out of live v1
