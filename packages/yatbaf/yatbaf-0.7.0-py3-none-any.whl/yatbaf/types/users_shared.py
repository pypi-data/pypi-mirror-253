from __future__ import annotations

from typing import final

from .abc import TelegramType


@final
class UsersShared(TelegramType):
    """This object contains information about the users whose identifiers were
    shared with the bot using a :class:`~yatbaf.types.keyboard_buton.KeyboardButtonRequestUsers` button.

    See: https://core.telegram.org/bots/api#usersshared
    """  # noqa: E501

    request_id: int
    """Identifier of the request."""

    user_ids: list[int]
    """Identifiers of the shared users."""
