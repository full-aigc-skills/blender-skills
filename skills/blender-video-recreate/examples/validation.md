# Reference recreation validation example

```yaml
skill: blender-video-recreate
source_sha256: <sha256>
source_segment: {start: "00:12.400", end: "00:20.400"}
project: {fps: 24, frame_start: 1, frame_end: 192}
status:
  media_analysis: PASS
  blender_structure: PASS
  motion_contacts: PASS | FAIL | UNVERIFIED
  camera_composition: PASS | FAIL | UNVERIFIED
  encoding: PASS | FAIL | UNVERIFIED
  generated_video: PASS | FAIL | UNVERIFIED
artifacts: []
comparisons: []
remaining_estimates: []
```
