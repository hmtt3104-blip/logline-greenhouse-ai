# 2026-04-17 - Flask Dashboard Bootstrap

## Problem

The greenhouse prototype needed a local interface for camera, sensors, and alert configuration without depending on an external cloud dashboard.

## Hypothesis

A small Flask app can provide enough local visibility for early greenhouse monitoring experiments.

## Experiment

Build a Flask dashboard with pages for home, camera, sensors, and Telegram configuration, then verify that the public export can start in local-only mode without optional hardware or external services.

## Environment

Local development environment and intended Raspberry Pi runtime.

Use sanitized environment values only.

Verified local-only smoke test environment:

```text
DASHBOARD_HOST=127.0.0.1
DASHBOARD_PORT=5055
TELEGRAM_ALERTS_ENABLED=0
PERSON_DETECTION_ENABLED=0
```

No-hardware smoke test file:

```text
tests/test_no_hardware_smoke.py
```

## Hardware

Target hardware: Raspberry Pi with optional camera.

Exact production hardware details are not documented in this draft.

The verified local smoke test did not require Picamera2, OpenCV, Telegram, or a physical camera.

## Software

- Python 3.12.10
- Flask
- `main.py`
- `dashboard/`
- `.env.example`
- `sensors/service.py`
- `tests/test_no_hardware_smoke.py`

## Data

Dashboard pages and API responses.

Sensor data is mock data at this stage.

Verified local smoke test:

```text
GET / -> 200
GET /api/sensors -> 200
```

No-hardware smoke test coverage added:

```text
Flask create_app()
GET /
GET /api/sensors
GET /api/detection/status
PERSON_DETECTION_ENABLED=0
TELEGRAM_ALERTS_ENABLED=0
```

`/api/sensors` serves mock sensor data through `get_sensor_service().read_all()`.

## Results

Local-only dashboard reproducibility: PASS.

No-hardware smoke-test path: ADDED, pending local test run after checkout.

The dashboard structure exists and exposes routes for camera, sensors, reference matching, and Telegram configuration.

The public export can start on `127.0.0.1` and serve the home page and mock sensor API without optional camera, OpenCV, or Telegram integrations.

The added no-hardware smoke test is intended to keep that path guarded in future changes.

## Failures

No authentication layer is present yet.

Public safety documentation was missing before this Logline skeleton.

LAN-exposed dashboard behavior is not validated and still needs authentication, network controls, or formally documented LAN-only constraints.

The assistant added the test file through GitHub but did not execute it locally on the user's machine; local test execution is still required.

## Lessons

Flask is sufficient for the first local observability layer, but dashboard exposure must be treated as a safety/security decision.

Local-only should remain the default mode for public reproducibility tests.

A smoke test proves local startup and mock sensor routing; it does not prove Raspberry camera reliability, production alerting, live sensor integration, or LAN exposure safety.

No-hardware tests should explicitly keep optional camera/CV/Telegram paths disabled unless those integrations are the subject of the test.

## Next Question

What authentication or LAN-only constraint should be documented before any LAN-exposed use?

## Status

Draft / local smoke test verified / no-hardware test added / needs local test run and hardware exposure validation

## Trust level

Medium for local-only dashboard startup and mock sensor API behavior.

Medium-low for the added no-hardware test until it is executed in the local checkout.

Low for Raspberry camera behavior, live sensors, production alerting, and LAN exposure safety until separately validated.

## Links

- Repository: `logline-greenhouse-ai`
- Related docs: `docs/setup.md`, `docs/safety.md`
- Release: none
