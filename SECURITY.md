# Security Policy

## Current status

Public readiness: `NEEDS_CLEANUP`

Known blocker:

- committed image artifacts in `reference/` and `test.jpg` must be replaced or sanitized before flagship public use.

## What must not be committed

- `.env`
- Telegram bot tokens
- Telegram chat IDs
- private keys
- production configs
- private IPs or deployment maps
- production logs
- personal images
- EXIF-bearing public assets

## Telegram tokens

Telegram credentials must stay local.

Use local `.env` or ignored local instance settings only.

If a token is exposed publicly, rotate it before continuing public work.

## Dashboard exposure

Use `127.0.0.1` for local-only testing.

Do not expose the dashboard with real camera feeds or credentials unless the deployment is intentionally secured.

## Reporting security issues

Do not paste secrets into public issues, pull requests, discussions, or comments.

Report the type of issue and affected file path without repeating the secret value.

## Cleanup checklist

Before this repository is pinned or treated as flagship-ready, run the Logline public repository cleanup checklist.
