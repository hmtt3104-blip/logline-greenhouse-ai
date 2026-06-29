# 2026-04-18 - Person Detection with OpenCV HOG

## Problem

The greenhouse observer needed a lightweight way to detect person-like activity from camera frames without adding a heavy AI stack.

## Hypothesis

OpenCV HOG person detection can provide a simple first signal on Raspberry Pi-class hardware.

## Experiment

Run an optional background worker that captures camera frames, checks for person-like detections with OpenCV HOG, saves alert snapshots, and exposes detection status.

Person detection is opt-in in the public export because it can save camera snapshots under `alerts/` and can send Telegram photo alerts when configured.

## Environment

Intended runtime: Raspberry Pi OS with optional `python3-opencv`.

The app should continue running when OpenCV is unavailable.

Verified local-only smoke test:

- OpenCV was not installed;
- `PERSON_DETECTION_ENABLED=0`;
- Flask app still imported, started locally, and served `/` and `/api/sensors` successfully.

## Hardware

Raspberry Pi with camera is the target.

Camera-specific reliability still needs a dedicated hardware experiment.

## Software

- `camera/person_detection.py`
- `camera/stream.py`
- OpenCV HOG detector
- Flask detection status endpoint

## Data

Camera frames and local alert snapshots.

Public sample images must be sanitized and EXIF-stripped.

Real reference images and private alert snapshots are not committed in this clean export.

## Results

Optional detection worker: implemented.

Default public behavior: disabled unless `PERSON_DETECTION_ENABLED=1`.

Local smoke test without OpenCV/person detection: PASS.

Field detection accuracy: NOT VALIDATED.

## Failures

False positives and false negatives have not been systematically measured.

Public demo images are not yet available because any future examples must be synthetic or sanitized and metadata-stripped.

Detection must not be treated as a security system or reliable intrusion detector without field data.

## Lessons

OpenCV HOG is acceptable as a first experiment, but the result should not be treated as reliable security detection without field data.

Optional computer-vision features must not block the local dashboard smoke test.

Privacy-sensitive features should be opt-in by default in public exports.

## Next Question

What is the false-positive rate in the actual greenhouse camera position and lighting when person detection is explicitly enabled?

## Status

Draft / optional feature implemented / disabled by default / field accuracy not validated

## Trust level

Medium for optional integration boundary and local smoke-test safety.

Low for detection accuracy and real greenhouse camera behavior until field-tested.

## Links

- Repository: `logline-greenhouse-ai`
- Related docs: `docs/architecture.md`, `docs/safety.md`
- Release: none
