## ADDED Requirements

### Requirement: Each skill is independently actionable

Every published Blender skill SHALL define when it applies, required inputs and prerequisites, an ordered workflow, observable validation evidence, capability boundaries, and recovery guidance without depending on files outside that skill directory.

#### Scenario: Granular installation

- **WHEN** a user installs one Blender skill without its siblings
- **THEN** every referenced instruction or example required for that skill exists inside the installed skill directory
- **AND** handoffs to other skills use the target skill name and install command rather than a relative sibling path

### Requirement: Domain claims are evidence-bound

Every workflow SHALL distinguish command success from artifact or visual acceptance and SHALL identify the receipt, measurement, preview, save/reopen, or re-import evidence required for completion.

#### Scenario: A Blender command returns success

- **WHEN** an operation reports successful execution
- **THEN** the skill requires the domain-specific validation evidence before claiming completion
- **AND** missing evidence is reported as unverified rather than passed

### Requirement: Published skills pass deterministic gates

The package SHALL provide a deterministic lint check and SHALL require each skill to reach TRACE overall score 4.5 or higher before release.

#### Scenario: A skill regresses

- **WHEN** lint finds a missing required section or TRACE reports an overall score below 4.5
- **THEN** the release gate fails and identifies the affected skill
