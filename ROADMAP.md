# Roadmap

## Current status

Repository status: `Prototype`

Public readiness: `NEEDS_CLEANUP`

Production readiness: `Not production-ready`

Reason: this repository is a clean public Logline export, but dashboard authentication, LAN exposure constraints, live sensor integration, and hardware/camera validation still need review before this repository can be treated as `READY`.

## Near-term

- [x] Publish a sanitized public export without old working-repository history.
- [x] Keep real reference images out of the public tree.
- [x] Document public image and camera privacy rules.
- [x] Keep private working-repository history separate from this public export.
- [x] Make the dashboard local-only by default.
- [x] Make person detection opt-in by default.
- [x] Record the public-readiness checklist result.
- [x] Verify local-only dashboard startup and mock sensor API without Picamera2, OpenCV, or Telegram.
- [ ] Add sanitized architecture diagram or screenshot assets under `images/`.
- [ ] Document Raspberry Pi hardware setup under `hardware/`.
- [ ] Add authentication or document LAN-only deployment constraints.
- [ ] Replace mock sensors with one documented live sensor experiment.

## Experiments to run

- [ ] Camera stream reliability on target Raspberry Pi hardware.
- [ ] OpenCV HOG person detection false-positive review.
- [ ] Telegram alert delivery under local-only settings.
- [ ] Mock sensor API to first live sensor driver.
- [ ] Local AI observer feasibility.

## Documentation to add

- [ ] Decision record for dashboard exposure model.
- [ ] Decision record for Telegram integration boundary.
- [ ] Hardware wiring/BOM notes.
- [ ] Sanitized demo images.

## Cleanup / review still required

- [ ] Dashboard security review.
- [ ] Confirm no production configs are present before each major public update.
- [ ] Confirm future public images are synthetic or sanitized and metadata-stripped.
- [ ] Confirm `.env`, tokens, chat IDs, private IPs, live dashboard URLs, and private images are absent from the public tree.

## Evidence required before `READY`

Public readiness should remain `NEEDS_CLEANUP` until:

- local-only setup remains reproducible;
- safety notes are current;
- LAN exposure and authentication behavior are reviewed;
- authentication or LAN-only constraints are decided and documented;
- at least one real hardware/camera experiment is documented.

## Release candidates

No release should be created until all `READY` evidence exists and the release notes explain what was tested and what was not tested.
