---
name: blender-preview
description: "Capture fresh camera, front, side, and top Blender previews for milestone review or visual diagnosis."
---

# Blender Milestone Preview

Call `preview.capture` for the current revision and snapshot. Require camera/front/side/top PNGs;
animation also needs first/middle/last frames. Verify file existence and SHA-256 before display.

Never reuse images from an older revision. Describe visible strengths and defects, and bind user
approval to the exact `sceneRevision + snapshotId`.
