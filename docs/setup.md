# Setup

This setup guide is sanitized. Do not paste real tokens, private IPs, or live deployment values into public documentation.

## Local Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Environment file

Copy the example file and edit it locally:

```bash
cp .env.example .env
```

Do not commit `.env`.

For local-only testing, prefer:

```text
DASHBOARD_HOST=127.0.0.1
DASHBOARD_PORT=5000
```

## Run locally

```bash
python main.py
```

Open:

```text
http://127.0.0.1:5000
```

## Raspberry Pi / Picamera2 notes

On Raspberry Pi OS, prefer system packages for camera support:

```bash
sudo apt update
sudo apt install -y python3-picamera2
```

The app can run without Picamera2. In that case, the camera stream uses placeholder frames.

## OpenCV notes

OpenCV is recommended for person detection and reference matching.

On Raspberry Pi OS:

```bash
sudo apt install -y python3-opencv
```

Without OpenCV:

- the dashboard still runs;
- person detection remains unavailable;
- reference matching falls back to the Pillow path where possible.

## Telegram optional setup

Telegram is optional.

If used, configure only in local `.env` or local instance settings:

```text
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
TELEGRAM_ALERTS_ENABLED=0
```

Do not commit Telegram tokens or chat IDs.

## Sensor status

Current sensor readings are mock data from `sensors/service.py`.

Future live drivers should document:

- sensor model;
- bus/pins;
- calibration assumptions;
- failure behavior;
- data trust level.
