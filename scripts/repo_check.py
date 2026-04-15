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
    'platform/kubernetes/base/README.md',
    'platform/kubernetes/base/kustomization.yaml',
    'platform/kubernetes/overlays/local-kind/kustomization.yaml',
    'platform/kubernetes/overlays/local-kind/kind-config.yaml',
    'platform/workloads/demo-app/README.md',
    'platform/workloads/demo-app/manifests/kustomization.yaml',
    'platform/workloads/demo-app/manifests/deployment.yaml',
    'platform/workloads/demo-app/manifests/service.yaml',
    'platform/workloads/demo-app/manifests/index.html',
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
    'examples/provider-sample/providers/TEMPLATE.md',
    'examples/provider-sample/modules/README.md',
    'examples/provider-sample/manifests/README.md',
    'examples/provider-sample/docs/extension-notes.md',
    'docs/examples/helm/README.md',
    'docs/examples/observability/README.md',
    'docs/examples/gitops/README.md',
    'docs/examples/provider-sample.md',
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
    base_kustomization = (ROOT / 'platform/kubernetes/base/kustomization.yaml').read_text()
    base_readme = (ROOT / 'platform/kubernetes/base/README.md').read_text()
    workload_deployment = (ROOT / 'platform/workloads/demo-app/manifests/deployment.yaml').read_text()
    workload_service = (ROOT / 'platform/workloads/demo-app/manifests/service.yaml').read_text()
    workload_kustomization = (ROOT / 'platform/workloads/demo-app/manifests/kustomization.yaml').read_text()
    workload_content = (ROOT / 'platform/workloads/demo-app/manifests/index.html').read_text()
    workload_readme = (ROOT / 'platform/workloads/demo-app/README.md').read_text()
    architecture = (ROOT / 'docs/architecture.md').read_text()

    ensure(
        '../../workloads/demo-app/manifests' in base_kustomization,
        'kubernetes base must compose workload-owned manifests',
    )
    ensure(
        'platform/workloads/demo-app/' in base_readme,
        'kubernetes base README must explain workload ownership',
    )
    ensure('name: demo-app' in workload_deployment, 'workload deployment must define demo-app')
    ensure('name: demo-app' in workload_service, 'workload service must define demo-app')
    ensure('configMapGenerator' in workload_kustomization, 'workload manifests must generate demo content config')
    ensure('index.html' in workload_kustomization, 'workload manifests must source demo content from index.html')
    ensure('AI DevOps Cloud Toolkit' in workload_content, 'workload content must retain the demo page identity')
    ensure('single source of truth' in workload_readme, 'workload README must explain workload ownership')
    ensure('workload-specific runtime assets' in architecture, 'architecture doc must explain workload ownership boundary')

    for rel in (
        'platform/kubernetes/base/deployment.yaml',
        'platform/kubernetes/base/service.yaml',
        'platform/kubernetes/base/configmap.yaml',
    ):
        ensure(not (ROOT / rel).exists(), f'kubernetes base must not own duplicate workload manifest: {rel}')


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


def check_provider_sample_contract() -> None:
    examples_index = (ROOT / 'examples/README.md').read_text()
    docs_examples_index = (ROOT / 'docs/examples/README.md').read_text()
    provider_sample = (ROOT / 'examples/provider-sample/README.md').read_text()
    provider_guide = (ROOT / 'docs/examples/provider-sample.md').read_text()
    extension_notes = (ROOT / 'examples/provider-sample/docs/extension-notes.md').read_text()

    ensure('provider-sample/' in examples_index, 'examples index must link to the provider sample')
    ensure('provider-sample.md' in docs_examples_index, 'docs examples index must link to the provider sample guide')
    ensure('example-only' in provider_sample.lower(), 'provider sample README must be labeled example-only')
    ensure('officially supports a cloud provider' in provider_sample, 'provider sample README must reject official provider support wording')
    ensure('docs/examples/provider-sample.md' in provider_sample, 'provider sample README must point to the canonical provider sample guide')
    ensure('prompts/add-example.md' in provider_guide, 'provider sample guide must reference prompts/add-example.md')
    ensure('canonical local-first path' in provider_guide, 'provider sample guide must preserve the canonical path')
    ensure('platform/' in provider_guide, 'provider sample guide must keep provider assets out of platform/')
    ensure('prompts/add-example.md' in extension_notes, 'extension notes must reference prompts/add-example.md')


def main() -> int:
    check_required_files()
    check_readme_contract()
    check_quickstart_contract()
    check_terraform_contract()
    check_kubernetes_contract()
    check_workflow_contract()
    check_provider_sample_contract()
    print('Repository contract checks passed.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f'REPO CHECK FAILED: {exc}', file=sys.stderr)
        raise SystemExit(1)
