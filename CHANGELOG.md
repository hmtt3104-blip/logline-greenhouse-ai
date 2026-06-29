# Changelog

All notable changes to this repository should be documented here.

## Unreleased

### Added

- Logline documentation skeleton.
- Architecture, setup, and safety documentation.
- Initial experiment record drafts.
- Roadmap, security, and contributing documentation.

### Changed

- Aligned README, architecture notes, safety notes, roadmap, and security policy with the sanitized public export model.
- Clarified that real reference images are local-only and are not part of this public repository.
- Clarified that the private working repository is maintained separately from this public export.
- Documented verified local-only startup with mock sensors and without Picamera2, OpenCV, Telegram tokens, or real camera images.
- Aligned public readiness language with Logline Foundation status taxonomy.
- Changed the dashboard default host to local-only `127.0.0.1`; LAN exposure now requires explicit configuration.
- Changed person detection to opt-in because it can save camera snapshots under `alerts/` and send photo alerts when configured.
- Clarified that Telegram alerting is optional, disabled for local smoke tests, and not validated as production alerting or LAN-safe settings behavior.

### Security

- Published this repository as a clean public export without old working-repository history.
- Documented image, camera privacy, and private runtime configuration boundaries.
- Added UI and setup warnings for Telegram settings, local secrets, and LAN-exposed dashboard risk.

## 2026-04-18 - Prototype snapshot

### Added

- Flask greenhouse dashboard.
- Camera stream with Picamera2 path and placeholder fallback.
- Reference capture and matching workflow.
- OpenCV HOG person detection worker.
- Optional Telegram alert path.
- Mock sensor service.

### Notes

- Status: `Prototype / NEEDS_CLEANUP / Not production-ready`.
- No release created.
