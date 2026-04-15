# Contributing

Thanks for contributing to the AI DevOps Cloud Toolkit.

## Contribution goals for v1

The live MVP should stay:
- demo-first
- cloud-agnostic
- easy to understand
- safe for AI-assisted contribution
- realistic for open-source maintenance

## Before you open a PR

1. Read the [quickstart](docs/quickstart.md)
2. Read the [AI workflows guide](docs/ai-workflows.md)
3. Keep changes aligned with the live/example/docs-only boundary in the README
4. Run validation

```bash
./scripts/validate.sh
```

## Safe extension classes

The safest contribution types in v1 are:
- improve docs or troubleshooting
- improve validation guidance
- add a small example under `examples/`
- adapt the demo workload in a bounded way

Avoid broadening the canonical path unless the change is explicitly planned.

## PR checklist

- [ ] I kept the canonical quickstart path clear
- [ ] I did not move example-only content into the live MVP path by accident
- [ ] I updated docs if behavior changed
- [ ] I ran validation locally where possible
- [ ] I preserved the one-hour clone-to-demo experience

## Development workflow

```bash
./scripts/bootstrap.sh
./scripts/validate.sh
./scripts/demo-up.sh
./scripts/demo-verify.sh
./scripts/demo-down.sh
```

## AI-assisted contribution

This repo intentionally supports AI-assisted work.

Before asking an AI model to make changes:
- point it to `AGENTS.md`
- point it to the relevant prompt in `prompts/`
- tell it whether the change is **live MVP**, **example-only**, or **docs-only**
- require it to preserve the canonical path and validation commands
