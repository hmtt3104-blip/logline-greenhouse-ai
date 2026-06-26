# 2026-04-18 - Telegram Alert Pipeline

## Problem

The greenhouse observer needed a simple notification path for detection events without building a full notification service.

## Hypothesis

Telegram Bot API can provide a practical optional alert channel for early greenhouse monitoring.

## Experiment

Load Telegram settings from local environment or ignored instance config, then send test messages or photo alerts when configured.

## Environment

Local dashboard runtime with optional outbound internet access.

Telegram credentials must stay outside Git.

## Hardware

No dedicated hardware required beyond the Raspberry Pi/runtime host and optional camera for photo alerts.

## Software

- `dashboard/telegram_config.py`
- `dashboard/routes.py`
- `camera/person_detection.py`
- Telegram Bot API

## Data

Telegram token and chat ID are local-only secrets.

Alert payloads may include images and captions.

## Results

The code path exists for test messages and photo alerts.

## Failures

There is no authentication layer around the dashboard settings page yet.

The public docs must clearly explain token handling and dashboard exposure risk.

## Lessons

Telegram is useful as an optional integration, but it increases the security burden around local configuration and dashboard access.

## Next Question

Should Telegram remain built into the dashboard or become a separate optional integration module?

## Status

Documented

## Trust level

Medium - the integration path exists, but operational security boundaries need review.

## Links

- Repository: `greenhouse_ai`
- Related docs: `docs/safety.md`, `docs/setup.md`
- Release:
