# 2026-04-18 - Person Detection with OpenCV HOG

## Problem

The greenhouse observer needed a lightweight way to detect person-like activity from camera frames without adding a heavy AI stack.

## Hypothesis

OpenCV HOG person detection can provide a simple first signal on Raspberry Pi-class hardware.

## Experiment

Run a background worker that captures camera frames, checks for person-like detections with OpenCV HOG, saves alert snapshots, and exposes detection status.

## Environment

Intended runtime: Raspberry Pi OS with optional `python3-opencv`.

The app should continue running when OpenCV is unavailable.

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

The detection worker exists and can save local snapshots and update public detection status.

## Failures

False positives and false negatives have not been systematically measured.

Public demo images are not yet available because any future examples must be synthetic or sanitized and metadata-stripped.

## Lessons

OpenCV HOG is acceptable as a first experiment, but the result should not be treated as reliable security detection without field data.

## Next Question

What is the false-positive rate in the actual greenhouse camera position and lighting?

## Status

Documented

## Trust level

Low - implementation exists, but field accuracy is not yet measured.

## Links

- Repository: `greenhouse_ai`
- Related docs: `docs/architecture.md`, `docs/safety.md`
- Release:
