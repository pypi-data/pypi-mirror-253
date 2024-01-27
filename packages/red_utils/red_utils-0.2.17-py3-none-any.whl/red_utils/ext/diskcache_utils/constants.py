from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Type, Union

from red_utils.core.dataclass_utils.mixins import DictMixin

valid_key_types: list[Type] = [str, int, tuple, frozenset]
valid_val_types: list[Type] = [str, bytes, float, int, list, dict]
valid_tag_types: list[Type] = [str, int, float, bytes]


@dataclass
class TimeoutConf(DictMixin):
    """Define cache timeout as a class.

    Inherits the .as_dict() method from DictMixin.

    Params:
        amount (int): Amount of time to allow for timeout
        unit (str): Unit of time corresponding with the `amount` passed. Examples: ["minutes", "hours", "days", etc]
    """

    unit: str | None = field(default="minutes")
    amount: int | None = field(default=15)


# default_cache_dir: str = ".cache"
## Set default timeout to 24 hours
# default_timeout_dict: dict[str, Union[str, int]] = {"unit": "minutes", "amount": 15}

DEFAULT_CACHE_TIMEOUT: TimeoutConf = TimeoutConf()
default_timeout_dict: dict[str, Union[str, int]] = TimeoutConf().as_dict()
