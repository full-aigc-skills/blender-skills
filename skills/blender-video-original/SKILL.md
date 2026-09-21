---
name: blender-video-original
description: Turn a prose video concept into a timed, editable Blender white-model scene with articulated action, camera motion, preview evidence, and an optional authorized model-video handoff. Use for original concepts without a required reference-video reconstruction.
---

# Blender original white-model video

Convert prose into an executable shot contract, then build and validate an editable Blender white
model before spending time or money on final styling. A mood image may guide appearance; if a video
must be followed for action or camera timing, use `blender-video-recreate` instead.

## 什么时候使用（When to Use）

Use for an original short, one-take action, product beat, scene concept, or story moment that needs
3D blocking, articulated motion, camera timing, and a white-model preview. Do not use for editing
existing clips or for rebuilding a supplied reference video's observable movement.

## 输入与前置条件（Prerequisites）

- A concept, required subjects/actions, output root, and explicit must-preserve/forbidden elements.
- Duration, FPS, dimensions, aspect ratio, and shot structure when specified. If absent, select
  reversible defaults and label them in `shot-plan.md`; defaults are not user requirements.
- A Blender control route capable of scene inspection and mutation. Missing tools do not authorize
  installation or a substitute provider.
- Read [shot-planning.md](references/shot-planning.md) before mutation and
  [white-model-production.md](references/white-model-production.md) before animation.
- Read [generation-handoff.md](references/generation-handoff.md) only when downstream generation is
  in scope.

## 执行流程（Workflow）

Step 1. Create `shot-plan.md` with stable shot ids, integer frame intervals, role ids, environment
anchors, action beats, contact/trigger events, camera intent, ending state, and documented defaults.
Cause must precede effect; allocate preparation, action, follow-through, and settling time.

Step 2. Build scale, floor, environment masses, articulated characters, persistent props, and the
delivery camera. Hand off domain work by installed Skill name:

- `blender-scene-assembly` for scene structure;
- `blender-character-rigging` and `blender-character-animation` for bodies and props;
- `blender-cinematography` for framing and motion;
- `blender-quality-validation` for measurable acceptance;
- `blender-render-compositing` and `blender-sequence-editing` for approved output.

Install a missing dependency with
`npx skills add full-aigc-skills/blender-skills --skill <skill-name>`; do not assume sibling files
exist after a granular install.

Step 3. Animate in dependency order: root motion and balance, planted feet, opposing limbs,
interaction contacts, prop constraints/free flight, gaze, secondary motion, then camera response.
Keep one persistent object for a prop across grip, release, flight, catch, and recovery.

Step 4. Render a cheap full-duration preview and inspect the intervals listed in
[acceptance-checklist.md](references/acceptance-checklist.md). Repair bounded defects without
rebuilding unrelated approved work. Technical validation and visual review are both required.

Step 5. Save the editable `.blend`, white-model preview, `shot-plan.md`, prompt package, and
acceptance record. Stop here when the user asks only for a white model.

Step 6. If authorized model-video generation is requested, discover the actual provider
capability, bind upload consent and budget, submit at most the authorized request, persist its task
id, and validate its result independently from the white model.

## 验证与交付证据（Validation）

Record assumptions, scene revision/snapshot, project FPS and exact frame range, role/object map,
action intervals, measured gait/contact/floor/camera results, inspected playback ranges, preview
and `.blend` hashes, encoding properties, and remaining risks. Status each layer separately as
`PASS`, `FAIL`, or `UNVERIFIED`; use [examples/validation.md](examples/validation.md).

## Rules 与能力边界（不适用场景）

- Do not silently add characters, shots, props, or narrative events that contradict the concept.
- Do not use a sliding rigid placeholder when articulated action is an acceptance target.
- Do not treat a successful render, keyframe count, or tool response as proof of good motion.
- Do not upload, publish, install, charge, or overwrite without the authority required for that
  action.
- Windows foreground Blender and real paid-provider behavior remain `UNVERIFIED` until exercised;
  local macOS evidence cannot be generalized to them.

## Gotchas（常见问题与恢复）

- Too many beats for the duration: simplify or lengthen the plan before animation; do not compress
  contacts until they become unreadable.
- Same-side gait or sliding: correct phase, root speed, step length, and foot-lock intervals.
- Trigger occurs early: drive the effect from the verified contact frame, not an approximate beat.
- Camera interpolation overshoots: inspect adjacent frames and adjust handles/path timing.
- Encoded video is valid but performance is not: keep encoding PASS and motion FAIL/UNVERIFIED.
- Two bounded repairs fail: preserve the best version, report the exact interval, and follow
  [examples/recovery.md](examples/recovery.md).
