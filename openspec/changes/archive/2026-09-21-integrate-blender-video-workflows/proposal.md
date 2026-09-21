## Why

The shared Blender skill package has strong domain skills for animation, cinematography, rendering, sequencing, and validation, but lacks a user-facing workflow that turns either a reference video or a prose concept into an editable white-model video package. The MIT-licensed `modengsir/blender-video-workflows` project provides a useful starting point that should be adapted to the package's existing capability boundaries and evidence requirements instead of copied as a second execution stack.

## What Changes

- Add `blender-video-recreate` for observable reference-video analysis, articulated white-model reconstruction, comparison, and optional authorized downstream video generation.
- Add `blender-video-original` for prose-to-shot-plan, articulated white-model animation, preview validation, and optional authorized downstream video generation.
- Route modeling, animation, camera, render, sequence, and quality work to the existing independently installable Blender skills by name and install command.
- Add self-contained production and generation references for granular single-skill installs.
- Add package metadata, bilingual catalog documentation, validation coverage, upstream attribution, and a minor package version bump.

## Capabilities

### New Capabilities

- `reference-video-recreation`: Analyze a readable reference clip and deliver an editable, evidence-backed Blender white-model recreation plus an optional authorized generation handoff.
- `original-white-model-video`: Turn a prose concept into an editable, evidence-backed Blender white-model video package plus an optional authorized generation handoff.

### Modified Capabilities

None.

## Impact

- Adds two skill directories under `skills/` and two manifest entries.
- Updates package READMEs, changelog, license attribution, tests/lint expectations, and package version.
- Does not add an MCP command, provider client, Blender add-on, model credential flow, or paid-submission bypass.
- Consumer plugins can adopt the new immutable package release through their existing lock-and-sync process.
