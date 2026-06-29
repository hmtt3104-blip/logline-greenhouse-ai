from __future__ import annotations

import importlib
import os


def test_local_dashboard_routes_work_without_optional_integrations(monkeypatch):
    monkeypatch.setenv("DASHBOARD_HOST", "127.0.0.1")
    monkeypatch.setenv("TELEGRAM_ALERTS_ENABLED", "0")
    monkeypatch.setenv("PERSON_DETECTION_ENABLED", "0")

    from dashboard.app import create_app

    app = create_app()
    assert app.name == "dashboard.app"

    client = app.test_client()

    home = client.get("/")
    assert home.status_code == 200

    sensors = client.get("/api/sensors")
    assert sensors.status_code == 200
    payload = sensors.get_json()
    assert isinstance(payload, dict)
    assert "temperature_c" in payload
    assert "humidity_pct" in payload
    assert "soil_moisture_pct" in payload
    assert "timestamp" in payload

    detection = client.get("/api/detection/status")
    assert detection.status_code == 200
    status = detection.get_json()
    assert status["detection_enabled"] is False


def test_optional_modules_are_not_required_for_disabled_local_smoke(monkeypatch):
    monkeypatch.setenv("PERSON_DETECTION_ENABLED", "0")
    monkeypatch.setenv("TELEGRAM_ALERTS_ENABLED", "0")

    person_detection = importlib.import_module("camera.person_detection")
    assert person_detection.person_detection_enabled() is False

    status = person_detection.get_public_status()
    assert status["detection_enabled"] is False

    # Do not import cv2 or Picamera2 here. The point of this test is that the
    # local dashboard smoke path must stay usable without optional camera/CV
    # packages and without outbound Telegram credentials.
    assert "cv2" not in globals()
    assert os.environ["TELEGRAM_ALERTS_ENABLED"] == "0"
