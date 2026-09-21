# Original video shot-planning contract

## Required plan fields

Write one row per shot or continuous action interval:

| Field | Meaning |
|---|---|
| id | stable identifier retained through revisions |
| frames | inclusive integer start/end at project FPS |
| roles | subject and prop ids present in the interval |
| action | preparation, action, contact/trigger, follow-through, settle |
| camera | size, lens intent, position/path, aim target, motion quality |
| environment | anchors required for scale, contact, occlusion, or parallax |
| acceptance | observable checks and representative frames |

Shot durations must sum to the project duration exactly. Keep cause before result: approach before
contact, contact before reaction, button touch before light, release before free flight, and impact
before camera shake.

## Defaults

When the user gives no delivery settings, choose a reversible project baseline appropriate to the
concept and machine. Record every default in the plan. Do not bake one genre, 8-second duration,
1080p, or 24 fps into unrelated requests as though the user requested it.

## Scope control

Prefer one readable action chain over many underdeveloped beats. Preserve the user's required
subjects and ending state. Treat costume, photoreal materials, sound, and visual effects as
separate scope unless explicitly requested.
