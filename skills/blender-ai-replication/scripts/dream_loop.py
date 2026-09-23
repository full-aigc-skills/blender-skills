#!/usr/bin/env python3
"""
dream_loop.py — orchestration loop on top of blender-harness.

Reads a target image + initial prompt, drives a Blender session through
N rounds of: build/edit → screenshot → VLM critic → diff prompt. The
critic is pluggable; default `stub` lets the loop run end-to-end without
an API key so you can validate harness/transaction wiring first.

Usage:
    python3 dream_loop.py \\
            --descriptor <descriptorPath from launch_harness.py> \\
            --target-image ./qingming_target.png \\
            --initial-prompt "Build a tiny riverside pavilion." \\
            --max-rounds 5 \\
            --output-dir ./out \\
            --critic {stub,vlm}

Prereqs:
  * blender-harness session running (see blender-mcp-setup SKILL.md).
  * harness_cli.py reachable at --harness-cli.
  * For --critic vlm: a real VLM client wired into `critic_vlm()`.
"""

import argparse
import json
import subprocess
import time
from pathlib import Path


def harness_send(descriptor, command, arguments, scene_rev=None):
    """One closed-envelope JSON request via harness_cli.py.

    Read-only commands (`*.inspect`, `capability.*`, queries) pass empty
    tx_id / scene_rev. Rewrite commands must be preceded by a
    `transaction.begin`; the caller threads tx_id + expected scene_rev.
    """
    payload = {
        "protocolVersion": "codex-blender/v1",
        "sessionId": "placeholder",
        "requestId": f"req-{int(time.time() * 1000)}",
        "transactionId": "",
        "command": command,
        "arguments": arguments,
    }
    if scene_rev is not None:
        payload["expectedSceneRevision"] = scene_rev

    req_file = Path("/tmp") / f"{payload['requestId']}.json"
    req_file.write_text(json.dumps(payload))
    try:
        proc = subprocess.run(
            ["python3", HARNESS_CLI, "--descriptor", str(descriptor),
             "--request", str(req_file)],
            capture_output=True, text=True, timeout=120,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"harness_cli exited {proc.returncode}: {proc.stderr}")
        resp = json.loads(proc.stdout)
        if resp.get("status") != "succeeded":
            err = resp.get("error", {})
            raise RuntimeError(f"{command} failed: {err}")
        return resp["result"]
    finally:
        req_file.unlink(missing_ok=True)


def begin_tx(descriptor):
    """Open a transaction. Returns (tx_id, scene_revision)."""
    r = harness_send(descriptor, "transaction.begin", {})
    return r["transactionId"], r["sceneRevision"]


def commit_tx(descriptor, tx_id):
    """Commit a transaction. Returns the approved snapshot_id."""
    r = harness_send(descriptor, "transaction.commit", {}, tx_id=tx_id)
    return r["snapshotId"]


def round_apply_and_capture(descriptor, tx_id, scene_rev, prompt, shot_path):
    """Apply prompt-driven edits + capture a screenshot, all inside one tx.

    The actual `object.create_mesh` / `material.create_pbr` calls driven
    by `prompt` belong here; this stub just screenshots the current scene.
    Replace `_apply_prompt_body` with your LLM-driven edit planner.
    """
    args = {"path": str(shot_path), "width": 1024, "height": 1024}
    r = harness_send(descriptor, "scene.screenshot", args,
                     tx_id=tx_id, scene_rev=scene_rev)
    return r["sceneRevision"]


# ---- VLM critic (pluggable) ----------------------------------------

def critic_stub(target, current, prompt):
    """No-op critic. Demonstrates the loop without an API call."""
    return {
        "score": 0.5,
        "issues": ["stub critic — wire critic_vlm() for real feedback"],
        "next_focus": "Roof tiles too uniform; vary color across the span.",
        "next_prompt": f"{prompt} Vary roof tile color across the span.",
    }


def critic_vlm(target, current, prompt):
    """Real VLM critic — call doubao-seed-2-1-pro vision or OpenAI vision.

    Return a dict with keys: score, issues, next_focus, next_prompt.
    """
    raise NotImplementedError("Wire your VLM here (Volcengine Ark / OpenAI)")

CRITICS = {"stub": critic_stub, "vlm": critic_vlm}


# ---- main loop ------------------------------------------------------

def dream_loop(descriptor, target_image, initial_prompt, max_rounds,
               output_dir, critic_name):
    critic = CRITICS[critic_name]
    output_dir.mkdir(parents=True, exist_ok=True)
    log_path = output_dir / "dream_loop.log"
    log = log_path.open("a", encoding="utf-8")
    log.write(f"== start == target={target_image} prompt={initial_prompt}\n")

    prompt = initial_prompt
    for r_idx in range(max_rounds):
        rdir = output_dir / f"round-{r_idx:02d}"
        rdir.mkdir(exist_ok=True)
        shot = rdir / "screenshot.png"

        tx_id, scene_rev = begin_tx(descriptor)
        try:
            scene_rev = round_apply_and_capture(
                descriptor, tx_id, scene_rev, prompt, shot,
            )
            commit_tx(descriptor, tx_id)
        except Exception as exc:
            log.write(f"[round {r_idx}] tx failed: {exc}\n")
            raise

        diff = critic(target_image, shot, prompt)
        diff["round"] = r_idx
        (rdir / "critic.json").write_text(json.dumps(diff, indent=2))
        log.write(f"[round {r_idx}] score={diff['score']} focus={diff['next_focus']}\n")
        print(f"[round {r_idx}] score={diff['score']}  →  {diff['next_focus']}")
        if diff["score"] >= 0.9:
            print("converged.")
            break
        prompt = diff["next_prompt"]

    log.write("== end ==\n")
    log.close()


def main():
    global HARNESS_CLI
    p = argparse.ArgumentParser()
    p.add_argument("--harness-cli", required=True,
                   help="path to <plugin>/scripts/harness_cli.py")
    p.add_argument("--descriptor", required=True, type=Path)
    p.add_argument("--target-image", required=True, type=Path)
    p.add_argument("--initial-prompt", required=True)
    p.add_argument("--max-rounds", type=int, default=5)
    p.add_argument("--output-dir", type=Path, default=Path("./out"))
    p.add_argument("--critic", choices=list(CRITICS), default="stub")
    args = p.parse_args()

    HARNESS_CLI = args.harness_cli
    dream_loop(args.descriptor, args.target_image, args.initial_prompt,
               args.max_rounds, args.output_dir, args.critic)


if __name__ == "__main__":
    main()
