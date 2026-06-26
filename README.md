# logline-greenhouse-ai

## What this is

`logline-greenhouse-ai` is a Raspberry Pi greenhouse monitoring prototype with a local Flask dashboard, camera stream, reference-image matching, OpenCV person detection, Telegram alert hooks, and a mock sensor API.

This repository is being shaped into a Logline flagship example: an engineering journal where the experiment, failures, safety boundaries, and next questions are documented alongside the code.

## Problem

Small greenhouse automation work often starts as working scripts and field tests, but the reasoning becomes scattered: camera setup, alerting, dashboard behavior, sensor assumptions, and hardware limitations are hard to reconstruct later.

The problem is not only "make a dashboard." The problem is to make a small, observable greenhouse system that can be inspected, tested, and improved without hiding the experimental state.

## Hypothesis

A Raspberry Pi can act as a local greenhouse observer by combining:

- camera streaming;
- lightweight computer vision;
- simple dashboard pages;
- optional Telegram alerts;
- sensor APIs that can start as mock data and later connect to real hardware.

The system should remain useful even when optional hardware or services are unavailable.

## Experiment

Current prototype:

- runs a Flask dashboard;
- serves an MJPEG camera feed;
- falls back to placeholder frames when Picamera2 is unavailable;
- captures and compares reference images;
- runs optional OpenCV HOG person detection;
- sends optional Telegram alerts;
- exposes mock environmental sensor readings.

## Architecture

```text
Raspberry Pi / camera
  -> camera stream
  -> Flask dashboard
  -> reference capture / matching
  -> person detection
  -> optional Telegram alert

Mock sensor service
  -> /api/sensors
  -> dashboard sensors page
  -> future live hardware drivers
```

See `docs/architecture.md` for the current flow and boundaries.

## Current status

Status: `Prototype / Public cleanup required`

The code represents a working prototype direction, but this repository is not yet Logline flagship-ready.

Image cleanup status:

- `reference/me.jpg` removed from current tree.
- `reference/last_test.jpg` removed from current tree.
- `test.jpg` removed from current tree.

Historical GitHub history may still need review before flagship/public-ready status.

## Results / Lessons

- Flask is enough for a small local greenhouse dashboard.
- The app can keep running without Picamera2 by serving placeholder frames.
- Reference capture and comparison are useful as a low-cost test path before heavier vision.
- OpenCV HOG detection is simple enough to test on Raspberry Pi, but must be treated as experimental.
- Telegram alerts are useful, but require strict token handling and dashboard exposure rules.
- Sensor integration should remain explicit: mock data now, live hardware later.

## What failed

- Real sensor drivers are not implemented yet.
- The dashboard currently has no authentication layer.
- Default dashboard host behavior needs safer documentation and likely safer defaults before public flagship use.
- Committed reference/test images were removed from the current tree, but Git history still needs public-readiness review.
- Initial experiment records are drafts and need validation.
- `docs/`, `hardware/`, `images/`, and `data/` are only being introduced now.

## Next questions

- What is the safest default run mode for a local greenhouse dashboard?
- Which camera pipeline is reliable on the target Raspberry Pi hardware?
- Can person detection produce useful signals with acceptable false positives?
- Which sensors should replace the mock sensor service first?
- Should Telegram alerts remain optional or become a separate integration module?
- What local AI layer, if any, belongs in this repo?

## Safety / Security notes

Before this repository is pinned or treated as public-ready, review it with the Logline public cleanup checklist.

Current status: `Public cleanup required`.

Important boundaries:

- Do not commit real `.env` files.
- Do not commit Telegram bot tokens or chat IDs.
- Do not commit production deployment configs.
- Do not expose a live dashboard publicly without authentication and network controls.
- Treat camera frames and reference images as sensitive.
- Strip EXIF metadata from any public images.
- Real reference images are not committed; use local private images only.
- Historical image artifacts may still exist in Git history and should be reviewed before flagship public use.

See `docs/safety.md` for detailed safety notes.

## Repository map

```text
README.md          Project entry point
CHANGELOG.md       Notable documented changes
CONTRIBUTING.md    Contribution and review expectations
ROADMAP.md         Cleanup and flagship path
SECURITY.md        Security policy
camera/            Camera stream and person detection
dashboard/         Flask dashboard, routes, templates, Telegram config
data/              Sanitized sample data notes
docs/              Architecture, setup, safety notes
docs/decisions/    Future decision records
experiments/       Logline experiment records
hardware/          Future hardware notes, wiring, BOM
images/            Future sanitized diagrams/screenshots
reference/         Local-only reference image notes; real images ignored
scripts/           Future helper scripts
sensors/           Mock sensor service, future live driver boundary
```

## How to run / reproduce

Use a local-only development setup first.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

For safer local testing, set:

```bash
DASHBOARD_HOST=127.0.0.1
DASHBOARD_PORT=5000
```

Open:

```text
http://127.0.0.1:5000
```

Raspberry Pi camera and OpenCV setup notes are in `docs/setup.md`.

## Related experiments

- `experiments/2026-04-17-flask-dashboard-bootstrap.md`
- `experiments/2026-04-18-person-detection-opencv-hog.md`
- `experiments/2026-04-18-telegram-alert-pipeline.md`
