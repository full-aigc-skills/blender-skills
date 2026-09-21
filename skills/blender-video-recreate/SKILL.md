---
name: blender-video-recreate
description: Reconstruct a readable reference video's observable shots, articulated action, contacts, and camera motion as an editable Blender white-model video, then optionally prepare or run an authorized model-video handoff. Use for reference-video recreation, not prose-only original previs or simple video editing.
---

# Blender reference-video recreation

Recreate what can be observed: timing, framing, screen-space motion, contacts, camera path,
and action continuity. Do not pass the source video through a style filter and call that a 3D
reconstruction. Monocular footage does not uniquely determine depth or hidden geometry; label
estimates and optimize them for the approved camera views.

## 什么时候使用（When to Use）

Use when the user supplies a readable video or bounded clip and wants its action, staging, or
camera movement rebuilt as an editable Blender white model. Do not use for a prose-only concept,
look development on an existing approved animation, or VSE-only editing.

## 输入与前置条件（Prerequisites）

- A locally readable or explicitly authorized reference video, target time range, desired changes,
  output root, and acceptance priorities.
- A Blender control route capable of scene inspection and mutation. If unavailable, report the
  missing route; installing or enabling one is a separate action.
- A declared frame rate and delivery size. Preserve source timing by default; do not silently
  retime it to convenient frame counts.
- Read [reference-analysis.md](references/reference-analysis.md) before inferring the shot table.
  Read [white-model-production.md](references/white-model-production.md) before scene mutation.
- Read [generation-handoff.md](references/generation-handoff.md) only when downstream model-video
  generation is in scope.

## 执行流程（Workflow）

Step 1. Probe the actual media and extract representative frames around shot boundaries, action
beats, contacts, occlusions, and camera-direction changes. If the media cannot be decoded, stop
instead of reconstructing from its title or description.

Step 2. Produce `shot-plan.md` with source timestamps and exact project frames. Record per shot:
composition, subject scale and screen position, environment anchors, articulated action beats,
prop state, contact order, camera intent, observed facts, and estimates.

Step 3. Establish scale, floor, stable subject ids, one object for each continuous prop, and an
editable articulated proxy or rig. For domain work, hand off by installed skill name:

- `blender-scene-assembly` for objects and collections;
- `blender-character-rigging` and `blender-character-animation` for articulated performance;
- `blender-cinematography` for lens, framing, path, and handheld response;
- `blender-quality-validation` for contacts, floor penetration, gait, prop handoff, and visibility.

Install missing domain skills with
`npx skills add full-aigc-skills/blender-skills --skill <skill-name>`; never depend on sibling
relative paths.

Step 4. Block coarse action and camera first, then refine contacts and transitions. Recreate the
source action order and cumulative imbalance rather than resetting the character after every hit
or beat. Keep effects, textures, sound, and final styling out of white-model acceptance unless the
user explicitly includes them.

Step 5. Render a cheap complete preview. Compare source and reconstruction at representative
frames and motion intervals using [acceptance-checklist.md](references/acceptance-checklist.md).
Correct bounded timing, composition, sliding, same-side gait, penetration, prop discontinuity, or
camera loss; do not use aesthetic differences to excuse geometric or temporal errors.

Step 6. Save the editable `.blend`, white-model video, `shot-plan.md`, `comparison.md`, and
acceptance record. If authorized generation is requested, prepare `prompts.md`, choose an actually
available provider route, and keep its result acceptance separate from Blender acceptance.

## 验证与交付证据（Validation）

Return an evidence packet containing source hash and probed properties, target segment, project
FPS/frame range, Blender scene and preview paths, inspected intervals, representative frame pairs,
measured validation results, unresolved estimates, and artifact hashes. Use `PASS`, `FAIL`, or
`UNVERIFIED` per layer: media analysis, Blender structure, motion/contact, camera/composition,
encoding, and optional generated video. A successful encode is not motion approval.

Use [examples/validation.md](examples/validation.md) for the minimum result shape.

## Rules 与能力边界（不适用场景）

- Do not claim exact 3D recovery from one view or invent unreadable action.
- Do not replace articulated characters with sliding single primitives when limb motion or contact
  order is part of acceptance.
- Do not overwrite the only source or approved `.blend`; save a new version or transaction.
- Do not upload reference media, incur a charge, or submit a remote task without the required
  authorization and budget envelope.
- Windows foreground Blender and real paid-provider behavior remain `UNVERIFIED` until tested in
  that environment; portable instructions are not runtime proof.

## Gotchas（常见问题与恢复）

- Ambiguous depth: match screen-space landmarks and parallax, then document the chosen depth.
- Foot sliding or same-side gait: fix root speed, planted-foot intervals, and opposing limb phase.
- Prop teleport at release/catch: retain one prop and verify world transforms before/after the
  constraint switch.
- Camera looks smooth but misses contact: validate visibility at the exact impact frames.
- Remote timeout: query the stored task id; never resubmit merely because the client timed out.
- Repeated defect after two bounded repair rounds: preserve the best version and report the exact
  interval and remaining deviation instead of looping indefinitely. See
  [examples/recovery.md](examples/recovery.md).
