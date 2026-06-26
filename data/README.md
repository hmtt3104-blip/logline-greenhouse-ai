# Data

This directory is reserved for sanitized sample data only.

Do not commit:

- production logs;
- raw camera frames from private spaces;
- Telegram payloads containing identifiers;
- real credentials;
- private IPs;
- sensor data that reveals a live deployment;
- EXIF-bearing images.

Allowed examples:

- small synthetic JSON payloads;
- mock sensor readings;
- redacted detection status samples;
- documented test fixtures.

If a dataset is derived from a real deployment, document:

- source;
- sanitization method;
- date range;
- limitations;
- trust level.
