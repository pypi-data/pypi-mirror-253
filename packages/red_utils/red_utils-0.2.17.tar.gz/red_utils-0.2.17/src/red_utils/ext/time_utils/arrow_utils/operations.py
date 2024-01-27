from __future__ import annotations

import datetime
from typing import Union

from .constants import TIME_FMT_12H, TIME_FMT_24H
from .validators import VALID_TIME_PERIODS

import arrow

def shift_ts(
    start_date: Union[datetime.datetime, str, arrow.Arrow] = None,
    _tz: str = "US/Eastern",
    target_tz: str = "US/Eastern",
    period: str = None,
    amount: int = 0,
) -> arrow.Arrow:
    """Shift a timestamp forward/back a period of time (years, months, weeks, days, hours, minutes, seconds).

    Arguments:
    ---------
        start_date (datetime.datetime, str, arrow.Arrow):
            The timestamp you already have that you want to shift/convert.
            If start_date is not of type (arrow.Arrow), the function will try to convert it
        _tz:
            The timezone for the starting timestamp.
        target_tz:
            The timezone for the shifted timestamp. If no target_tz is passed, it will default
            to the same value as _tz.
        period:
            The period of time to shift the timestamp forward/backward. Must be one of:
            [years, months, weeks, days, hours, minutes, seconds]
        amount:
            A positive or negative integer value (i.e. +1/-1) to shift the timestamp. Positive integer
            values can be passed explicitly or implicitly, i.e. amount=1 OR amount=+1.

    Example:
    -------
        _tz = "US/Eastern"
        target_tz = "UTC"
        _start_date_time_str = "2022-08-12 00:00:00"
        start_date = arrow.get(_start_date_time_str, tzinfo=_tz)

        ## start_date = 2022-08-19T00:00:00-04:00
    """
    ## Validate inputs
    if not period:
        raise ValueError(
            f"Missing a period of time. Must be one of {VALID_TIME_PERIODS}"
        )
    if not isinstance(period, str) and not isinstance(period, datetime.datetime):
        raise TypeError(
            f"Invalid type for period: ({type(period)}). Must be one of [str, datetime.datetime]"
        )
    if period not in VALID_TIME_PERIODS:
        raise TypeError(
            f"Invalid period of time: [{period}]. Must be one of {VALID_TIME_PERIODS}"
        )
    if not amount:
        raise ValueError("Missing amount of time to shift timestamp")
    ## Validate timezones
    if not _tz:
        raise ValueError("Missing starting timezone")
    if not target_tz:
        try:
            ## Set target_tz to same timezone as _tz if no value was passed
            target_tz = _tz
        except Exception as exc:
            raise Exception(f"Unhandled exception setting target_tz. Details: {exc}")
    if not start_date:
        raise ValueError("Missing a start date")
    if not isinstance(start_date, arrow.Arrow):
        start_date = arrow.get(start_date, tzinfo=_tz)

    try:
        ## Initialize return timestamp
        return_ts: arrow.Arrow = None

        match period:
            case "years":
                return_ts: arrow.Arrow = start_date.shift(years=amount)
            case "months":
                return_ts: arrow.Arrow = start_date.shift(months=amount)
            case "weeks":
                return_ts: arrow.Arrow = start_date.shift(weeks=amount)
            case "days":
                return_ts: arrow.Arrow = start_date.shift(days=amount)
            case "hours":
                return_ts: arrow.Arrow = start_date.shift(hours=amount)
            case "minutes":
                return_ts: arrow.Arrow = start_date.shift(minutes=amount)
            case "seconds":
                return_ts: arrow.Arrow = start_date.shift(seconds=amount)
            case _:
                raise NotImplementedError(
                    f"Support for shift type: {period} not yet implemented."
                )

        return return_ts
    except Exception as exc:
        raise Exception(f"Unhandled exception")
