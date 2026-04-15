# ADR-0001: Local-first MVP

## Status
Accepted

## Context
The project needs to be practical, demoable, cloud-agnostic, and realistic for open source. A provider-first v1 would add friction and branching too early.

## Decision
Adopt a **local-first, single canonical path** for v1 using Docker Desktop + `kind`.

Terraform remains in the live path by managing a lightweight demo foundation. Kubernetes handles workload deployment. Extra providers and extensions stay example-only or docs-only.

## Consequences
- the first-time user experience stays focused
- open-source maintenance stays realistic
- provider-specific depth is intentionally deferred
- the repo remains a strong demo and workshop asset
