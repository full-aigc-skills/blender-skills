# Optional model-video handoff

## Capability and authorization gate

Inspect the current provider or companion Skill rather than inferring support from a model name.
Confirm whether it accepts video reference, motion control, first/last frames, or images only.
Images are a weaker motion constraint and must be reported as such.

Before transmitting media, bind all of:

- chosen provider and actual supported input;
- explicit authorization to upload the reference/preview;
- model, duration, ratio, and resolution;
- authoritative quote or an exact approved request;
- maximum cost and permission for one submission.

No available provider means the local Blender package and prompt handoff are still valid; remote
generation remains `UNVERIFIED`.

## Prompt package

`prompts.md` should state target appearance, timestamped action order, camera constraints,
structural invariants, and provider-supported negative constraints. It must tell the model to use
the white model for spatial, motion, and camera guidance without claiming pixel-exact control.

## Task recovery and result validation

Persist the remote task id immediately after submission. On timeout or unknown state, query that id
and do not create a second charge. Download only to an approved directory, hash the result, probe
its media properties, and compare the generated action and camera interval-by-interval with the
white model. A Blender PASS does not transfer to the generated result.
