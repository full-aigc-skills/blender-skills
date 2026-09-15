---
name: blender-background-jobs
description: Run snapshot-isolated Blender exports, durable animation frame sequences, explicit frame recovery, verified video composition, still renders, and simulation baking without blocking the foreground scene.
---

# Blender background jobs

Use for `job.*` when an approved output root exists. A submission saves a versioned source snapshot first; the child Blender process may write only inside its job directory. The foreground may continue editing, but the job remains bound to the submitted snapshot.

Route by `kind`: EXPORT and RENDER_STILL also use `blender-render-compositing`; BAKE_POINT_CACHES also uses `blender-simulation`. Use RENDER_ANIMATION_FRAMES for a persistent PNG or multilayer EXR sequence. Use COMPOSE_VIDEO only after its source FrameSequenceReceipt has complete frame hashes; it produces a separate H.264 receipt without rerendering Blender.

Query status until a terminal receipt and keep the job ID, snapshot hash, manifest hash, and artifact receipt together. Cancellation terminates only the child task. `job.recover` may mark a lost task `interrupted` but never restarts it. Resume only after an explicit `job.resume`; verified frames remain untouched while missing or hash-invalid frames are replaced. A background receipt does not approve external upload, publishing, payment, or Video Factory orchestration.
