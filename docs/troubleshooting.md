# Troubleshooting

## `docker` not available

Make sure Docker Desktop is installed and running.

## `kind` not found

Install `kind` and re-run:

```bash
./scripts/bootstrap.sh
```

## Terraform validation fails

Check:
- your Terraform version
- local kubeconfig path
- whether the `kind` cluster is running before apply

## `demo-up.sh` fails at Terraform apply

The Terraform layer expects a reachable Kubernetes API for the local cluster. Confirm:

```bash
kubectl cluster-info
kubectl config current-context
```

## Demo workload does not become ready

Inspect:

```bash
kubectl -n demo-toolkit get all
kubectl -n demo-toolkit describe deploy/demo-app
kubectl -n demo-toolkit logs deploy/demo-app
```

## `demo-verify.sh` cannot reach the app

Check whether port-forwarding is blocked or already in use.

You can manually test:

```bash
kubectl -n demo-toolkit port-forward svc/demo-app 8080:80
curl http://127.0.0.1:8080
```

## Validation tool missing

The full validation path expects the listed tools to be installed.

For a repo-only structural check, use:

```bash
./scripts/validate.sh --contract-only
```
