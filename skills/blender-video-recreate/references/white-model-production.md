# White-model production contract

## Editable scene

Use stable object and role names, explicit frame ranges, one continuous object per persistent prop,
and articulated proxies or rigs when limb movement matters. Keep scene units, output root, camera,
and render settings explicit. Preserve an initial snapshot before mutation.

## Animation invariants

- Convert timestamps to project frames consistently and keep shot totals exact.
- Drive locomotion from the root while feet and limbs animate relative to it.
- Opposing gait means left leg/right arm and right leg/left arm advance together.
- Minimize planted-foot world drift during contact.
- For grip/release/catch, animate one prop and constraint influence; preserve visible free flight.
- Let impacts accumulate through follow-through. Do not return the receiver to a neutral pose
  between sequential contacts unless the reference does.
- Keep controlled handheld response parameterized: impact reaction begins at impact, not before it,
  and repeated hits must not reuse an identical shake waveform.

## Preview and persistence

Render the entire target interval at low cost before final output. Inspect playback and adjacent
frames around transitions, contacts, release/catch, camera turns, and the ending. For restartable
renders, prefer a frame sequence before MP4 encoding. Probe the final dimensions, FPS, frame count,
duration, and decodability; save and reopen the `.blend` when persistence is part of acceptance.
