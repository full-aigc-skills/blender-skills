# Blender Simulation recovery example

For a failed or interrupted operation:

1. Stop further mutation and preserve the failing receipt or error.
2. Compare the current scene revision with the operation's expected revision.
3. Classify the cause as missing input, unsupported capability, validation failure, or user takeover.
4. Recover only the affected transaction or artifact; do not overwrite later user work.
5. Re-run the same validation and report both the original failure and recovery evidence.
