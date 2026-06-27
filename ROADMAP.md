# Roadmap

## Current status

Repository status: `Prototype`

Public readiness: `NEEDS_CLEANUP`

Production readiness: `Not production-ready`

Reason: this repository is a clean public Logline export, but dashboard exposure, authentication, image privacy, live sensor integration, and public-readiness checklist evidence still need review before this repository can be treated as `READY`.

## Near-term

- [x] Publish a sanitized public export without old working-repository history.
- [x] Keep real reference images out of the public tree.
- [x] Document public image and camera privacy rules.
- [x] Keep private working-repository history separate from this public export.
- [ ] Record the public-readiness checklist result.
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

- [ ] Public-readiness checklist result.
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

- setup is reproducible;
- safety notes are current;
- dashboard exposure behavior is reviewed;
- authentication or LAN-only constraints are decided and documented;
- at least one real hardware/camera experiment is documented;
- the repository has a clear public-readiness checklist result.

## Release candidates

No release should be created until all `READY` evidence exists and the release notes explain what was tested and what was not tested.
