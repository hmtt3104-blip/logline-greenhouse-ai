# Safety and Security Notes

Current public-readiness status: `Public cleanup required`.

This repository is a sanitized public Logline export. The working/private `greenhouse_ai` repository may contain local experiment history and is maintained separately.

## Public image cleanup status

The following image artifacts were removed from the current tree:

- `reference/me.jpg`
- `reference/last_test.jpg`
- `test.jpg`

This export does not include the old Git history. If publishing from the original working repository instead, historical GitHub history still needs review before flagship/public-ready status.

Real reference images are not committed. Use local private images only.

## Dashboard exposure

The app can bind to different hosts through `DASHBOARD_HOST`.

Recommended local-only value:

```text
DASHBOARD_HOST=127.0.0.1
```

Riskier LAN-exposed value:

```text
DASHBOARD_HOST=0.0.0.0
```

`0.0.0.0` makes the dashboard reachable from other devices on the network when firewall and routing allow it. Do not use this mode with real camera feeds, Telegram settings, or greenhouse controls unless the network exposure is intentional and protected.

## Telegram token handling

Telegram tokens and chat IDs must stay local.

Allowed local locations:

- `.env` ignored by Git;
- local Flask `instance/telegram.json` ignored by Git.

Never commit:

- `TELEGRAM_BOT_TOKEN`;
- `TELEGRAM_CHAT_ID`;
- copied bot URLs containing tokens;
- screenshots showing Telegram credentials.

If a token is exposed, rotate it before continuing public work.

## Camera privacy

Camera frames can expose people, property, greenhouse layout, timestamps, or other private context.

Rules for public examples:

- use synthetic or sanitized images;
- crop private surroundings;
- strip EXIF metadata;
- do not publish reference face/person images;
- do not publish alert snapshots from real deployments.

## EXIF/image artifacts

Before public flagship use:

- confirm image artifacts are absent from the current tree;
- review historical GitHub history for old image artifacts;
- strip EXIF from any retained images;
- verify screenshots do not show tokens, IPs, file paths, or private dashboards.

## No production secrets

This repository must not contain:

- real API keys;
- Telegram bot tokens;
- production `.env`;
- private keys;
- Wi-Fi credentials;
- private deployment configs.

## No public live deployment configs

Public documentation should use placeholders, not live infrastructure details.

Do not publish:

- production IPs;
- VPN/Tailscale details;
- live dashboard URLs;
- private network maps;
- production logs;
- real alert photos.

## Before flagship public use

Run the Logline public repo cleanup checklist and mark the result:

- `BLOCKED`
- `NEEDS_CLEANUP`
- `READY`
