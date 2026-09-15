---
name: blender-simulation
description: Configure and validate Blender rigid-body, collision, cloth, soft-body, smoke, point-cache, and fluid-cache workflows.
---

# Blender simulation

Declare active/passive roles, collision shapes, physical parameters, frame range and approved cache location. Verify object scale and collision proxies before simulation.

Use `blender-background-jobs` with `BAKE_POINT_CACHES` for expensive baking. Query the terminal receipt, reopen the baked project, and check physical measurements plus visual behavior. Cache paths must stay inside the job directory.

Free or invalidate caches before parameter changes. Never auto-retry an interrupted bake, and do not require cross-device byte identity. Low-resolution fixtures prove the workflow, not film-quality fluid or cloth.
