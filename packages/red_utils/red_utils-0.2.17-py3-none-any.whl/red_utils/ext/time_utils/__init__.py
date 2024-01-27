"""Utilities for `pendulum` and `arrow` libraries.

!!! warning

    The `arrow_utils` module will eventually be phased out, as I have nearly abandoned `arrow` in favor of `pendulum`.
"""
from __future__ import annotations

import pkgutil

if pkgutil.find_loader("arrow"):
    from . import arrow_utils

if pkgutil.find_loader("pendulum"):
    from . import pendulum_utils
    from .pendulum_utils import get_ts
    from .pendulum_utils.constants import (
        DEFAULT_TZ,
        TIME_FMT_12H,
        TIME_FMT_24H,
        TS_STR_REPLACE_MAP,
        VALID_TIME_PERIODS,
    )
    from .pendulum_utils.validators import validate_time_period
