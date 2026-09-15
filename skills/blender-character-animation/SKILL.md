---
name: blender-character-animation
description: Animate a registered Blender character rig and a single interactive prop with editable timing, IK controls, constraints, and continuity checks.
---

# Character and prop animation

Work from named action beats and frame intervals. Pose controls or bones, key only intended channels, and retain editable constraints. For grip/release/catch, use one prop object: keep grip influence at one before release, zero through a visible free-flight interval, and restore it only after the prop reaches the catch pose.

Inspect the release distance and duration, catch position/rotation discontinuity, planted foot drift, limb-length preservation and floor proxies. A passing numeric check is necessary but not sufficient: also review silhouette, balance, contact readability and camera composition.

Use `blender-quality-validation` for measurements and `blender-cinematography` when
the task includes camera paths, focus or handheld behavior. Keep those acceptance decisions
separate from pose authoring.

When timing changes, move the release/apex/catch parameters or keyframes without rebuilding unrelated animation. Do not add skin detail, effects, sound or downstream rendering to a white-model task unless separately requested and supported.
