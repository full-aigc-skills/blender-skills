# Blender Sculpt Surface validation example

Return a compact evidence packet after the workflow:

```yaml
skill: blender-sculpt-surface
scene_revision: <revision>
snapshot_id: <snapshot>
status: PASS | FAIL | UNVERIFIED
measurements: []
previews: []
artifacts: []
remaining_risks: []
```

Command success alone is not `PASS`; attach the checks required by the skill.
