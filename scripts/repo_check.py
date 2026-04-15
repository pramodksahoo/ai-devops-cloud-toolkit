#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md',
    'CONTRIBUTING.md',
    'LICENSE',
    'docs/quickstart.md',
    'docs/architecture.md',
    'docs/contributor-onboarding.md',
    'docs/troubleshooting.md',
    'docs/ai-workflows.md',
    'docs/roadmap.md',
    'docs/decisions/adr-0001-local-first-mvp.md',
    'prompts/extend-toolkit.md',
    'prompts/validate-change.md',
    'prompts/add-example.md',
    'scripts/bootstrap.sh',
    'scripts/validate.sh',
    'scripts/demo-up.sh',
    'scripts/demo-verify.sh',
    'scripts/demo-down.sh',
    'scripts/install-validation-tools.sh',
    'platform/terraform/modules/demo-foundation/main.tf',
    'platform/terraform/examples/local-demo/main.tf',
    'platform/kubernetes/base/kustomization.yaml',
    'platform/kubernetes/base/deployment.yaml',
    'platform/kubernetes/base/service.yaml',
    'platform/kubernetes/base/configmap.yaml',
    'platform/kubernetes/overlays/local-kind/kustomization.yaml',
    'platform/kubernetes/overlays/local-kind/kind-config.yaml',
    '.github/workflows/validate.yml',
    '.github/workflows/docs.yml',
    '.github/workflows/demo-smoke.yml',
    'Makefile',
]

EXAMPLE_ONLY_PATHS = [
    'examples/helm/README.md',
    'examples/observability/README.md',
    'examples/gitops/README.md',
    'examples/provider-sample/README.md',
    'docs/examples/helm/README.md',
    'docs/examples/observability/README.md',
    'docs/examples/gitops/README.md',
]


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_required_files() -> None:
    for rel in REQUIRED_FILES + EXAMPLE_ONLY_PATHS:
        ensure((ROOT / rel).exists(), f'missing required file: {rel}')


def check_readme_contract() -> None:
    readme = (ROOT / 'README.md').read_text()
    ensure(
        'clone -> bootstrap -> validate -> deploy to local Kubernetes -> verify -> extend safely with AI' in readme,
        'README must describe the canonical path',
    )
    ensure('Live MVP vs examples vs docs-only' in readme, 'README must explain repo boundaries')


def check_quickstart_contract() -> None:
    quickstart = (ROOT / 'docs/quickstart.md').read_text()
    for step in (
        './scripts/bootstrap.sh',
        './scripts/validate.sh',
        './scripts/demo-up.sh',
        './scripts/demo-verify.sh',
        './scripts/demo-down.sh',
    ):
        ensure(step in quickstart, f'quickstart missing canonical command: {step}')


def check_terraform_contract() -> None:
    module_main = (ROOT / 'platform/terraform/modules/demo-foundation/main.tf').read_text()
    example_main = (ROOT / 'platform/terraform/examples/local-demo/main.tf').read_text()
    ensure('resource "kubernetes_namespace"' in module_main, 'terraform module must create namespace')
    ensure('resource "kubernetes_service_account"' in module_main, 'terraform module must create service account')
    ensure('module "demo_foundation"' in example_main, 'local demo example must use demo foundation module')


def check_kubernetes_contract() -> None:
    deployment = (ROOT / 'platform/kubernetes/base/deployment.yaml').read_text()
    service = (ROOT / 'platform/kubernetes/base/service.yaml').read_text()
    ensure('name: demo-app' in deployment, 'deployment must define demo-app')
    ensure('name: demo-app' in service, 'service must define demo-app')


def check_workflow_contract() -> None:
    validate = (ROOT / '.github/workflows/validate.yml').read_text()
    smoke = (ROOT / '.github/workflows/demo-smoke.yml').read_text()
    ensure('scripts/validate.sh' in validate, 'validate workflow must run validation')
    ensure(
        'scripts/install-validation-tools.sh' in validate and 'scripts/install-validation-tools.sh' in smoke,
        'validation workflows must use the shared install helper',
    )
    ensure(
        'scripts/demo-up.sh' in smoke and 'scripts/demo-verify.sh' in smoke,
        'smoke workflow must call demo scripts',
    )


def main() -> int:
    check_required_files()
    check_readme_contract()
    check_quickstart_contract()
    check_terraform_contract()
    check_kubernetes_contract()
    check_workflow_contract()
    print('Repository contract checks passed.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f'REPO CHECK FAILED: {exc}', file=sys.stderr)
        raise SystemExit(1)
