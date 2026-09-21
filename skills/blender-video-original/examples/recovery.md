# Original white-model recovery example

When a trigger light starts before hand contact:

1. Preserve the current scene revision and identify the verified contact frame.
2. Move only the trigger/effect keys; do not rebuild approved locomotion or camera work.
3. Re-render and inspect the contact interval plus adjacent frames.
4. Update the evidence packet with both the initial failure and repaired result.

After two bounded repairs of the same defect, preserve the best version and report the remaining
interval as `FAIL` or `UNVERIFIED` rather than repeatedly changing approved work.
