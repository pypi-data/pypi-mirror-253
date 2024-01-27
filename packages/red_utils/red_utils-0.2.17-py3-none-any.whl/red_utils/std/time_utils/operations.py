from __future__ import annotations

import datetime
from datetime import (
    datetime as dt,
    timedelta,
)
from typing import Union

from .constants import TIME_FMT_12H, TIME_FMT_24H

def datetime_as_str(ts: dt = None, format: str = TIME_FMT_24H) -> str:
    """Convert a `datetime.datetime` object to a string.

    Params:
        ts (datetime.datetime): A Python `datetime.datetime` object to convert to a `str`
        format (str): The `str` time string format to use

    Returns
    -------
        (str): A formatted `datetime.datetime` `str`
    """
    _ts: str = ts.strftime(format=format)

    return _ts


def datetime_as_dt(ts: str = None, format: str = TIME_FMT_24H) -> dt:
    """Convert a datetime string to a `datetime.datetime` object.

    Params:
        ts (str): A datetime str to convert to a Python `datetime.datetime` object
        format (str): The `str` time string format to use

    Returns
    -------
        (str): A formatted `datetime.datetime` object
    """
    _ts: dt = dt.strptime(ts, format)

    return _ts


def get_ts(as_str: bool = False, format: str = TIME_FMT_24H) -> Union[dt, str]:
    """Get a timestamp object.

    Params:
        as_str (bool): If `True`, converts `datetime` to a `str`
        format (str): The `str` time string format to use

    Returns
    -------
        (datetime.datetime): a Python `datetime.datetime` object.
        (str): If `as_str` is `True`, converts datetime to a string & returns.
    """
    now: dt = dt.now()

    if as_str:
        now: str = datetime_as_str(ts=now, format=format)

    return now


if __name__ == "__main__":
    ts = get_ts()

    print(f"Timestamp ({type(ts)}): {ts}")

    as_str: str = get_ts(as_str=True)
    print(f"Timestamp: datetime to str Type({type(as_str).__name__}): {as_str}")

    as_dt: dt = datetime_as_dt(ts=as_str)
    print(f"Timestamp: str to datetime Type({type(as_dt).__name__}): {as_dt}")
