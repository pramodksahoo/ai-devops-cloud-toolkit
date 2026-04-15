#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLUSTER_NAME="${CLUSTER_NAME:-toolkit-demo}"
TERRAFORM_DIR="$ROOT_DIR/platform/terraform/examples/local-demo"
KUSTOMIZE_DIR="$ROOT_DIR/platform/kubernetes/overlays/local-kind"
KIND_CONFIG="$KUSTOMIZE_DIR/kind-config.yaml"

require() {
  command -v "$1" >/dev/null 2>&1 || { printf 'Missing required command: %s\n' "$1" >&2; exit 1; }
}

for cmd in docker kind kubectl terraform; do
  require "$cmd"
done

if ! kind get clusters | grep -qx "$CLUSTER_NAME"; then
  printf 'Creating kind cluster %s...\n' "$CLUSTER_NAME"
  kind create cluster --name "$CLUSTER_NAME" --config "$KIND_CONFIG"
else
  printf 'Reusing existing kind cluster %s\n' "$CLUSTER_NAME"
fi

printf 'Applying Terraform-managed demo foundation...\n'
terraform -chdir="$TERRAFORM_DIR" init
terraform -chdir="$TERRAFORM_DIR" apply -auto-approve \
  -var="cluster_context=kind-$CLUSTER_NAME" \
  -var="kubeconfig_path=${KUBECONFIG:-$HOME/.kube/config}"

printf 'Deploying Kubernetes demo workload...\n'
kubectl apply -k "$KUSTOMIZE_DIR"
kubectl -n demo-toolkit rollout status deployment/demo-app --timeout=180s

printf '\nDemo environment is up. Next step: ./scripts/demo-verify.sh\n'
