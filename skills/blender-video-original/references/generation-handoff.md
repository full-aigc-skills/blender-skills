# Optional generation handoff

Treat local white-model production and stochastic video generation as separate acceptance layers.
Discover the current provider's documented inputs instead of guessing from its name. Prefer a
video/motion reference route when available; image-only input weakens temporal control.

Before any upload or paid submission, bind provider, input artifact hash, upload authorization,
model/settings, cost quote or exact request, maximum charge, and allowed submission count. Store
the task id after submission and query it after timeouts or unknown states; never duplicate a paid
job because polling failed.

The handoff prompt should preserve roles, count, action order, contacts, camera route, and ending
state while adding target appearance. Verify the downloaded result's hash, media properties,
action order, contacts, and camera separately. If no compatible authorized service exists, deliver
the `.blend`, preview, shot plan, and prompt package with generation marked `UNVERIFIED`.
