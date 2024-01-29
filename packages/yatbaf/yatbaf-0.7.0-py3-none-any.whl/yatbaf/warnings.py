from __future__ import annotations

__all__ = ("warn_duplicate",)

import warnings
from typing import TYPE_CHECKING

from .exceptions import BotWarning

if TYPE_CHECKING:
    from .abc import AbstractRouter
    from .handler import Handler


def warn_duplicate(
    obj: Handler | AbstractRouter,
    dest: AbstractRouter,
    stacklevel: int = 2,
) -> None:
    warnings.warn(
        f"{obj!r} is a duplicate and was not added to {dest!r}",
        category=BotWarning,
        stacklevel=stacklevel,
    )
