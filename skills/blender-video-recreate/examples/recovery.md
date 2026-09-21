# Reference recreation recovery example

If a contact remains late after two bounded repairs:

1. Preserve the best `.blend`, preview, failing interval, and comparison pair.
2. Verify that timestamp-to-frame conversion and source frame rate are correct.
3. Adjust only the relevant action/camera keys and re-render that interval.
4. If the defect persists, mark motion/contact `FAIL`, describe the measured offset, and stop.

For remote generation, store and query the original task id. Recovery never means silently
submitting another paid job.
