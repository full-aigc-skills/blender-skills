# Verified Pitfalls (smoke-test 2026-09-23)

Each pitfall was reproduced against the live PartMe plugin cache v0.14.1 session (`smoke-test-001`, pid 39727, descriptor on Unix socket).

## 1. `blender_auto_setup` false-positive on stale MCP servers

**Symptom**: `blender_auto_setup` returns `ok: false, stage: enable, manualHint: "检测到 Blender 正在运行..."`, but `ps aux | grep blender` shows no actual Blender GUI process.

**Root cause** (verified by reading `scripts/auto_setup.py:73-87`):
```python
def blender_running() -> bool:
    pattern = "Blender" if sys.platform == "darwin" else "blender"
    out = subprocess.run(["pgrep", "-f", pattern], ...)
    return bool((out.stdout or "").strip())
```

`pgrep -f Blender` matches any process whose command line contains "Blender" — including:
- `/Users/wandl/Library/Caches/PartMe/BlenderDesign/runtime/0.7.0-rc.2/venv/bin/python .../blender_mcp_server.py` (9+ stale instances)
- `mcp_bootstrap.mjs` (Node bootstrap scripts)

Since the harness has been running across multiple plugin versions, dozens of stale `blender_mcp_server.py` processes accumulate. Each one matches `Blender`, so the detector believes Blender is running.

**Workaround** (do NOT kill the MCP servers — they are your bridge to this MCP):
```bash
# 1. Skip auto_setup entirely
# 2. Call launch_harness.py directly — it does the same launch logic minus the running check
python3 ~/.zcode/cli/plugins/cache/full-aigc-plugins/blender-design/0.14.1/scripts/launch_harness.py \
    --session-id "qingming-v1" \
    --output-root "/Users/wandl/partme/blender/design-outputs" \
    --execution-mode "auto_with_budget" \
    --export-format "glb"

# 3. Use harness_cli.py to send commands — no MCP layer needed
python3 ~/.zcode/cli/plugins/cache/full-aigc-plugins/blender-design/0.14.1/scripts/harness_cli.py \
    --descriptor <descriptor.json> \
    --request <req.json>
```

**Proper fix** (upstream issue): the detector should anchor on `/Applications/Blender.app/Contents/MacOS/Blender` specifically, or use `launchctl print user/$(id -u)` to check registered GUI apps. Filed mentally; not in this skill.

---

## 2. `transactionId` must be non-empty for ALL requests

**Symptom**: Sending `transactionId: ""` for `capability.list` returns `INVALID_REQUEST: transactionId must be a non-empty string`.

**Resolution**: The SKILL.md says "read commands don't need transactionId", but the harness contract is stricter. Use a sentinel:
```json
{"transactionId": "READ"}    // for capability.list / scene.inspect / scene.screenshot when reading only
{"transactionId": "EXPORT"}   // for export.file
```

For modify commands, use the `transactionId` returned by `transaction.begin`.

---

## 3. `export.file` rejects `format` field

**Symptom**: `INVALID_ARGUMENT: unknown argument fields: ['format']`

**Resolution**: `format` is fixed at session launch (`launch_harness.py --export-format glb`). The command itself only takes `path` + `snapshotId`:
```json
{
  "command": "export.file",
  "arguments": {
    "path": "/.../qm-v1.glb",
    "snapshotId": "<from transaction.commit>"
  }
}
```

Sending the rejected payload got the user the validation gate that the harness was supposed to enforce. **This is the gate working as designed** — it surfaces undocumented arg fields before silently writing the wrong thing to disk.

---

## 4. `expectedSceneRevision` is a moving target

**Symptom**: Sending `expectedSceneRevision: 0` after the server is already at `sceneRevision: 1` returns `STALE_SCENE_REVISION` (retryable).

**Resolution**:
- Read the response's `sceneRevision` field after every successful modify.
- Thread it into the next request's `expectedSceneRevision`.
- The harness contract is "you assert what you believe the current revision is; the server either accepts (and bumps) or rejects with retryable=true".

In the qingming sequence, sceneRevision walks: `1 → 2 → 3 → 4 → 5 → 11 → 14 → 17 → 25 → 26 → 27 → 28 → 29 → ...`. Threading by hand is tedious — the dream_loop script does it automatically.

---

## 5. `transactionId` echoed vs generated

**Observed behavior**: `transaction.begin` with `transactionId: "READ"` returns `result.transactionId: "READ"` (echoes the input).

**Implication**: The harness does not generate a new tx_id; whatever you send becomes the registered id. So:
- Don't send `"READ"` and then try to use it for a modify — `TRANSACTION_NOT_FOUND`.
- Always send a fresh unique id (e.g., `tx-qm-build-001`) for modify chains.
- Use a new tx_id per logical phase (build / lighting / export).

---

## 6. `scene.screenshot` return does NOT include `sceneRevision`

**Observed behavior**: `scene.screenshot` returns `{path, format, ...}` but no `sceneRevision` in `result`.

**Resolution**: For mid-transaction screenshots, you still need to know the sceneRevision going in. Read it from the response of the prior modify call, not from screenshot's result. The dream_loop script threads it correctly.

---

## 7. Disk reservation gate on long jobs

**Documented but not tested**: `job.submit kind=RENDER_ANIMATION_FRAMES` enforces `max(20% 卷容量, 20GB)` reservation; jobs that would exceed are **denied without spawning**. Symptom would be `DISK_RESERVE_EXCEEDED`. Always check disk before submitting high-sample renders.

---

## 8. `MATERIAL_INVALID` / `MEDIA_INVALID` on output

**Documented but not tested**: Export validation includes `format`/frame rate checks. Symptom: `MEDIA_INVALID` with actual reported values. Run `ffprobe` on the path first to confirm it matches the harness's expectations.

---

## Verification checklist

When this skill is used in production, the orchestrator should write a `verify.json`:
```json
{
  "session": "qingming-v1",
  "harness_revision": "<launch_harness.py version>",
  "addon_version": "<from providers.json>",
  "auto_setup_workaround_used": true,
  "rounds": [
    {"round": 0, "scene_rev": 25, "screenshot_sha256": "..."},
    ...
  ],
  "export": {
    "path": ".../qm-v1.glb",
    "sha256": "...",
    "ffprobe_ok": true
  }
}
```

Future replays of this skill can use the JSON to confirm which pitfalls were avoided.