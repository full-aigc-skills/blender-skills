---
name: blender-sequence-editing
description: Assemble editable Blender VSE timelines from images, image sequences, scenes, movies, text, and sound, including timing, speed, transitions, audio fades, compositor modifiers, and verified local output.
---

# Blender sequence editing

Use approved local media and explicit frame, channel, resolution and FPS requirements. Choose IMAGE_SEQUENCE for numbered rendered frames, SCENE for an editable Blender scene, and TEXT for local titles or captions. Place strips on deliberate channels, trim with final frame bounds, and overlap clips only for an intended transition.

Use CROSS, GAMMA_CROSS or WIPE only on overlapping visual strips. SOUND_CROSSFADE is implemented as opposing volume keyframes because Blender 5.2 does not expose it as an Effect Strip. Set speed through a SPEED strip and use a compositor modifier only with an existing CompositorNodeTree group.

Before export, inspect strip names, types, channels and frame ranges. For long or restartable output, render a durable frame sequence and submit COMPOSE_VIDEO. Probe the resulting MP4 for dimensions, frame rate, duration and required audio stream, then reopen the `.blend` to verify editability.

This Skill edits a supplied timeline; it does not create story structure, authorize external publishing or replace a dedicated audio-mixing workflow.
