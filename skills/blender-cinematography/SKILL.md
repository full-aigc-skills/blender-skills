---
name: blender-cinematography
description: Design and validate Blender cameras, lenses, subject aiming, path motion, focus, framing, and controlled handheld response.
---

# Blender cinematography

Use for camera creation, lens choice, composition, path following, focus and handheld motion. Obtain the subject list, intended shot size, frame range and movement beats before changing the camera.

Create or select one delivery camera, aim it at an explicit point or object, then add path and handheld behavior only when required. Handheld noise must remain parameterized and visually subordinate to readable subject motion.

Run `validation.camera_visibility` over the specified frames and inspect camera plus orthographic previews. Report missed objects and frame ranges rather than claiming that a constraint or keyframe guarantees good composition. Camera work does not authorize rendering, export or downstream generation.
