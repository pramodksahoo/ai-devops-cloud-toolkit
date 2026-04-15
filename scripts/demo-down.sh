#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLUSTER_NAME="${CLUSTER_NAME:-toolkit-demo}"
TERRAFORM_DIR="$ROOT_DIR/platform/terraform/examples/local-demo"
KUSTOMIZE_DIR="$ROOT_DIR/platform/kubernetes/overlays/local-kind"

if command -v kubectl >/dev/null 2>&1; then
  kubectl delete -k "$KUSTOMIZE_DIR" --ignore-not-found || true
fi

if command -v terraform >/dev/null 2>&1; then
  terraform -chdir="$TERRAFORM_DIR" destroy -auto-approve \
    -var="cluster_context=kind-$CLUSTER_NAME" \
    -var="kubeconfig_path=${KUBECONFIG:-$HOME/.kube/config}" || true
fi

if command -v kind >/dev/null 2>&1 && kind get clusters | grep -qx "$CLUSTER_NAME"; then
  kind delete cluster --name "$CLUSTER_NAME"
fi

printf 'Demo environment torn down.\n'
