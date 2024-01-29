from __future__ import annotations

__all__ = (
    "UpdateT",
    "UpdateModel",
    "RouterMiddleware",
    "RouterCallable",
    "HandlerCallable",
    "HandlerMiddleware",
    "ReplyMarkup",
    "NoneStr",
    "NoneInt",
    "NoneBool",
)

from collections.abc import Awaitable
from collections.abc import Callable
from typing import TYPE_CHECKING
from typing import Any
from typing import Protocol
from typing import TypeAlias
from typing import TypeVar
from typing import runtime_checkable

if TYPE_CHECKING:
    from .bot import Bot
    from .models import UpdateInfo
    from .types import CallbackQuery
    from .types import ChatBoostRemoved
    from .types import ChatBoostUpdated
    from .types import ChatJoinRequest
    from .types import ChatMemberUpdated
    from .types import ChosenInlineResult
    from .types import ForceReply
    from .types import InlineKeyboardMarkup
    from .types import InlineQuery
    from .types import Message
    from .types import MessageReactionCountUpdated
    from .types import MessageReactionUpdated
    from .types import Poll
    from .types import PollAnswer
    from .types import PreCheckoutQuery
    from .types import ReplyKeyboardMarkup
    from .types import ReplyKeyboardRemove
    from .types import ShippingQuery
    from .types.abc import TelegramType
else:
    TelegramType = Any
    CallbackQuery = Any
    ChatBoostRemoved = Any
    ChatBoostUpdated = Any
    ChatJoinRequest = Any
    ChatMemberUpdated = Any
    ChosenInlineResult = Any
    ForceReply = Any
    InlineKeyboardMarkup = Any
    InlineQuery = Any
    Message = Any
    MessageReactionCountUpdated = Any
    MessageReactionUpdated = Any
    Poll = Any
    PollAnswer = Any
    PreCheckoutQuery = Any
    ReplyKeyboardMarkup = Any
    ReplyKeyboardRemove = Any
    ShippingQuery = Any

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

UpdateT = TypeVar(
    "UpdateT",
    bound=(
        CallbackQuery
        | ChatJoinRequest
        | ChatMemberUpdated
        | InlineQuery
        | ChosenInlineResult
        | Message
        | MessageReactionCountUpdated
        | MessageReactionUpdated
        | Poll
        | PollAnswer
        | PreCheckoutQuery
        | ShippingQuery
        | ChatBoostRemoved
        | ChatBoostUpdated
    )
)

ResultModelT = TypeVar(
    "ResultModelT", bound=TelegramType | list | int | str | bool
)

UpdateModel: TypeAlias = (
    "CallbackQuery "
    "| ChatJoinRequest "
    "| ChatMemberUpdated "
    "| InlineQuery "
    "| ChosenInlineResult "
    "| Message "
    "| MessageReactionCountUpdated "
    "| MessageReactionUpdated "
    "| Poll "
    "| PollAnswer "
    "| PreCheckoutQuery "
    "| ShippingQuery"
    "| ChatBoostRemoved"
    "| ChatBoostUpdated"
)

ReplyMarkup: TypeAlias = (
    "ForceReply "
    "| InlineKeyboardMarkup "
    "| ReplyKeyboardMarkup "
    "| ReplyKeyboardRemove"
)

NoneStr: TypeAlias = "str | None"
NoneInt: TypeAlias = "int | None"
NoneBool: TypeAlias = "bool | None"

GuardCallable: TypeAlias = "Callable[[UpdateT], None]"
MiddlewareType: TypeAlias = "Callable[[T], T]"
HandlerCallable: TypeAlias = "Callable[[UpdateT], Awaitable[None]]"
HandlerMiddleware: TypeAlias = "MiddlewareType[HandlerCallable[UpdateT]]"
RouterCallable: TypeAlias = "Callable[[UpdateInfo[UpdateT]], Awaitable[bool]]"
RouterMiddleware: TypeAlias = "MiddlewareType[RouterCallable[UpdateT]]"

PollingHook: TypeAlias = "Callable[[Bot], Awaitable[None]]"


@runtime_checkable
class Filter(Protocol[T_contra]):
    """Update filter protocol."""

    @property
    def priority(self) -> int:
        """Filter priority. Used for sorting."""
        pass

    def check(self, update: T_contra) -> bool:  # noqa: U100
        """Returns ``True`` if ``update`` matches the filter parameters.

        :param update: Incoming update.
        """
        pass


@runtime_checkable
class InputFile(Protocol):
    """File protocol"""

    @property
    def file_name(self) -> str:
        """Name of file."""
        pass

    async def read(self) -> bytes:
        """Returns the file content."""
        pass
