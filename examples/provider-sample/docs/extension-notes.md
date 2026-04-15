# Provider sample extension notes

This note exists to keep future provider-oriented examples consistent.

## Safe extension checklist

1. Start from the neutral scaffold in this directory and the rules in `prompts/add-example.md`.
2. Add provider-specific context under `providers/` first.
3. Keep optional modules under `modules/`.
4. Keep illustrative manifests under `manifests/`.
5. Update `docs/examples/provider-sample.md` so readers understand the boundary and intent.

## Anti-patterns

- moving provider content into `platform/`
- changing the root README quickstart to point at provider-specific material
- treating the sample as an officially supported deployment target
