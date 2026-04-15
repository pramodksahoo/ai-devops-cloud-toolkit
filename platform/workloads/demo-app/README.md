# Demo App

The live demo workload is a deliberately small NGINX-based application that serves a static page.

It is simple on purpose:
- fast to pull and run on `kind`
- easy to verify with a port-forward
- easy to extend for workshops or examples

## Ownership contract

This directory is the single source of truth for demo workload-specific assets.

- keep workload manifests, config, and content here
- use `platform/kubernetes/` to assemble those assets into the canonical deployment path
- keep Terraform focused on shared foundation resources only

## Safe change guidance

When you update the live demo workload:

1. change workload-specific assets here first
2. keep the canonical flow unchanged: `bootstrap -> validate -> demo-up -> demo-verify -> demo-down`
3. only update `platform/kubernetes/` when composition or overlay wiring needs to change
