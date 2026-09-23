## Why

The current Blender AIGC skill package exposes strong single-domain skills (`blender-design`,
`blender-character-rigging`, `blender-cinematography`, etc.) but does not provide a user-facing
workflow that turns a **2D reference image** (古画 / 概念图 / 电影画面 / 角色三视图) into an
editable 3D Blender scene through LLM-driven iteration. The pattern is observable in the wild
(豆包 + Blender MCP + dream-loop 复刻 《清明上河图》 as a micro-scene, 2026-09), but the
package today leaves the orchestration glue — the dream-loop, the VLM critic wiring, the
transaction-batched scene-edit envelope — to every user that wants to replicate it.

This change ships that orchestration as a single independently installable skill so granular
installations (e.g., `npx skills add full-aigc-skills/blender-skills --skill blender-ai-replication`)
deliver a working reference image → 3D scene pipeline without forcing every consumer to
hand-roll the same loop.

## What Changes

- Add `blender-ai-replication` for reference-image → LLM-driven Blender iteration with a
  VLM critic loop, sitting on top of any one of three independent Blender MCP ecosystems
  (PartMe / Codex / ahujasid).
- Ship a reference orchestrator (`scripts/dream_loop.py`) that wraps `harness_cli.py`,
  threads `transactionId` + `sceneRevision`, and plugs in a stub-or-real critic.
- Ship a complete first-version JSON command sequence
  (`references/qingming-sequence.md`) so a user can copy-paste 30 envelopes and reproduce
  the canonical 《清明上河图》 micro-scene case study end-to-end.
- Ship an ecosystem decision matrix (`references/ecosystem-choices.md`) because the three
  Blender MCP ecosystems are NOT interchangeable (different Add-on names, N-panel
  categories, and setup paths).
- Ship verified pitfalls (`references/pitfalls.md`) from the 2026-09-23 smoke-test
  (`smoke-test-001`, PartMe plugin cache v0.14.1) so future runs do not re-discover
  `pgrep -f Blender` false-positives, `export.file format` rejections, or
  `transactionId` echoing.
- Bump the package version `1.1.0` → `1.2.0` and update the bilingual catalog.

## Capabilities

### New Capabilities

- `ai-driven-image-replication`: Iterate a Blender scene toward a target 2D image via an
  LLM driver + VLM critic on top of a Blender MCP bridge, returning per-round screenshot
  + diff prompt + final-transaction artifact.

### Modified Capabilities

None.

## Impact

- Affects the package manifest (`plugin.json`), bilingual READMEs, and CHANGELOG.
- Affects one new skill directory: `skills/blender-ai-replication/` with `SKILL.md`,
  `references/` (3 docs), `scripts/` (1 executable).
- Adds one new capability spec to `openspec/specs/ai-driven-image-replication/spec.md`.
- Does NOT modify any existing skill.
- Does NOT introduce a new Blender MCP ecosystem — PartMe / Codex / ahujasid all exist
  upstream; this skill routes between them, does not own any.
- Does NOT introduce network calls or paid actions at skill level; the optional
  `--critic vlm` mode in `dream_loop.py` is a user-wired stub they replace with their own
  provider SDK.

## Out of Scope

- Forking `achimala/dream-loop`. The bundled orchestrator is a thin reference, not a fork.
- Building a unified Blender MCP bridge. The three ecosystems remain independent; this
  skill documents which one to pick and how to talk to it.
- Web frontend (Three.js / R3F) for the tutorial's "click NPC, third-person roam" layer.
  That work happens after `qm-v1.glb` export, in a separate web project.