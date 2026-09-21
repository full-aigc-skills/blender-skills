## Context

See `proposal.md` for motivation. The package already owns independently installable domain skills for scene assembly, character animation, cinematography, rendering, sequencing, and validation. The upstream MIT project offers useful orchestration language but duplicates production references and does not use this package's mandatory section structure, TRACE gate, granular-install discipline, or runtime evidence model.

The source package cannot assume that the `blender-design` plugin, PartMe Blender MCP, FFmpeg, or a video provider is installed. It must describe capability discovery and clean stopping points while allowing a consuming host to bind the workflow to its available tools.

## Goals / Non-Goals

**Goals:**

- Expose two discriminating, user-facing orchestration entry points.
- Preserve the useful upstream timing, gait, contact, render, and paid-task recovery guidance.
- Reuse existing domain skills by name while keeping each new skill independently installable.
- Produce observable local evidence before any optional external generation.

**Non-Goals:**

- Add or modify Blender MCP commands, provider SDKs, OAuth flows, or credentials.
- Guarantee monocular depth recovery, exact motion capture, or deterministic model-video output.
- Bundle the upstream repository verbatim or maintain duplicate copies of existing domain skills.

## Decisions

### Two workflow skills instead of one mode-heavy skill

`blender-video-recreate` and `blender-video-original` have different required inputs, failure states, and acceptance evidence. Separate descriptions improve automatic routing and let users install only the needed workflow. A single skill with a mode switch was rejected because its description would attract both reference-analysis and generic Blender animation requests.

### Orchestration over implementation duplication

The new skills own phase ordering, evidence, and stopping conditions. Domain execution is handed to the existing skills by stable skill name and documented install command. The references remain self-contained for a granular install but do not copy entire sibling instructions. Copying the upstream files unchanged was rejected because it would create a second Blender production standard and bypass current validation conventions.

### White-model acceptance is distinct from generated-video acceptance

The workflow records local Blender evidence and downstream model evidence separately. A successful white-model review cannot prove that a stochastic video provider preserved the action. This avoids propagating a local PASS into an unverified remote artifact.

### Minor package release and upstream attribution

The package moves from 23 to 25 public skills, so the manifest version advances from `1.0.2` to `1.1.0`. The repository retains Apache-2.0 for the adapted package and records the MIT upstream in `NOTICE` so the upstream copyright and license condition remain visible.

## Risks / Trade-offs

- [Risk] A granular installation lacks sibling domain skills. → Mitigation: every handoff names the required skill and its explicit `npx skills add` command, while the orchestration skill still explains the required outcome.
- [Risk] Users interpret a render receipt as artistic acceptance. → Mitigation: require playback or interval inspection and separate technical, motion, visual, and remote-generation states.
- [Risk] Reference-video depth and occluded action are overclaimed. → Mitigation: require observation-versus-estimate labeling and screen-space acceptance rather than false 3D ground truth.
- [Risk] Optional providers trigger uploads or charges unexpectedly. → Mitigation: require compatible capability discovery, upload authorization, cost envelope, stored task identifier, and query-before-retry semantics.

## Migration Plan

1. Add and validate both skills plus manifest, README, changelog, and NOTICE updates.
2. Publish immutable `v1.1.0` only after lint, TRACE, OpenSpec, and clean-install checks pass.
3. Let consumer plugins update their managed `skills.lock.json` through the existing release dispatch; do not edit vendored copies directly.
4. Roll back by pinning consumers to `v1.0.2`; no runtime or data migration is required.
