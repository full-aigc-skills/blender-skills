---
name: blender-ai-replication
description: "Replicate a reference image (ancient Chinese painting, concept art, film frame) as a 3D Blender scene through LLM-driven iteration on top of a Blender MCP bridge. Covers dream-loop orchestration, VLM critic integration, transaction-batched scene edits, and the first-version → iterate → render → export pipeline. Use when the user has a target image and wants iterative AI-driven Blender modeling (e.g., recreating 《清明上河图》 as a 3D micro-scene from a screenshot)."
---

# Blender AI-Replication

Drive a Blender scene from a target image via LLM-orchestrated MCP commands and a VLM critic loop. The
pattern is: target image → first-version model → per-round screenshot + VLM critic + diff prompt →
next round, then render → export glTF. Companion skill to **`blender-design`**, which handles
non-iterative Blender work without an LLM critic.

This skill is the bridge between three otherwise independent worlds: a Blender MCP transport
(PartMe / Codex / ahujasid), an LLM driver (豆包 / Claude / OpenAI / Doubao Seed 2.1 Pro), and a
VLM critic (豆包 vision / OpenAI vision / any multimodal model). The skill ships the
orchestration glue — the user wires the three endpoints.

For a full first-version command sequence of a 《清明上河图》 micro-scene, see
`references/qingming-sequence.md`. For the orchestrator, see `scripts/dream_loop.py`.

## 什么时候使用（When to Use）

Use this skill when:

- 用户有一张参考图（古画、概念图、电影画面、角色三视图）想复刻为可编辑 Blender 场景。
- 用户要"长镜头运镜复刻"模式（Blender 当摄影指导 + 下游视频生成）。
- 用户需要 dream-loop 闭环（reference → build → VLM critic → diff prompt → next round）。
- 非迭代单次 Blender 任务应直接触发 `blender-design`；本技能不是替代品。

Three MCP ecosystems are NOT interchangeable. Pick one before installing — see `When to Use` and
`references/ecosystem-choices.md`:

| Ecosystem | Add-on name | N-panel | Setup entry | Source |
|---|---|---|---|---|
| **PartMe** (plugin cache v0.14.1) | PartMe Blender MCP | PartMe MCP | `blender_auto_setup` (auto) | `full-aigc-plugins/blender-design` |
| **Codex** (local clone v1.1.0) | Blender Connector | Codex | `blender_getting_started` (manual) | `full-aigc-skills/blender-skills` |
| **ahujasid** (community) | `blender-mcp` | varies | git clone + manual | github.com/ahujasid/blender-mcp |

The original 清上河图 3D blog post links ahujasid — that URL does not satisfy the connection
check of either packaged plugin. If the user's only goal is "follow the tutorial exactly",
install ahujasid and stop.

## 输入与前置条件（Prerequisites）

- **Blender MCP session running.** Launch via `launch_harness.py --session-id <id> --output-root <path> --export-format <fmt>` (PartMe) or the equivalent for your chosen ecosystem. Save the `descriptorPath`.
- **harness_cli.py reachable.** For PartMe: `<plugin>/scripts/harness_cli.py`.
- **Target image.** A reference PNG/JPG readable from the orchestrator's working directory.
- **Initial prompt.** A short Chinese or English text describing the first-version scene.
- **Output dir inside `--output-root`.** Outside it → `OUTPUT_NOT_AUTHORIZED`.
- **Optional: real VLM critic.** For `--critic vlm`, wire `critic_vlm()` in `scripts/dream_loop.py` with your provider's SDK call (Volcengine Ark / OpenAI vision). Default `stub` runs the loop without an API key.
- **Disk reservation:** `max(20% 卷容量, 20GB)`. Long RENDER_ANIMATION jobs may be denied.
- **Python 3.10+** on the orchestrator host.

## 执行流程（Workflow）

### 1. Pick ecosystem + launch session

```bash
# PartMe path (this skill's primary test path):
python3 ~/.zcode/cli/plugins/cache/full-aigc-plugins/blender-design/0.14.1/scripts/launch_harness.py \
    --session-id "qingming-v1" \
    --output-root "/Users/wandl/partme/blender/design-outputs" \
    --execution-mode "auto_with_budget" \
    --export-format "glb"
# → save descriptor.json path
```

If `blender_auto_setup` returns `stage: enable, manualHint: "检测到 Blender 正在运行..."` but
`ps aux | grep blender` shows no real Blender GUI, the detector has a known false-positive on
stale `blender_mcp_server.py` processes — skip auto_setup, call `launch_harness.py` directly.

### 2. First-version command sequence

Run the JSON envelopes in `references/qingming-sequence.md`:

1. **Probe (read, `tx="READ"` sentinel)** — `capability.list` + `scene.inspect` to get current scene revision.
2. **Begin transaction** — capture `transactionId` + `sceneRevision` from response.
3. **Inside the same tx** — `object.create_mesh` × N (sand base, river, bridge, buildings),
   `material.create_pbr` × M, `material.assign`, mid-tx `scene.screenshot`.
4. **Commit** — capture approved `snapshotId` for export.
5. **Lighting + cameras** in their own tx — `light.create`, `camera.create`.
6. **Render** — `job.submit kind=RENDER_STILL` per camera, `job.status` to poll.
7. **Export** — open a new tx, commit (gives a fresh `snapshotId`), then `export.file` with that
   snapshotId. **Do not pass `format`** — session-launch fixed it; passing it returns
   `INVALID_ARGUMENT`.

