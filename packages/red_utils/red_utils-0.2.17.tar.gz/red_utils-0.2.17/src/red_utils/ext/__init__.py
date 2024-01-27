"""Extensions & utilities for third-party libraries I use frequently, like `red_utils.ext.sqla_utils`, which contains
boilerplate code for `SQLAlchemy`, or `red_utils.ext.pydantic`, which contains a method (parse_pydantic_schema) that can
parse a `Pydantic` class object into a compatible `SQLAlchemy` model.

This module uses pkgutil to only load modules if dependencies are met, keeping the `red_utils` package functional by limiting the utilities that are loaded.
If a pkgutil.find_loader() check fails, that import is passed over and will be unavailable
for type completion & usage.

!!! warning

    `pkutil.find_loader()` will be deprecated in a future Python 3.12 release. I will start updating the code in `red_utils` to be
    compatible with the new `importlib.util.find_spec()` method.
"""
from __future__ import annotations

import pkgutil

if pkgutil.find_loader("arrow") or pkgutil.find_loader("pendulum"):
    from . import time_utils

if pkgutil.find_loader("loguru"):
    from . import loguru_utils

if pkgutil.find_loader("pydantic"):
    from . import pydantic_utils

if pkgutil.find_loader("msgpack"):
    from . import msgpack_utils

if pkgutil.find_loader("diskcache"):
    from . import diskcache_utils

if pkgutil.find_loader("httpx"):
    from . import httpx_utils

if pkgutil.find_loader("fastapi"):
    from . import fastapi_utils

if pkgutil.find_loader("sqlalchemy"):
    from . import sqlalchemy_utils

if pkgutil.find_loader("rich"):
    from . import context_managers

if pkgutil.find_loader("pandas") or pkgutil.find_loader("polars"):
    from . import dataframe_utils
