# Roadmap

## Current status

Repo status: `Prototype`

Public readiness: `SANITIZED_PUBLIC_EXPORT`

Reason: this repository is a clean public Logline export. It does not include real reference images, old working-repository history, production configs, or deployment secrets.

## Near-term

- [x] Publish a sanitized public export without old working-repository history.
- [x] Keep real reference images out of the public tree.
- [x] Document public image and camera privacy rules.
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

## Cleanup / review still required

- [ ] Dashboard security review.
- [ ] Confirm no production configs are present before each major public update.
- [ ] Confirm future public images are synthetic or sanitized and metadata-stripped.
- [ ] Keep private working-repository history separate from this public export.

## Release candidates

No release should be created until:

- setup is reproducible;
- safety notes are current;
- at least one real hardware/camera experiment is documented;
- the repository has a clear public-readiness checklist result.