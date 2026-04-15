# Architecture

## MVP architecture in one view

The toolkit deliberately separates concerns:

1. **Terraform foundation**
   - creates the live demo namespace and baseline RBAC/service account resources
   - gives Terraform a real role in the MVP without introducing cloud-account friction

2. **Workload asset layer**
   - keeps demo workload-specific manifests, config, and content under `platform/workloads/demo-app/`
   - makes the demo workload the clear source of truth for runtime-specific assets

3. **Kubernetes composition layer**
   - assembles the workload into the Terraform-created namespace
   - keeps `platform/kubernetes/overlays/local-kind/` as the canonical local deployment entrypoint
   - keeps app deployment assembly separate from workload ownership and Terraform foundation

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

## Workload ownership boundary

The approved follow-up lane keeps the user-facing flow stable:

```text
bootstrap -> validate -> demo-up -> demo-verify -> demo-down
```

Inside the repo, ownership becomes more explicit:

- `platform/workloads/demo-app/` owns workload-specific manifests, content, and workload notes
- `platform/kubernetes/` owns composition, shared labels/conventions, and overlays such as `local-kind`
- `platform/terraform/` owns shared foundation prerequisites that run before workload deployment

That split makes it easier to extend the demo workload without drifting workload logic back into generic deployment folders, and it keeps workload-specific runtime assets discoverable in the workload directory.

## Why Kubernetes stays separate

Kubernetes manifests still own deployment assembly concerns:
- composition of workload manifests into the live path
- service exposure and environment wiring
- overlays for local-kind

This makes it easy for contributors to extend app/runtime behavior without blurring workload, deployment, and infrastructure responsibilities.

## Directory intent

| Directory | Intent |
|---|---|
| `platform/terraform/` | Live demo foundation |
| `platform/kubernetes/` | Live deployment composition and overlays |
| `platform/workloads/` | Workload-owned manifests, content, and notes |
| `platform/policies/` | Baseline policy/security placeholders |
| `examples/` | Example-only extensions |
| `docs/examples/` | Example-only guidance |
| `prompts/` | AI task prompts scoped to repo conventions |

## Design constraints

- one obvious path must remain easy to follow
- live assets stay separate from example-only assets
- provider-specific depth stays out of the canonical path
- anything that threatens the one-hour experience should move out of live v1
