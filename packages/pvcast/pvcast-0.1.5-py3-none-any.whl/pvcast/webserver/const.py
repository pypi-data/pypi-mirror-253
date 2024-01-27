"""Constants for the webserver module."""
from __future__ import annotations

import datetime as dt

API_VERSION = "0.1.2"

START_DT_DEFAULT = dt.datetime.now(dt.timezone.utc).replace(
    hour=0, minute=0, second=0, microsecond=0
)

END_DT_DEFAULT = dt.datetime.now(dt.timezone.utc).replace(
    hour=23, minute=59, second=59, microsecond=0
)
