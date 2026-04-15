SHELL := /bin/bash

.PHONY: bootstrap validate validate-contract demo-up demo-verify demo-down repo-check test

bootstrap:
	./scripts/bootstrap.sh

validate:
	./scripts/validate.sh

validate-contract:
	./scripts/validate.sh --contract-only

repo-check:
	python3 scripts/repo_check.py

test:
	python3 -m unittest -v tests/test_repo_contract.py

demo-up:
	./scripts/demo-up.sh

demo-verify:
	./scripts/demo-verify.sh

demo-down:
	./scripts/demo-down.sh
