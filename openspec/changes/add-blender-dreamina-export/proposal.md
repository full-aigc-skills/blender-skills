## Why

The Blender package can create and export a white-model video but lacks instructions for installing and using the official Jimeng Seedance 2.5 uploader. Users need one installable skill that covers both the camera-render and existing-video routes through to an observable reference input on the Jimeng website.

## What Changes

- Add `blender-dreamina-export` with official uploader setup, two export routes, and separate local/link/web acceptance states.
- Add camera-render and local-video examples; register the skill in the package manifest and catalogs.
- Preserve the distinct purpose of `blender-mcp-setup` and existing white-model authoring skills.
- Add a named handoff from both video-authoring skills to the new official uploader skill.

## Capabilities

### New Capabilities

- `blender-dreamina-reference-export`: Guide authorized official uploader installation and verify the handoff of a Blender white-model video into Jimeng's web reference input.

## Impact

Skill source and package metadata only. No vendor ZIP is redistributed, no automated upload API is asserted, and no paid generation is included.
