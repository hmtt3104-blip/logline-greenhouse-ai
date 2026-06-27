"""Entry point: Flask dashboard for greenhouse_ai on Raspberry Pi."""

from __future__ import annotations

import logging
import os

from dotenv import load_dotenv

from dashboard.app import create_app


DEFAULT_DASHBOARD_HOST = "127.0.0.1"
DEFAULT_DASHBOARD_PORT = "5000"


def main() -> None:
    load_dotenv()
    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    app = create_app()
    host = os.environ.get("DASHBOARD_HOST", DEFAULT_DASHBOARD_HOST)
    port = int(os.environ.get("DASHBOARD_PORT", DEFAULT_DASHBOARD_PORT))
    app.run(host=host, port=port, threaded=True, use_reloader=False)


if __name__ == "__main__":
    main()
