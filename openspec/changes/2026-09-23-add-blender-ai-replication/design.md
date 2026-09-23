## Context

The package already owns independently installable domain skills for scene assembly,
character rigging, cinematography, rendering, sequencing, simulation, and validation.
Three Blender MCP ecosystems ship independently in the broader ecosystem: PartMe (in the
plugin cache v0.14.1, addon name `PartMe Blender MCP`, N-panel `PartMe MCP`),
Codex (in the local clone v1.1.0, addon name `Blender Connector`, N-panel `Codex`), and
the community `ahujasid/blender-mcp` (no curated addon name). Each ships its own
`mcp-setup` skill and its own protocol envelope; none share schemas.

The dream-loop pattern (reference image → LLM edit → VLM critic → diff prompt → next round)
became observable in 2026-09 as a way to recreate 2D artwork as 3D Blender scenes with
LLM drivers (豆包 Seed 2.1 Pro). The pattern requires three moving parts that the package
must NOT lock in: the bridge, the LLM, and the VLM. The skill's role is to ship the
orchestration glue and document the decision matrix.

## Goals / Non-Goals

**Goals:**

- Ship one independently installable skill `blender-ai-replication` with the
  orchestration skeleton, not the bridge.
- Cover all three Blender MCP ecosystems with the same orchestrator contract, so
  switching bridges is a parameter change, not a rewrite.
- Produce observable local evidence per round (screenshot + `critic.json`) so users can
  audit convergence without trusting the producer's declared sha256.
- Verify the chain end-to-end with a real Blender session (PartMe plugin cache v0.14.1,
  smoke-test `smoke-test-001`, 2026-09-23) and document the pitfalls encountered.

**Non-Goals:**

- Add or modify Blender MCP commands, PartMe / Codex / ahujasid addons, or provider SDKs.
- Ship a fork of `achimala/dream-loop`. The bundled `dream_loop.py` is a thin reference.
- Guarantee convergence on the target image. Convergence is a property of the user's VLM
  critic and target image, not the orchestration.
- Cover web frontend (Three.js / R3F) for the tutorial's interactive layer.

## Decisions

### One orchestration skill, three bridges

**Decision.** `blender-ai-replication` exposes the dream-loop orchestration. The bridge
(PartMe / Codex / ahujasid) is documented in `references/ecosystem-choices.md` and wired
via the user's own MCP-setup skill. The orchestrator never imports or depends on a
specific bridge's Python internals — it shells out to `harness_cli.py` for PartMe or the
equivalent for Codex.

**Why.** Trying to ship a unified bridge means taking on a dependency on every MCP
ecosystem's runtime, breaking one of the three each time a vendor changes a CLI flag. The
plugin cache and local clone have already diverged (skill count 36 vs 25, Add-on name
`PartMe Blender MCP` vs `Blender Connector`). Converging at the orchestration level is
cheap; converging at the bridge level is intractable.

**Alternative considered.** Ship three skills (`blender-ai-replication-partme`,
`blender-ai-replication-codex`, `blender-ai-replication-ahujasid`). Rejected: would force
the user to choose a bridge at install time, when the meaningful choice is at runtime.

### Pluggable critic with stub default

**Decision.** The bundled `dream_loop.py` ships a `stub` critic that runs the loop end-to-end
without an API key, and a `vlm` critic placeholder that raises `NotImplementedError`. Users
wire their own provider SDK into `critic_vlm()`.

**Why.** The orchestration logic (transaction threading, screenshot capture, score diff) is
the reusable part. The VLM call itself depends on provider choice (Volcengine Ark SDK, OpenAI
Vision, Anthropic). Shipping a stub means a user can validate the wiring before spending
API credits; shipping a real-call default would lock them into one provider.

**Alternative considered.** Ship one provider's SDK as the default. Rejected: locks the
package into a vendor, drifts as soon as one SDK version changes.

### Verified pitfalls are first-class content

**Decision.** Eight pitfalls observed during the 2026-09-23 smoke-test ship as
`references/pitfalls.md`. The most surprising: `blender_auto_setup`'s `pgrep -f Blender`
false-positive on stale `blender_mcp_server.py` processes blocks the auto-install path
until those processes are cleaned.

**Why.** The same trap will catch every future user. A pitfall page that names the
root cause, the recovery, and the upstream issue location is more valuable than a
troubleshooting flowchart.

**Alternative considered.** Bake pitfalls into `SKILL.md` Gotchas section only.
Rejected: 8 pitfalls would push `SKILL.md` past the 500-line limit and dilute the
skill's main contract.

## Risks

### The three bridges will keep diverging

If PartMe v0.15.0 ships breaking changes to `harness_cli.py`, the orchestrator's
`harness_send` wrapper will break silently. Mitigation: the orchestrator is small enough
(~140 lines) to be re-targeted when any single bridge breaks. No upstream coupling.

### The Python orchestrator will fail codeguard python lint

`dream_loop.py` already had one `F401 sys imported but unused` flagged during drafting
and was fixed. Future additions must keep the file under the package's python constraints
(import order, no unused imports, line length, docstrings). Mitigation: include the file
in the change so reviewers can re-run `codeguard lint` before merge.

### OpenSpec conventions drift

This change uses the same `proposal.md` / `design.md` / `tasks.md` / `specs/<name>/spec.md`
shape as `2026-09-21-integrate-blender-video-workflows`. If the openspec format changes
in a future openspec release, this change will need revalidation. Mitigation: this is
normal openspec lifecycle; archive and re-propose as needed.