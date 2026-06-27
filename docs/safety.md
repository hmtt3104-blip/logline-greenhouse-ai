# Safety and Security Notes

Repository status: Prototype.

Public readiness: NEEDS_CLEANUP.

Production readiness: Not production-ready.

This repository is a sanitized public Logline export. The private working repository is maintained separately and is not part of this public history.

The repository remains `NEEDS_CLEANUP` until dashboard exposure, authentication, image privacy, external service configuration, and public-readiness checklist evidence are reviewed.

## Public readiness checklist result

Final public readiness status: NEEDS_CLEANUP.

Reason:

- The public tree is sanitized and excludes old working-repository history, real reference images, private runtime configuration, production configs, and deployment secrets.
- Dashboard default is local-only, and person detection is opt-in.
- The repository still needs authentication or formally documented LAN-only constraints before any LAN-exposed use.
- Live sensor integration is still mock-only.
- Hardware/camera behavior and person-detection accuracy still need documented validation.

Finding statuses:

| Area | Finding status | Notes |
| --- | --- | --- |
| Secrets and tokens | OK | `.env`, Telegram tokens, and chat IDs are local-only and ignored. |
| Private images | OK | Real reference images and alert snapshots are not part of the public export. |
| Old working history | OK | Public export does not include old working-repository Git history. |
| Dashboard exposure | WARNING | Default is local-only, but LAN-exposed mode still lacks authentication and needs review. |
| External service settings | WARNING | Telegram is optional and local-only, but dashboard settings require protected use. |
| Live sensor integration | WARNING | Sensor data is mock-only until a live sensor experiment is documented. |
| Hardware/camera validation | WARNING | Target Raspberry Pi/camera behavior is not yet validated in a completed experiment record. |

## Public image status

This export does not include real reference images or old working-repository history.

The public tree intentionally contains only notes for image-related directories:

- `reference/README.md`
- `images/README.md`

Real reference images are local-only. Use synthetic or sanitized images for future public examples.

## Dashboard exposure

The dashboard should be tested locally first.

Recommended local-only value:

```text
DASHBOARD_HOST=127.0.0.1
```

LAN-exposed mode:

```text
DASHBOARD_HOST=0.0.0.0
```

`0.0.0.0` can expose the dashboard to other devices on the network. Use it only when the network exposure is intentional and protected.

LAN-exposed mode without authentication, network controls, and a documented reason keeps public readiness at `NEEDS_CLEANUP`.

## External service settings

Any messaging or notification integration must use local configuration only.

Do not commit private runtime configuration, chat identifiers, service credentials, copied request URLs, or screenshots that reveal private settings.

## Camera privacy

Camera frames can reveal people, property, greenhouse layout, timestamps, or other private context.

Rules for public examples:

- use synthetic or sanitized images;
- crop private surroundings;
- strip image metadata;
- do not publish person reference images;
- do not publish alert snapshots from real deployments.

## Public image metadata

Before adding public images:

- confirm the image is safe for publication;
- strip metadata;
- verify screenshots do not show private settings, file paths, dashboards, or network details;
- keep private reference images out of Git.

## No private runtime configuration

This repository must not contain private deployment files, private keys, Wi-Fi credentials, real runtime settings, or environment files from deployed systems.

## No public live deployment details

Public documentation should use placeholders, not live infrastructure details.

Do not publish production IPs, VPN details, live dashboard URLs, private network maps, logs, or real alert photos.

## Status escalation

If this repository contains a secret, token, chat ID, private IP, live dashboard URL, private image, or deployment map, public readiness becomes `BLOCKED` until cleaned and reviewed.

If safety is uncertain, public readiness remains `NEEDS_CLEANUP`.

## Before pinned, flagship, or READY use

Run the Logline public repo cleanup checklist and mark the result:

- `BLOCKED`
- `NEEDS_CLEANUP`
- `READY`

Do not treat this repository as pinned, flagship-ready, release-ready, or public-readiness `READY` until the checklist result and supporting evidence are documented.
