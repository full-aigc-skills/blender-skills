# Original white-model production contract

## Build order

1. Establish units, floor, scale reference, environment masses, and approved camera bounds.
2. Create stable roles and articulated proxies or rigs; create one continuous object per prop.
3. Animate root motion and balance before limbs, contacts, prop states, and secondary motion.
4. Add camera movement after action timing is readable, then validate visibility at key beats.
5. Render the complete low-cost preview before final output.

## Motion invariants

- Opposing gait pairs each forward leg with the opposite arm.
- Root speed, step length, and planted-foot intervals must agree.
- Transitions into stopping, turning, reaching, impact, and recovery need visible easing and body
  inertia; characters must not snap between isolated poses.
- Grip/release/catch uses one prop with explicit constraint influence and visible free flight.
- Effects and reactions start from the verified event frame, not before it.
- Handheld response is bounded and event-specific; it may look effortful without losing the action.

## Preview and persistence

Inspect full playback plus adjacent frames at starts, stops, contacts, constraint switches, camera
turns, and the ending. Render restartable frame sequences for long output, then encode and probe
the media. Save the editable project and reopen it when persistence is required. Command success
alone is not artistic or motion acceptance.
