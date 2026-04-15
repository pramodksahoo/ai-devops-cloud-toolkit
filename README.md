# AI DevOps Cloud Toolkit

A practical, open-source **DevOps/cloud platform starter toolkit** built for the community and designed to work well with AI-assisted development workflows.

This MVP focuses on one strong, cloud-agnostic path:

> **clone -> bootstrap -> validate -> deploy to local Kubernetes -> verify -> extend safely with AI**

It brings together:

- **Terraform** starter foundations
- **Kubernetes** deployment templates
- **GitHub Actions** validation workflows
- **security and validation checks**
- **AGENTS.md + prompts** for AI-assisted contribution
- **clear docs and contributor onboarding**

---

## Why this repo exists

Today, contributors often have to stitch together Terraform, Kubernetes, CI/CD, validation, documentation, and AI guidance manually. That process is slow, fragmented, and difficult to extend safely.

This toolkit provides a clean starting point for building, demoing, and evolving a modern cloud/platform repository with clear guardrails and a contributor-friendly workflow.

It is designed to help people move faster from:

**idea -> working repo -> validated setup -> local demo -> safe extension with AI**

---

## Use cases

This toolkit is intended for practical, community-focused scenarios such as:

### 1. Open-source platform starter repo
Use this as a foundation for launching a new DevOps, cloud, or platform engineering project with sane structure, validation, deployment patterns, and contributor guidance already in place.

### 2. Workshops, hackathons, and community demos
Use the toolkit for hands-on sessions where participants need a fast, repeatable path to clone a repo, run checks, deploy a demo workload, and understand the platform flow without cloud account friction.

### 3. AI-assisted infrastructure and platform development
Use the repo to demonstrate how AI models can safely support DevOps and platform workflows through repo-specific prompts, contribution boundaries, AGENTS.md guidance, and validation-driven changes.

### 4. Starter internal platform repository
Use it as a lightweight starting point for an internal team that wants Terraform, Kubernetes, CI/CD, validation, and documentation conventions without having to build a full platform stack from scratch.

### 5. Contributor onboarding accelerator
Use the toolkit to help new contributors understand the repo quickly, run the canonical workflow, make safe changes, and extend the project without breaking the main demo path.

### 6. Safe experimentation sandbox
Use it as a controlled environment for trying small infrastructure, Kubernetes, documentation, or AI-assisted workflow changes while keeping the canonical path stable and easy to verify.

---

## Who this is for

This project is especially useful for:

- DevOps engineers
- platform engineers
- SREs
- cloud-native developers
- open-source maintainers
- workshop facilitators
- community contributors
- teams exploring AI-assisted infrastructure workflows

## Canonical v1 path

The live MVP is intentionally optimized for a **local macOS/Linux developer environment** with:
- Docker Desktop
- `kind`
- `kubectl`
- Terraform
- validation tools listed in the quickstart

The core flow is:

```bash
./scripts/bootstrap.sh
./scripts/validate.sh
./scripts/demo-up.sh
./scripts/demo-verify.sh
./scripts/demo-down.sh
```

## Live MVP vs examples vs docs-only

| Area | Status | Purpose |
|---|---|---|
| `platform/terraform/` | Live MVP | Terraform-managed demo foundation |
| `platform/kubernetes/` | Live MVP | Kubernetes composition and overlays |
| `platform/workloads/demo-app/` | Live MVP | Demo workload manifest source and content |
| `scripts/` | Live MVP | Canonical local workflow entrypoints |
| `.github/workflows/` | Live MVP | Validation and smoke workflow scaffolding |
| `examples/` | Example-only | Extra starter examples kept out of the happy path |
| `docs/examples/` | Example-only | Guidance for optional extensions |
| `docs/roadmap.md` | Docs-only | Future depth beyond v1 |

## Ownership boundary

The approved follow-up lane keeps one stable user path while making ownership clearer:

- `platform/workloads/demo-app/` is the single source of truth for demo workload-specific manifests and content
- `platform/kubernetes/` assembles workload assets into the canonical deployment path and keeps `overlays/local-kind/` as the stable entrypoint
- `platform/terraform/` continues to own only the shared demo foundation that runs before workload deployment

## Quick links

- [Quickstart](docs/quickstart.md)
- [Architecture](docs/architecture.md)
- [Contributor onboarding](docs/contributor-onboarding.md)
- [AI workflows](docs/ai-workflows.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Roadmap](docs/roadmap.md)
- [Contributing](CONTRIBUTING.md)

## Repository structure

```text
.
├── docs/                  # Quickstart, architecture, onboarding, roadmap
├── prompts/               # Repo-specific AI prompting surfaces
├── scripts/               # bootstrap / validate / demo-up / demo-verify / demo-down
├── platform/
│   ├── terraform/         # Live demo foundation
│   ├── kubernetes/        # Composition layer + local-kind overlay
│   ├── workloads/         # Workload-owned manifests/content
│   └── policies/          # Baseline policy guidance/config placeholders
├── examples/              # Example-only extensions
└── .github/workflows/     # CI validation + smoke workflow scaffolding
```

## What is intentionally not in live v1

These are **not** part of the canonical path:
- deep multi-cloud production abstraction
- service mesh or operator-heavy platform control planes
- full observability stacks
- enterprise governance bundles
- disaster recovery frameworks
- broad app framework scaffolding

See [Roadmap](docs/roadmap.md) for what comes later.

## Safe AI extension boundary

AI-assisted changes for v1 should stay within these classes unless separately planned:
1. duplicate or lightly adapt the demo workload overlay
2. add one small example under `examples/`
3. improve docs or validation guidance without changing the canonical runtime path

If a change makes the first demo harder to complete within about one hour, it should move out of the live MVP path.
