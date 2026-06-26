# DEC-001 — Dashboard Exposure Model

## Status

`Accepted / documentation-only`

## Context

`logline-greenhouse-ai` includes a local Flask dashboard for camera, reference image, Telegram test, and mock sensor workflows.

The dashboard is useful during local development, but network exposure changes the risk profile. Camera frames, reference image flows, Telegram settings, and future sensor integrations can reveal private operational details if the dashboard is exposed without controls.

## Decision

The default documented dashboard model is local-only.

Recommended value:

```text
DASHBOARD_HOST=127.0.0.1
```

LAN-exposed mode is treated as advanced and intentional.

Advanced value:

```text
DASHBOARD_HOST=0.0.0.0
```

`0.0.0.0` should not be presented as the normal default in public documentation. It may be used only when the operator intentionally wants the dashboard reachable from other devices and understands the network exposure.

## Alternatives considered

### Always bind to `0.0.0.0`

Rejected for public guidance.

It is convenient for phone or LAN access, but it risks normalizing an unsafe default for a dashboard that can show camera-related data and integration settings.

### Always bind to `127.0.0.1`

Accepted as the public documentation default.

This is safer for reproducible local testing and reduces accidental exposure.

### Add authentication now

Deferred.

Authentication may be needed later, but this decision record does not change runtime behavior. It only defines the public documentation boundary.

## Consequences

- README and setup docs should recommend `127.0.0.1` first.
- Safety docs should explain that `0.0.0.0` exposes the dashboard to the network.
- LAN-exposed use requires a separate review before being treated as normal use.
- Runtime code is not changed by this decision.

## Related issue

- https://github.com/hmtt3104-blip/logline-greenhouse-ai/issues/1

## Related documents

- `README.md`
- `docs/setup.md`
- `docs/safety.md`

## Review trigger

Review this decision if:

- dashboard authentication is added;
- camera streams are exposed beyond localhost;
- real sensors replace mock data;
- Telegram settings become part of the normal UI flow;
- this repo becomes a pinned or flagship Logline repository.
