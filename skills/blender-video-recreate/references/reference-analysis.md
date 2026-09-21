# Reference analysis contract

## Probe before interpretation

Record the source SHA-256, duration, frame rate, frame count, dimensions, rotation metadata, codec,
and audio presence using available local media tools. Preserve source timestamps independently of
the project frame rate. If variable frame rate or damaged frames make exact conversion uncertain,
record that uncertainty and derive frames from timestamps rather than assuming a constant index.

## Observation table

For each shot or continuous take, capture:

| Field | Required evidence |
|---|---|
| Time | source start/end timestamps and project frame interval |
| Composition | shot size, subject screen position/scale, horizon, dominant lines |
| Space | floor, anchors, relative distance, visible parallax |
| Action | preparation, main action, contact, follow-through, recovery |
| Prop | identity, grip/release/catch state, trajectory, orientation |
| Camera | static/pan/tilt/dolly/orbit/handheld, direction, acceleration |
| Certainty | observed, inferred, or occluded |

One source frame cannot prove acceleration, foot locking, or a contact sequence. Inspect adjacent
frames around every important beat. Extracting thumbnails is preparation, not acceptance evidence.

## Reconstruction priorities

Prefer, in order: event timing and contact order; camera-relative silhouette and position; subject
scale; parallax and camera movement; hidden geometry. When constraints conflict, preserve the
user's stated priority and document the compromise in `comparison.md`.
