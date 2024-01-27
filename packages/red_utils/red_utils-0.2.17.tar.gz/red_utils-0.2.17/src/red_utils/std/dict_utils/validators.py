"""Functions to validate inputs for other `red_utils.std.dict_utils` methods."""
from __future__ import annotations

from typing import Any

def validate_dict(_dict: dict[str, str] = None) -> dict[Any, Any]:
    """Validates an input dict.

    Params:
        _dict (dict): The Python `dict` to validate

    Returns
    -------
        (dict): A validated `dict`

    Raises
    ------
        ValueError: If _dict is `None` or an invalid type
        TypeError: When `_dict`'s type is not `dict`
    """
    if _dict is None:
        raise ValueError("Missing dict to evaluate")

    if not isinstance(_dict, dict):
        raise TypeError(
            f"Invalid type for input _dict: ({type(_dict)}). Must be dict[str, str]"
        )

    return _dict
