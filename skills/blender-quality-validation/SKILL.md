---
name: blender-quality-validation
description: Measure Blender geometry, character, prop, collision, motion, and camera acceptance criteria against explicit objects, frames, proxies, and tolerances.
---

# Blender quality validation

Use only explicit targets and intent supplied by the task: objects, armature bones, frame intervals, contact points, collision proxies and numeric limits. Do not infer every performance intention from scene geometry.

Run the relevant `validation.*` checks and return the measured value, affected object or bone, frame range, limit and pass/fail result. Character work commonly combines limb length, planted-foot drift, prop handoff and floor penetration; camera work adds visibility and motion-discontinuity checks.

Technical thresholds are necessary but do not replace visual review. After numeric checks, inspect silhouette, balance, contact readability and composition. If a check lacks a required proxy or frame interval, identify that exact missing input; do not silently broaden the target set.
