## Why

The 23 published Blender skills currently average 3.789 under TRACE and omit repeatable workflow, validation, failure-handling, and capability-boundary guidance in several domain skills. They need a consistent operational contract before the next external-skill release so agents can trigger and execute them safely instead of treating short summaries as complete procedures.

## What Changes

- Expand every Blender skill with explicit trigger conditions, prerequisites, ordered execution, validation evidence, and common failure recovery.
- Keep domain-specific command and acceptance guidance in each skill while moving reusable operating policy into package references.
- Remove install-fragile relative references to sibling skills or package-level docs.
- Add deterministic lint and TRACE release gates requiring all 23 skills to score at least 4.5.
- Dispatch only immutable release tags and peeled commit SHAs to the actual Blender plugin consumer.
- Replace the obsolete Codex-only plugin identity in public package documentation.

## Capabilities

### New Capabilities

- `skill-quality-gate`: Defines the authoring, portability, validation, and TRACE requirements for published Blender skills.

### Modified Capabilities

None.

## Impact

This changes `skills/*/SKILL.md`, skill-local references/examples, package validation tooling, and the release dispatch workflow. It does not change Blender plugin runtime code, command schemas, or the already published `v1.0.0` tag.
