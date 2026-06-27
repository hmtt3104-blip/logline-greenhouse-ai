# Security Policy

## Current status

Repository status: Prototype.

Public readiness: NEEDS_CLEANUP.

Production readiness: Not production-ready.

This repository is a clean public Logline export. The private working repository is maintained separately and is not part of this public history.

The export is sanitized, but dashboard exposure, authentication, image privacy, external service configuration, and public-readiness checklist evidence still need review before this repository can be treated as `READY`.

## What must not be committed

- `.env`
- private runtime configuration
- notification or messaging credentials
- private keys
- deployment configs from real systems
- private IPs or deployment maps
- production logs
- personal images
- metadata-bearing public assets

## External service settings

External service credentials must stay local.

Use local `.env` or ignored local instance settings only.

If a credential is exposed publicly, rotate it before continuing public work.

## Dashboard exposure

Use `127.0.0.1` for local-only testing.

Do not expose the dashboard with real camera feeds, private settings, or credentials unless the deployment is intentionally secured.

Dashboard exposure without authentication, network controls, and documented intent keeps public readiness at `NEEDS_CLEANUP`.

## Images and camera data

Camera frames and reference images can reveal people, property, greenhouse layout, timestamps, or private environment details.

Public examples must use synthetic or sanitized images with metadata removed.

## Status escalation

If a secret, token, chat ID, private IP, live dashboard URL, private image, or deployment map is found in this repository, public readiness becomes `BLOCKED` until the unsafe content is removed and any exposed credential is rotated.

If safety is uncertain, keep public readiness at `NEEDS_CLEANUP`.

## Reporting security issues

Do not paste secrets into public issues, pull requests, discussions, or comments.

Report the type of issue and affected file path without repeating the secret value.

## Cleanup checklist

Before this repository is pinned or treated as flagship-ready, run the Logline public repository cleanup checklist and record the result.
