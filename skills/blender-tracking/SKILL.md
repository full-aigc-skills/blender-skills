---
name: blender-tracking
description: Load approved footage, create normalized Blender tracking markers, solve a foreground camera, set up the scene, and validate reprojection error.
---

# Blender motion tracking

Load clips only from approved asset roots. Add named tracks with normalized coordinates and explicit frames. Confirm enough common tracks and meaningful parallax before solving.

Camera solve and scene setup require a foreground CLIP_EDITOR. Accept a solve only after inspecting bundle count and measured reprojection error against the task threshold; operator success alone is insufficient.

Preserve the original footage path and solved `.blend` receipt. Tracking does not imply masking or editing; combine with render-compositing or sequence-editing only when the task requests those outcomes.
