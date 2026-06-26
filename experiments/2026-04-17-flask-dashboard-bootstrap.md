# 2026-04-17 - Flask Dashboard Bootstrap

## Problem

The greenhouse prototype needed a local interface for camera, sensors, and alert configuration without depending on an external cloud dashboard.

## Hypothesis

A small Flask app can provide enough local visibility for early greenhouse monitoring experiments.

## Experiment

Build a Flask dashboard with pages for home, camera, sensors, and Telegram configuration.

## Environment

Local development environment and intended Raspberry Pi runtime.

Use sanitized environment values only.

## Hardware

Target hardware: Raspberry Pi with optional camera.

Exact production hardware details are not documented in this draft.

## Software

- Python
- Flask
- `main.py`
- `dashboard/`
- `.env.example`

## Data

Dashboard pages and API responses.

Sensor data is mock data at this stage.

## Results

The dashboard structure exists and exposes routes for camera, sensors, reference matching, and Telegram configuration.

## Failures

No authentication layer is present yet.

Public safety documentation was missing before this Logline skeleton.

## Lessons

Flask is sufficient for the first local observability layer, but dashboard exposure must be treated as a safety/security decision.

## Next Question

What should the default safe dashboard exposure model be: local-only by default or LAN-accessible with explicit warnings?

## Status

Documented

## Trust level

Medium - the dashboard exists, but deployment safety and reproducibility still need review.

## Links

- Repository: `greenhouse_ai`
- Related docs: `docs/setup.md`, `docs/safety.md`
- Release:
