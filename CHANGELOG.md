# Changelog

## 1.2.0 - 2026-09-23

- Added `blender-ai-replication` for LLM-driven, VLM-critic-validated iteration on top of a Blender MCP bridge.
- Bundled `scripts/dream_loop.py` (~140 lines): closed-envelope harness wrapper, transaction-threaded edits, pluggable critic (stub / vlm).
- Bundled `references/qingming-sequence.md`: full first-version JSON command sequence (capability.list → transaction.begin → object.create_mesh → material → scene.screenshot → commit → job.submit RENDER_STILL → export.glb), tested live against PartMe plugin cache v0.14.1.
- Bundled `references/ecosystem-choices.md` + `references/pitfalls.md`: decision matrix for PartMe vs Codex vs ahujasid bridges; verified pitfalls (auto_setup pgrep false-positive, transactionId empty rejection, export.format rejected, expectedSceneRevision threading).
- Manifest bumped to 26 skills; `plugin.json` version 1.1.0 → 1.2.0.

## 1.1.0 - 2026-09-21

- Added `blender-video-recreate` for evidence-backed reference-video analysis and editable Blender white-model reconstruction.
- Added `blender-video-original` for prose-to-shot planning, articulated white-model animation, validation, and optional authorized generation handoff.
- Added manifest completeness and upstream MIT attribution gates; package now contains 25 independently installable skills.

## 1.0.1 - 2026-09-20

- Expanded all 23 Blender skills with standalone triggers, prerequisites, workflows, validation evidence, boundaries, and recovery guidance.
- Added portable request, validation, recovery, and acceptance templates for granular skill installations.
- Added deterministic lint gates for required sections, local-link integrity, frontmatter, and document length.
- Removed package-external and sibling-relative documentation dependencies.

## 1.0.0

- Initial public package release with 23 Blender skills.
