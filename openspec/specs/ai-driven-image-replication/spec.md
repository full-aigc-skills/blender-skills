# ai-driven-image-replication Specification

## Purpose

This spec defines the contract for `blender-ai-replication`: the reference-image →
LLM-driven → VLM-critic-iterated Blender workflow that lets a user recreate 2D artwork
(ancient paintings, concept art, film frames) as an editable 3D Blender scene without
hand-rolling the orchestration glue themselves.

The skill ships in three flavors and one orchestrator. The flavors are persisted state for
the user (skills under `skills/blender-ai-replication/`); the orchestrator is the
runtime entry point (`scripts/dream_loop.py`) that talks to whichever Blender MCP
ecosystem the user has installed (PartMe / Codex / ahujasid).

## Requirements

### Requirement: Iterative reference-image to Blender scene

The `blender-ai-replication` skill SHALL drive a Blender scene toward a target 2D image
through an outer loop of: LLM edit, screenshot, VLM-style critic, diff prompt, next round.
The skill SHALL ship a reference `dream_loop.py` orchestrator that wraps the bridge's
harness CLI, threads transaction IDs and scene revisions across edits, and exposes a
pluggable critic with a `stub` default that runs the loop without an API key.

#### Scenario: User has a reference image and an LLM driver

- **WHEN** the user provides a target image and a short initial prompt
- **THEN** the skill routes the user to launch a Blender MCP session, run a
  first-version JSON command sequence, then iterate via the bundled orchestrator
- **AND** each round produces a `screenshot.png` and a `critic.json` under
  `--output-dir/round-NN/` so the user can audit convergence

### Requirement: Three Blender MCP ecosystems, one orchestrator

The skill SHALL document the PartMe, Codex, and ahujasid Blender MCP ecosystems with their
respective Add-on names, N-panel categories, setup entry points, and capability drift
(`references/ecosystem-choices.md`). The orchestrator SHALL NOT hard-depend on any one
ecosystem's Python internals — it shells out to the user's chosen bridge.

#### Scenario: User picks PartMe

- **WHEN** the user is on the `full-aigc-plugins/blender-design` ecosystem
- **THEN** the skill points them at `launch_harness.py` + `harness_cli.py` and explains
  the auto-install `blender_auto_setup` is gated on a known pgrep false-positive
- **AND** provides the working directory + descriptor.json + output-root path convention

### Requirement: First-version command sequence is reproducible

The skill SHALL ship a complete first-version JSON command sequence
(`references/qingming-sequence.md`) covering: capability probe, transaction begin,
mesh creation, material binding, mid-transaction screenshot, commit, lighting +
camera, render jobs, and export. The sequence SHALL be tested end-to-end against at
least one Blender MCP ecosystem and SHALL mark each envelope as tested or
schema-only.

#### Scenario: User reproduces the canonical case study

- **WHEN** the user runs the `qingming-sequence.md` against a fresh PartMe session
- **THEN** they produce a scene with the documented object count and a `qm-v1.glb`
  whose `result.artifact.sha256` matches the local `shasum -a 256`
- **AND** the export can be loaded into Three.js / R3F for the tutorial's interactive
  layer (out of scope for this skill)

### Requirement: Verified pitfalls are first-class content

The skill SHALL ship a `references/pitfalls.md` listing every pitfall observed during
verification, including the `pgrep -f Blender` false-positive that blocks
`blender_auto_setup` when stale `blender_mcp_server.py` processes are running. Each
pitfall SHALL name its symptom, root cause, recovery, and upstream issue location.

#### Scenario: User hits `TRANSACTION_NOT_FOUND`

- **WHEN** the user runs a modify command with a fresh `transactionId` that was not
  passed to `transaction.begin`
- **THEN** the skill points them at `references/pitfalls.md` rule 5 (`transactionId`
  echoed vs generated) and the SKILL.md Gotchas section
- **AND** they recover by calling `transaction.begin` first with a fresh unique id
  and threading that id through subsequent modify commands

### Requirement: Domain claims are evidence-bound

Every workflow SHALL distinguish command success from artifact or visual acceptance and
SHALL identify the receipt, measurement, preview, save/reopen, or re-import evidence
required for completion. Convergence on the target image SHALL require critic score
above a documented threshold (default 0.9) AND a successfully committed final
snapshot, not command success alone.

#### Scenario: User claims convergence

- **WHEN** the user asserts the scene matches the target image
- **THEN** the skill requires the `dream_loop.log` showing `score >= 0.9` AND a
  successful `transaction.commit` of the final round AND `export.artifact.sha256`
  matching the local file
- **AND** missing evidence is reported as `UNVERIFIED`, not `passed`