### 3. Dream-loop iteration (per round)

```
[LLM-driven edit via blender-mcp]
            ↓
[scene.screenshot]              ← inside the same tx as the edit
            ↓
[commit → approved snapshotId]
            ↓
[VLM critic: target vs current, returns score + diff + next_prompt]
            ↓
[thread sceneRevision through next round]
            ↓ loop until score ≥ 0.9 or max_rounds
```

The orchestrator (`scripts/dream_loop.py`) implements all of this. Pluggable critic via
`CRITICS = {"stub": ..., "vlm": ...}`.

### 4. Run the orchestrator

```bash
python3 scripts/dream_loop.py \
    --harness-cli <plugin>/scripts/harness_cli.py \
    --descriptor <descriptor.json> \
    --target-image ./qingming_target.png \
    --initial-prompt "Build a tiny riverside pavilion." \
    --max-rounds 5 \
    --output-dir ./out \
    --critic {stub,vlm}
```

### 5. Verify outputs

| Check | Expected |
|---|---|
| `--output-dir/round-NN/screenshot.png` exists | One per round |
| `critic.json` per round | Score + diff + next_prompt |
| `dream_loop.log` | Round-by-round progression |
| Scene revision monotonically increased | Threading works |
| Final `qm-v1.glb` exists + `file qm-v1.glb` reports "glTF binary model" | export succeeded |
| Local `shasum -a 256` matches `result.artifact.sha256` | producer didn't lie |

### 6. Close the session

```bash
# Best effort: SIGTERM the pid from the descriptor's `pid` field.
# Escalate to SIGKILL if needed.
kill -TERM <pid>
rm <descriptor.json> <descriptor.sock>   # session-private artifacts
```

User artifacts inside `--output-root` are retained.

## 验证与交付证据（Validation）

`scripts/lint_skills.py` must pass for the package itself. For per-round work, the orchestrator
writes `critic.json` and a round-screenshot per round. For final export, the harness returns
`result.artifact.validation.status: passed` (checks: `exists`, `non_empty`, `sha256`). Command
success alone is NOT design acceptance — verify the round's screenshot against the target via
the critic before declaring convergence.

Bindings:

- Each transaction's `snapshotId` + `sceneRevision` + `changedObjects` + `warnings` is the
  audit trail for that phase.
- `result.artifact.sha256` from `export.file` MUST equal the local `shasum -a 256` of the
  exported file — do not trust the producer's declared hash alone.
- The orchestrator's `dream_loop.log` is the trace of which prompt drove each round.

## Rules 与能力边界（不适用场景）

- This skill is **not** the Blender MCP bridge itself. Pick PartMe / Codex / ahujasid and use
  that ecosystem's `mcp-setup` skill.
- This skill is **not** an LLM driver. Wire your own (豆包 / Claude / OpenAI / Doubao Seed 2.1 Pro)
  at the orchestrator level (`critic_vlm()` in `dream_loop.py`).
- This skill is **not** `dream-loop` framework itself. The bundled `dream_loop.py` is a thin
  reference, not a fork of `achimala/dream-loop`.
- This skill does **not** ship web frontend (Three.js / R3F). The tutorial's "click NPC, third-
  person roam" layer is outside this skill's scope — handle in a separate web project after
  `qm-v1.glb` export.
- Do not install Blender, enable Add-ons, or change MCP configuration without the user's
  authorization (per `blender-mcp-setup` contract).
- Do not commit skill code into `full-aigc-skills/` (catalog only); this skill ships in
  `full-aigc-skills-repositories/blender-skills/`.

## Gotchas（常见问题与恢复）

- **`blender_auto_setup` false-positive.** Symptom: "Blender 正在运行" but `ps aux | grep
  blender` shows no real Blender GUI. Root cause: `pgrep -f Blender` matches
  `blender_mcp_server.py` stale processes. Recovery: skip auto_setup, call `launch_harness.py`
  directly.
- **`transactionId` must be non-empty for ALL requests.** SKILL.md claims "read commands don't
  need tx"; the harness disagrees. Use `tx="READ"` for read-only commands.
- **`export.file` rejects `format` field.** `INVALID_ARGUMENT: unknown argument fields:
  ['format']`. Format is fixed at session launch.
- **`expectedSceneRevision` is moving.** Send what the previous response said, not what you
  think it is. `STALE_SCENE_REVISION` is retryable; threading by hand is the safer habit.
- **`transaction.begin` echoes your `transactionId`** — it does not generate one. Use a fresh
  unique id per logical phase (`tx-qm-build-001`, `tx-qm-lighting-001`, `tx-qm-export-001`).
- **`scene.screenshot` result has no `sceneRevision` field.** Read it from the prior modify
  response, not from screenshot.
- **Path outside `--output-root`** → `OUTPUT_NOT_AUTHORIZED`. Move outputs inside.
- **`STALE_SCENE_REVISION` may succeed-and-report-fail** in edge cases — re-verify with
  `scene.inspect` to confirm the change landed before retrying.
- **Disk reservation `max(20% 卷容量, 20GB)`** can silently reject long jobs. Pre-check disk
  before `job.submit kind=RENDER_ANIMATION_FRAMES`.

See `references/pitfalls.md` for the verified evidence behind these eight.