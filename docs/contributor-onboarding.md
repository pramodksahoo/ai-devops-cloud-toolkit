# Contributor Onboarding

## Start here

If you are new to the project:
1. read the README
2. run the quickstart
3. understand the live/example/docs-only split
4. make one small change first

## Suggested first contributions

- improve a docs section
- improve script messages or error handling
- add an example under `examples/`
- duplicate the demo app as an example-only variant

## Repo contracts to protect

These are shared contracts and should be treated carefully:
- `docs/quickstart.md`
- `scripts/validate.sh`
- `scripts/demo-up.sh`
- `scripts/demo-verify.sh`
- live asset directories under `platform/`

If you change those, update docs and verification together.

## Workload boundary rule

For the live demo path:

- make workload-specific changes under `platform/workloads/demo-app/`
- treat `platform/kubernetes/` as the deployment composition and overlay layer
- treat `platform/terraform/` as shared foundation only

This keeps the approved path clear while preserving the same user-facing commands.

## Validation expectation

Use:

```bash
./scripts/validate.sh
```

If you do not have the full toolchain installed yet, use the contract-only repo checks first:

```bash
./scripts/validate.sh --contract-only
```

## Live vs example-only guidance

### Live MVP
- canonical quickstart
- Terraform demo foundation
- Kubernetes demo deployment
- GitHub Actions validation scaffolding
- AI-friendly contributor guidance

### Example-only
- extra providers
- extra workloads
- Helm sample
- observability sample
- GitOps sample

### Docs-only
- hardening notes
- cost-awareness notes
- roadmap and deferred topics
