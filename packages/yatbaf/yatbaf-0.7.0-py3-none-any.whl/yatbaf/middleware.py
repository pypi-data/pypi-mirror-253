from __future__ import annotations

__all__ = (
    "Middleware",
    "chat_action",
)

import asyncio
from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import TypeVar

if TYPE_CHECKING:
    from .enums import ChatAction
    from .types import Message
    from .typing import HandlerCallable
    from .typing import HandlerMiddleware
    from .typing import MiddlewareType

T = TypeVar("T")


class Middleware(Generic[T]):

    def __init__(
        self,
        obj: MiddlewareType[T],
        *,
        is_handler: bool = False,
        is_local: bool = False,
        **params: Any,
    ) -> None:
        self.obj = obj
        self.is_handler = is_handler
        self.is_local = is_local
        self.params = params

    def __call__(self, obj: T) -> T:
        return self.obj(obj, **self.params)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Middleware) and (  # yapf: disable
            other is self or (
                other.obj is self.obj
                and other.is_handler is self.is_handler
                and other.is_local is self.is_local
            )
        )


def chat_action(action: ChatAction) -> HandlerMiddleware[Message]:
    """Send chat action and automatically update it if your operation takes
    more than 5 seconds to complete.

    Usage::

        @on_message(middleware=[chat_action(ChatAction.UPLOAD_PHOTO)])
        async def slow_operation(message: Message) -> None:
            ...

    See: :class:`ChatAction <yatbaf.enums.ChatAction>`

    :param action: Chat action.
    """

    def outer(handler: HandlerCallable[Message]) -> HandlerCallable[Message]:

        async def inner(update: Message) -> None:
            event = asyncio.Event()

            async def _task() -> None:
                while not event.is_set():
                    await update.bot.send_chat_action(update.chat.id, action)
                    await asyncio.sleep(4.5)  # update status every 4.5 sec

            _ = asyncio.create_task(
                _task(), name=f"chat-action-{update.message_id}"
            )
            try:
                await handler(update)
            finally:
                event.set()

        return inner

    return outer
