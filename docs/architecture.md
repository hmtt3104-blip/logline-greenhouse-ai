# Architecture

## Current flow

```text
Camera / Picamera2
  -> camera.stream.CameraStream
  -> MJPEG frame cache
  -> Flask /video_feed
  -> dashboard camera page
```

```text
Camera frame
  -> local reference capture
  -> private local reference image
  -> reference matching
  -> private local comparison output
  -> dashboard result
```

```text
Camera frame
  -> OpenCV HOG person detection
  -> local alert snapshot
  -> optional Telegram photo alert
  -> detection status API
```

```text
Mock sensor service
  -> /api/sensors
  -> dashboard sensors page
  -> future live greenhouse sensor drivers
```

## Components

### `main.py`

Entry point. Loads `.env`, creates the Flask app, and starts the local dashboard server.

### `dashboard/`

Flask application, routes, templates, static CSS, reference-image workflow, and Telegram configuration helpers.

Main routes:

- `/`
- `/camera`
- `/video_feed`
- `/reference/me.jpg`
- `/reference/last_test.jpg`
- `/api/reference/capture`
- `/api/reference/test`
- `/sensors`
- `/api/sensors`
- `/telegram`
- `/api/telegram/test`

### `camera/stream.py`

Camera abstraction.

Uses Picamera2 when available. Falls back to generated placeholder frames when camera hardware or dependencies are missing.

### `camera/person_detection.py`

Optional person detection worker.

Uses OpenCV HOG detection when OpenCV is installed. Saves local alert snapshots and can send Telegram photo alerts when credentials are configured.

### `dashboard/reference_flow.py`

Reference image capture and comparison.

Current matching path:

- OpenCV ORB when available;
- Pillow dHash fallback when OpenCV is unavailable.

Real reference images are local-only and are not part of this public export.

### `dashboard/telegram_config.py`

Loads and saves Telegram settings from environment variables or local instance config.

Sends Telegram messages or photos through the Telegram Bot API.

### `sensors/service.py`

Mock sensor service.

Returns generated values for temperature, humidity, soil moisture, pressure, and light. This is the boundary where future live sensor drivers should connect.

## Source of truth

Current source of truth:

- code in `camera/`, `dashboard/`, `sensors/`, and `main.py`;
- setup and safety docs in `docs/`;
- experiment records in `experiments/`.

Real reference images are not source-of-truth for this public repository. The `reference/` directory contains only usage notes, and private image files are ignored by Git.

## Future architecture questions

- Should live sensor drivers stay inside `sensors/` or become adapters under a new hardware layer?
- Should Telegram alerts remain in the dashboard app or become an integration module?
- Should local AI inference be added here or kept as a separate repo/module?
- Should authentication be added before any LAN-exposed dashboard use?
