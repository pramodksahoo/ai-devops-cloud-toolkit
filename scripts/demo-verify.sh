#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${NAMESPACE:-demo-toolkit}"
SERVICE="${SERVICE:-demo-app}"
LOCAL_PORT="${LOCAL_PORT:-8080}"

command -v kubectl >/dev/null 2>&1 || { printf 'kubectl is required\n' >&2; exit 1; }

kubectl -n "$NAMESPACE" get deploy "$SERVICE" >/dev/null
kubectl -n "$NAMESPACE" rollout status deployment/"$SERVICE" --timeout=120s >/dev/null
kubectl -n "$NAMESPACE" get pods

kubectl -n "$NAMESPACE" port-forward svc/"$SERVICE" "$LOCAL_PORT":80 >/tmp/demo-app-port-forward.log 2>&1 &
pf_pid=$!
trap 'kill "$pf_pid" >/dev/null 2>&1 || true' EXIT
sleep 3

if command -v curl >/dev/null 2>&1; then
  body="$(curl -fsS "http://127.0.0.1:${LOCAL_PORT}")"
else
  body="$(python3 - <<PY
import urllib.request
print(urllib.request.urlopen('http://127.0.0.1:${LOCAL_PORT}').read().decode())
PY
)"
fi

printf '%s\n' "$body"
if [[ "$body" != *"AI DevOps Cloud Toolkit"* ]]; then
  printf 'Unexpected demo response\n' >&2
  exit 1
fi

printf '\nDemo verification succeeded.\n'
