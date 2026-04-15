#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTRACT_ONLY=0

if [[ "${1:-}" == "--contract-only" ]]; then
  CONTRACT_ONLY=1
fi

run() {
  printf '\n==> %s\n' "$*"
  "$@"
}

cd "$ROOT_DIR"

run bash -n scripts/*.sh
run ruby -e "require 'yaml'; Dir['.github/workflows/*.yml', 'platform/kubernetes/**/*.yaml', 'platform/workloads/**/*.yaml', '.config/**/*.yml', '.config/**/*.yaml'].sort.each { |f| YAML.load_file(f) }"
run python3 scripts/repo_check.py
run python3 -m unittest -v tests/test_repo_contract.py
run kubectl kustomize platform/kubernetes/overlays/local-kind >/dev/null

if [[ "$CONTRACT_ONLY" -eq 1 ]]; then
  printf '\nContract-only validation completed successfully.\n'
  exit 0
fi

REQUIRED=(terraform tflint checkov yamllint kubeconform actionlint)
missing=0
for cmd in "${REQUIRED[@]}"; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    printf 'Missing required validation tool: %s\n' "$cmd" >&2
    missing=1
  fi
done

if [[ "$missing" -ne 0 ]]; then
  printf '\nInstall the required validation tools or use --contract-only for repo structure checks only.\n' >&2
  exit 1
fi

run terraform fmt -check -recursive platform/terraform
run terraform -chdir=platform/terraform/examples/local-demo init -backend=false
run terraform -chdir=platform/terraform/examples/local-demo validate
run tflint --chdir platform/terraform/examples/local-demo
run checkov -d platform/terraform
run yamllint -c .config/yamllint.yml \
  .github/workflows \
  .config/checkov/checkov.yaml \
  .config/yamllint.yml \
  platform/kubernetes \
  platform/workloads
rendered_manifest="$(mktemp)"
trap 'rm -f "$rendered_manifest"' EXIT
kubectl kustomize platform/kubernetes/overlays/local-kind >"$rendered_manifest"
run kubeconform -summary -strict "$rendered_manifest"
run actionlint .github/workflows/*.yml

printf '\nFull validation completed successfully.\n'
