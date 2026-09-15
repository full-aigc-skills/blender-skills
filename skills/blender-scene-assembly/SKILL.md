---
name: blender-scene-assembly
description: Organize Blender scenes, collections, object identity, transforms, visibility, and authorized reusable assets without losing editability or provenance.
---

# Scene and asset assembly

Inspect the current scene and units first. Use stable object IDs for continued work while retaining names for human readability. Put functional groups and helper geometry in named collections; distinguish independent duplicates from linked-data instances. When parenting an already placed object, use world-preserving parenting unless local-space relocation is intentional.

Import or link only from approved asset roots. Choose append when the project must own editable data, and link when provenance and shared updates matter. Record source paths, imported object receipts and any missing dependency. Do not download assets, install import extensions, or infer third-party license rights.

Before delivery, verify collection membership, local/world transforms, visibility in viewport and render, stable IDs after rename, linked versus copied data, and successful save/reopen. A successful simple fixture import does not guarantee compatibility with every external FBX, OBJ or glTF producer; disclose untested format features.
