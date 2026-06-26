# Roadmap

## Current status

Repo status: `Prototype`

Public readiness: `NEEDS_CLEANUP`

Reason: committed image artifacts must be replaced or sanitized before flagship public use.

## Near-term

- [ ] Replace or sanitize `reference/me.jpg`, `reference/last_test.jpg`, and `test.jpg`.
- [ ] Add sanitized architecture diagram or screenshot assets under `images/`.
- [ ] Document Raspberry Pi hardware setup under `hardware/`.
- [ ] Decide safe default dashboard host behavior.
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
- [ ] Public-readiness checklist result.

## Cleanup required

- [ ] Image/EXIF cleanup.
- [ ] Git history / secret scanning review.
- [ ] Dashboard security review.
- [ ] Confirm no production configs are present.

## Release candidates

No release should be created until:

- public cleanup blockers are resolved;
- README/docs are complete;
- setup is reproducible;
- safety notes are current.
