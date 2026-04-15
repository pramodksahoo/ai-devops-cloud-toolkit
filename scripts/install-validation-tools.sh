#!/usr/bin/env bash
set -euo pipefail

OS="${1:-linux}"
ARCH="${2:-amd64}"
DEST_BIN="${DEST_BIN:-/usr/local/bin}"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

python -m pip install --upgrade pip
python -m pip install checkov yamllint

curl -sSL -o "$TMP_DIR/kubeconform.tar.gz" \
  "https://github.com/yannh/kubeconform/releases/download/v0.6.7/kubeconform-${OS}-${ARCH}.tar.gz"
tar -xzf "$TMP_DIR/kubeconform.tar.gz" -C "$TMP_DIR"
sudo mv "$TMP_DIR/kubeconform" "$DEST_BIN/kubeconform"

curl -sSL -o "$TMP_DIR/actionlint.tar.gz" \
  "https://github.com/rhysd/actionlint/releases/download/v1.7.7/actionlint_1.7.7_${OS}_${ARCH}.tar.gz"
tar -xzf "$TMP_DIR/actionlint.tar.gz" -C "$TMP_DIR"
sudo mv "$TMP_DIR/actionlint" "$DEST_BIN/actionlint"
