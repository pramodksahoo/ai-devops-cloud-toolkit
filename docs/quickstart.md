# Quickstart

This is the **canonical v1 path**. If you are new to the repo, start here.

## Target environment

- macOS or Linux
- Docker Desktop running
- local Kubernetes via `kind`
- Terraform available locally
- validation tools available locally

## Prerequisites

Required commands for the full local workflow:
- `docker`
- `kind`
- `kubectl`
- `terraform`
- `tflint`
- `checkov`
- `yamllint`
- `kubeconform`
- `actionlint`
- `python3`
- `make`

## 1. Clone and inspect

```bash
git clone <your-fork-or-repo-url>
cd ai-devops-cloud-toolkit
```

Read these in order:
1. `README.md`
2. `docs/quickstart.md`
3. `docs/ai-workflows.md`

## 2. Bootstrap prerequisites

```bash
./scripts/bootstrap.sh
```

This script verifies the local toolchain and prints the missing tools you still need.

## 3. Run validation

```bash
./scripts/validate.sh
```

Validation includes:
- Terraform format / validate / lint / security
- YAML linting
- Kubernetes manifest validation
- GitHub Actions linting
- repository contract checks

## 4. Bring up the demo

```bash
./scripts/demo-up.sh
```

The live path does the following:
1. creates or reuses a `kind` cluster
2. applies the Terraform-managed demo foundation
3. deploys the demo workload with Kubernetes manifests

## 5. Verify the demo

```bash
./scripts/demo-verify.sh
```

Expected result:
- namespace `demo-toolkit` exists
- deployment `demo-app` rolls out successfully
- the service can be reached through a local port-forward

## 6. Tear down

```bash
./scripts/demo-down.sh
```

This deletes the Kubernetes resources, destroys the Terraform-managed foundation, and removes the `kind` cluster.

## Boundaries

Stay on the canonical path first.

Optional material belongs in:
- `examples/`
- `docs/examples/`
- `docs/roadmap.md`

## Fast orientation checklist

- [ ] README read
- [ ] prerequisites checked
- [ ] validation completed
- [ ] demo deployed
- [ ] demo verified
- [ ] teardown completed
- [ ] AI workflow docs reviewed before extending
