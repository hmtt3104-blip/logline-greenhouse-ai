# 2026-04-18 - Telegram Alert Pipeline

## Problem

The greenhouse observer needed a simple notification path for detection events without building a full notification service.

## Hypothesis

Telegram Bot API can provide a practical optional alert channel for early greenhouse monitoring.

## Experiment

Load Telegram settings from local environment or ignored instance config, then send test messages or photo alerts only when explicitly configured and enabled.

Telegram is optional in the public export. The local dashboard smoke test does not require Telegram credentials or outbound Telegram calls.

## Environment

Local dashboard runtime with optional outbound internet access.

Telegram credentials must stay outside Git.

Verified local-only smoke test posture:

```text
TELEGRAM_ALERTS_ENABLED=0
PERSON_DETECTION_ENABLED=0
DASHBOARD_HOST=127.0.0.1
```

## Hardware

No dedicated hardware required beyond the Raspberry Pi/runtime host and optional camera for photo alerts.

Photo alerts are privacy-sensitive because they may include camera frames.

## Software

- `dashboard/telegram_config.py`
- `dashboard/routes.py`
- `camera/person_detection.py`
- Telegram Bot API

## Data

Telegram token and chat ID are local-only secrets.

Alert payloads may include images and captions.

`instance/telegram.json` and `.env` are local-only runtime configuration and must not be committed.

## Results

Optional Telegram code path: implemented.

Local smoke test without Telegram: PASS.

Production alerting behavior: NOT VALIDATED.

The code path exists for test messages and photo alerts, but the public export does not prove safe operational use.

## Failures

There is no authentication layer around the dashboard settings page yet.

The public docs must clearly explain token handling and dashboard exposure risk.

Telegram settings must not be used from a LAN-exposed dashboard unless authentication, network controls, and deployment intent are reviewed.

## Lessons

Telegram is useful as an optional integration, but it increases the security burden around local configuration and dashboard access.

Outbound integrations should be disabled for local smoke tests unless they are the explicit subject of the test.

Photo alerts combine notification risk with camera privacy risk, so person detection and Telegram alerting must remain opt-in.

## Next Question

Should Telegram remain built into the dashboard or become a separate optional integration module?

## Status

Draft / optional integration implemented / local smoke test does not require Telegram / production alerting not validated

## Trust level

Medium for optional integration boundary and token-handling documentation.

Low for production alerting behavior and LAN-exposed settings safety until separately validated.

## Links

- Repository: `logline-greenhouse-ai`
- Related docs: `docs/safety.md`, `docs/setup.md`
- Release: none
