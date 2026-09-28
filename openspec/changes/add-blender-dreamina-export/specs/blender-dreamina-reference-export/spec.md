## ADDED Requirements

### Requirement: Official uploader installation is independently guided

The skill SHALL guide discovery, official ZIP installation, enabled-state checking, and Jimeng sidebar access without mistaking the Codex Blender Connector for the Jimeng uploader.

#### Scenario: Jimeng panel is absent

- **WHEN** the user requests a Blender-to-Jimeng export but the Jimeng panel is absent
- **THEN** the skill checks the official add-on installation and enabled state before attempting export

### Requirement: Both official video routes are supported

The skill SHALL support camera rendering from the Blender scene and selection of an already-rendered local white-model video.

#### Scenario: Local video already exists

- **WHEN** the user supplies a valid existing white-model video
- **THEN** the skill selects the local-upload route without requiring another Blender render

### Requirement: Web reference handoff is independently verified

The skill SHALL report local media, uploader link, web navigation, and reference-video loading as distinct results; it SHALL NOT infer paid generation from any of them.

#### Scenario: Link appears but reference is not observed

- **WHEN** the uploader produces a link but the Jimeng web input cannot be inspected
- **THEN** the skill reports link creation and marks reference loading unverified
