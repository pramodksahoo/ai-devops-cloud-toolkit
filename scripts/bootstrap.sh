#!/usr/bin/env bash
set -euo pipefail

REQUIRED=(docker kind kubectl terraform tflint checkov yamllint kubeconform actionlint python3 make)

printf 'Checking local prerequisites for the canonical demo path...\n\n'
missing=0
for cmd in "${REQUIRED[@]}"; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf '[ok] %s -> %s\n' "$cmd" "$(command -v "$cmd")"
  else
    printf '[missing] %s\n' "$cmd"
    missing=1
  fi
done

printf '\nNotes:\n'
printf -- '- Docker Desktop should be running before demo-up.\n'
printf -- '- kind should provide the local Kubernetes cluster.\n'
printf -- '- Terraform and validation tools are required for the full validate/demo flow.\n'

if [[ "$missing" -ne 0 ]]; then
  printf '\nOne or more required tools are missing. Install them, then re-run this script.\n' >&2
  exit 1
fi

printf '\nAll required tools were found. You can continue with ./scripts/validate.sh\n'
