# reference-video-recreation Specification

## Purpose
Provide a portable workflow that reconstructs the observable timing, staging, articulated action, and camera motion of a readable reference clip as an editable Blender white-model package with explicit evidence and limitations.
## Requirements
### Requirement: Reference evidence precedes reconstruction
The workflow SHALL inspect the actual reference media, record its technical properties, and distinguish observations from estimates before authoring the Blender scene.

#### Scenario: Readable reference clip
- **WHEN** the user supplies an accessible reference video and a target segment
- **THEN** the workflow produces a shot-and-action plan containing source timestamps, framing, subject motion, contacts, camera motion, and identified uncertainties

#### Scenario: Reference cannot be read
- **WHEN** the reference video cannot be accessed or decoded
- **THEN** the workflow reports the concrete blocker and SHALL NOT invent shots or claim a recreation was completed

### Requirement: Recreation remains editable and measurable
The workflow SHALL deliver an editable Blender scene and white-model preview whose timing, screen-space composition, contact sequence, and camera path can be compared with the source.

#### Scenario: White-model comparison
- **WHEN** a reconstruction preview is rendered
- **THEN** the workflow records comparison evidence for representative frames and motion intervals, including unresolved deviations and any estimated hidden geometry

### Requirement: Downstream generation preserves authorization boundaries
The workflow SHALL treat external video generation as an optional handoff that requires a compatible service, authorized reference upload, and an approved cost envelope when fees may be incurred.

#### Scenario: No authorized generation service
- **WHEN** the Blender package is complete but no compatible service or upload authorization is available
- **THEN** the workflow delivers the Blender scene, white-model preview, shot plan, comparison evidence, and prompt package with final generation marked `UNVERIFIED`

#### Scenario: Existing remote task is uncertain
- **WHEN** a submitted generation request times out or returns an uncertain state
- **THEN** the workflow queries the recorded task identifier and SHALL NOT create a duplicate paid submission
