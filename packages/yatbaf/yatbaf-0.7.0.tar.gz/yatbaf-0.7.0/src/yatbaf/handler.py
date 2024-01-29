from __future__ import annotations

__all__ = (
    "Handler",
    "on_message",
    "on_edited_message",
    "on_channel_post",
    "on_edited_channel_post",
    "on_message_reaction",
    "on_message_reaction_count",
    "on_inline_query",
    "on_chosen_inline_result",
    "on_callback_query",
    "on_shipping_query",
    "on_pre_checkout_query",
    "on_poll",
    "on_poll_answer",
    "on_my_chat_member",
    "on_chat_member",
    "on_chat_join_request",
    "on_chat_boost",
    "on_removed_chat_boost",
)

from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeAlias
from typing import TypeVar
from typing import cast
from typing import final
from typing import overload

from .enums import UpdateType
from .typing import UpdateT
from .utils import ensure_unique

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Sequence

    from .abc import AbstractRouter
    from .middleware import Middleware
    from .types import CallbackQuery
    from .types import ChatBoostRemoved
    from .types import ChatBoostUpdated
    from .types import ChatJoinRequest
    from .types import ChatMemberUpdated
    from .types import ChosenInlineResult
    from .types import InlineQuery
    from .types import Message
    from .types import MessageReactionCountUpdated
    from .types import MessageReactionUpdated
    from .types import Poll
    from .types import PollAnswer
    from .types import PreCheckoutQuery
    from .types import ShippingQuery
    from .typing import Filter
    from .typing import HandlerCallable
    from .typing import HandlerMiddleware


@final
class Handler(Generic[UpdateT]):
    """Handler object.

    :param fn: Handler function.
    :param update_type: Handler update type. See :class:`~yatbaf.enums.UpdateType`
    :param middleware: *Optional.* A sequence of :class:`~yatbaf.typing.HandlerMiddleware`.
    :param filters: *Optional.* A sequence of :class:`~yatbaf.typing.Filter`.
    :param sort_filters: Pass ``False`` if you want to use your filter order.
        Default ``True``.
    :param any_filter: Pass ``True`` if matching one of the filters is enough.
        Default ``False``.
    """  # noqa: E501

    __slots__ = (
        "_fn",
        "_filters",
        "_middleware",
        "_update_type",
        "_parent",
        "_match_fn",
        "_middleware_stack",
        "_is_fallback",
    )

    def __init__(
        self,
        fn: HandlerCallable[UpdateT],
        update_type: UpdateType | str,
        *,
        middleware: Sequence[HandlerMiddleware[UpdateT]] | None = None,
        filters: Sequence[Filter[UpdateT]] | None = None,
        sort_filters: bool = True,
        any_filter: bool = False,
    ) -> None:
        self._fn = fn
        self._update_type = update_type
        self._match_fn = all if not any_filter else any
        self._parent: AbstractRouter | None = None

        self._filters: list[Filter[UpdateT]] = []
        self._is_fallback = True
        # yapf: disable
        self._middleware: list[HandlerMiddleware[UpdateT]] = ensure_unique(
            middleware or []
        )
        # yapf: enable
        self._register_filters(filters or [], sort_filters)
        self._middleware_stack: HandlerCallable[UpdateT] = self._fn

    def __repr__(self) -> str:
        return f"<Handler[type={self._update_type}]>"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Handler) and (  # yapf: disable
            other is self or (
                # type, callback and middleware is the same - handlers are
                # equal. filters don't matter.
                other._update_type == self._update_type
                and other._fn is self._fn
                and other._middleware == self._middleware
            )
        )

    async def __call__(self, update: UpdateT, /) -> None:
        """Execute middleware and handler.

        :param update: Incoming update.
        """
        await self._middleware_stack(update)

    @property
    def orig(self) -> HandlerCallable[UpdateT]:
        """Original function."""
        return self._fn

    @property
    def update_type(self) -> UpdateType | str:
        """Handler type."""
        return self._update_type

    def _register_filters(
        self, filters: Sequence[Filter[UpdateT]], sort_filters: bool
    ) -> None:
        for func in filters:
            if func not in self._filters:
                self._filters.append(func)
        if sort_filters:
            self._filters.sort(key=lambda v: v.priority)

    def _build_middleware_stack(self) -> HandlerCallable[UpdateT]:
        middleware_stack = self._fn
        router: AbstractRouter | Handler | None = self
        func: HandlerMiddleware[UpdateT] | Middleware[HandlerCallable[UpdateT]]
        while router is not None:
            middleware = cast(
                "list[HandlerMiddleware[UpdateT]]", router._middleware
            )
            for func in reversed(middleware):
                middleware_stack = func(middleware_stack)
            router = router._parent
        return middleware_stack

    def _on_registration(self) -> None:
        self._middleware_stack = self._build_middleware_stack()
        self._is_fallback = not bool(self._filters)

    def _match(self, update: UpdateT, /) -> bool:
        return self._match_fn(f.check(update) for f in self._filters)


T = TypeVar("T")
Wrapper: TypeAlias = "Callable[[HandlerCallable[T]], Handler[T]]"


@overload
def on_message(__fn: HandlerCallable[Message]) -> Handler[Message]:
    ...


@overload
def on_message(
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message]:
    ...


def on_message(
    __fn: HandlerCallable[Message] | None = None,
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message] | Handler[Message]:
    """Message handler decorator.

    Use this decorator to decorate handler for `message` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[Message]) -> Handler[Message]:
        handler: Handler[Message] = Handler(
            fn=fn,
            update_type=UpdateType.MESSAGE,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_edited_message(__fn: HandlerCallable[Message]) -> Handler[Message]:
    ...


@overload
def on_edited_message(
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message]:
    ...


def on_edited_message(
    __fn: HandlerCallable[Message] | None = None,
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message] | Handler[Message]:
    """Edited message handler decorator.

    Use this decorator to decorate handler for `edited_message` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[Message]) -> Handler[Message]:
        handler: Handler[Message] = Handler(
            fn=fn,
            update_type=UpdateType.EDITED_MESSAGE,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_message_reaction(
    __fn: HandlerCallable[MessageReactionUpdated]
) -> Handler[MessageReactionUpdated]:
    ...


@overload
def on_message_reaction(  # yapf: disable
    *,
    filters: Sequence[Filter[MessageReactionUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[MessageReactionUpdated]] | None = None,  # noqa: E501
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[MessageReactionUpdated]:
    ...


def on_message_reaction(  # yapf: disable
    __fn: HandlerCallable[MessageReactionUpdated] | None = None,
    *,
    filters: Sequence[Filter[MessageReactionUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[MessageReactionUpdated]] | None = None,  # noqa: E501
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[MessageReactionUpdated] | Handler[MessageReactionUpdated]:
    """Message reaction handler decorator.

    Use this decorator to decorate handler for `message_reaction` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[MessageReactionUpdated]
    ) -> Handler[MessageReactionUpdated]:
        handler: Handler[MessageReactionUpdated] = Handler(
            fn=fn,
            update_type=UpdateType.MESSAGE_REACTION,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_message_reaction_count(
    __fn: HandlerCallable[MessageReactionCountUpdated]
) -> Handler[MessageReactionCountUpdated]:
    ...


@overload
def on_message_reaction_count(  # yapf: disable
    *,
    filters: Sequence[Filter[MessageReactionCountUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[MessageReactionCountUpdated]] | None = None,  # noqa: E501
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[MessageReactionCountUpdated]:
    ...


def on_message_reaction_count(  # yapf: disable
    __fn: HandlerCallable[MessageReactionCountUpdated] | None = None,
    *,
    filters: Sequence[Filter[MessageReactionCountUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[MessageReactionCountUpdated]] | None = None,  # noqa: E501
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[MessageReactionCountUpdated] | Handler[MessageReactionCountUpdated]:  # noqa: E501
    """Message reaction count handler decorator.

    Use this decorator to decorate handler for `message_reaction` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[MessageReactionCountUpdated]
    ) -> Handler[MessageReactionCountUpdated]:
        handler: Handler[MessageReactionCountUpdated] = Handler(
            fn=fn,
            update_type=UpdateType.MESSAGE_REACTION_COUNT,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_channel_post(__fn: HandlerCallable[Message]) -> Handler[Message]:
    ...


@overload
def on_channel_post(
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message]:
    ...


def on_channel_post(
    __fn: HandlerCallable[Message] | None = None,
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message] | Handler[Message]:
    """Channel post handler decorator.

    Use this decorator to decorate handler for `channel_post` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[Message]) -> Handler[Message]:
        handler: Handler[Message] = Handler(
            fn=fn,
            update_type=UpdateType.CHANNEL_POST,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_edited_channel_post(__fn: HandlerCallable[Message]) -> Handler[Message]:
    ...


@overload
def on_edited_channel_post(
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message]:
    ...


def on_edited_channel_post(
    __fn: HandlerCallable[Message] | None = None,
    *,
    filters: Sequence[Filter[Message]] | None = None,
    middleware: Sequence[HandlerMiddleware[Message]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Message] | Handler[Message]:
    """Edited channel post handler decorator.

    Use this decorator to decorate handler for `edited_channel_post` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[Message]) -> Handler[Message]:
        handler: Handler[Message] = Handler(
            fn=fn,
            update_type=UpdateType.EDITED_CHANNEL_POST,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_inline_query(__fn: HandlerCallable[InlineQuery]) -> Handler[InlineQuery]:
    ...


@overload
def on_inline_query(
    *,
    filters: Sequence[Filter[InlineQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[InlineQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[InlineQuery]:
    ...


def on_inline_query(
    __fn: HandlerCallable[InlineQuery] | None = None,
    *,
    filters: Sequence[Filter[InlineQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[InlineQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[InlineQuery] | Handler[InlineQuery]:
    """Inline query handler decorator.

    Use this decorator to decorate handler for `inline_query` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[InlineQuery]) -> Handler[InlineQuery]:
        handler: Handler[InlineQuery] = Handler(
            fn=fn,
            update_type=UpdateType.INLINE_QUERY,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_chosen_inline_result(
    __fn: HandlerCallable[ChosenInlineResult]
) -> Handler[ChosenInlineResult]:
    ...


@overload
def on_chosen_inline_result(
    *,
    filters: Sequence[Filter[ChosenInlineResult]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChosenInlineResult]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChosenInlineResult]:
    ...


def on_chosen_inline_result(
    __fn: HandlerCallable[ChosenInlineResult] | None = None,
    *,
    filters: Sequence[Filter[ChosenInlineResult]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChosenInlineResult]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChosenInlineResult] | Handler[ChosenInlineResult]:
    """Chosen inline result handler decorator.

    Use this decorator to decorate handler for `chosen_inline_result` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChosenInlineResult]
    ) -> Handler[ChosenInlineResult]:
        handler: Handler[ChosenInlineResult] = Handler(
            fn=fn,
            update_type=UpdateType.CHOSEN_INLINE_RESULT,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_callback_query(
    __fn: HandlerCallable[CallbackQuery]
) -> Handler[CallbackQuery]:
    ...


@overload
def on_callback_query(
    *,
    filters: Sequence[Filter[CallbackQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[CallbackQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[CallbackQuery]:
    ...


def on_callback_query(
    __fn: HandlerCallable[CallbackQuery] | None = None,
    *,
    filters: Sequence[Filter[CallbackQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[CallbackQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[CallbackQuery] | Handler[CallbackQuery]:
    """Callback query handler decorator.

    Use this decorator to decorate handler for `callback_query` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[CallbackQuery]) -> Handler[CallbackQuery]:
        handler: Handler[CallbackQuery] = Handler(
            fn=fn,
            update_type=UpdateType.CALLBACK_QUERY,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_shipping_query(
    __fn: HandlerCallable[ShippingQuery]
) -> Handler[ShippingQuery]:
    ...


@overload
def on_shipping_query(
    *,
    filters: Sequence[Filter[ShippingQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[ShippingQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ShippingQuery]:
    ...


def on_shipping_query(
    __fn: HandlerCallable[ShippingQuery] | None = None,
    *,
    filters: Sequence[Filter[ShippingQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[ShippingQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ShippingQuery] | Handler[ShippingQuery]:
    """Shipping query handler decorator.

    Use this decorator to decorate handler for `shipping_query` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[ShippingQuery]) -> Handler[ShippingQuery]:
        handler: Handler[ShippingQuery] = Handler(
            fn=fn,
            update_type=UpdateType.SHIPPING_QUERY,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_pre_checkout_query(
    __fn: HandlerCallable[PreCheckoutQuery]
) -> Handler[PreCheckoutQuery]:
    ...


@overload
def on_pre_checkout_query(
    *,
    filters: Sequence[Filter[PreCheckoutQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[PreCheckoutQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[PreCheckoutQuery]:
    ...


def on_pre_checkout_query(
    __fn: HandlerCallable[PreCheckoutQuery] | None = None,
    *,
    filters: Sequence[Filter[PreCheckoutQuery]] | None = None,
    middleware: Sequence[HandlerMiddleware[PreCheckoutQuery]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[PreCheckoutQuery] | Handler[PreCheckoutQuery]:
    """Pre-checkout query handler decorator.

    Use this decorator to decorate handler for `pre_checkout_query` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[PreCheckoutQuery]
    ) -> Handler[PreCheckoutQuery]:
        handler: Handler[PreCheckoutQuery] = Handler(
            fn=fn,
            update_type=UpdateType.PRE_CHECKOUT_QUERY,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_poll(__fn: HandlerCallable[Poll]) -> Handler[Poll]:
    ...


@overload
def on_poll(
    *,
    filters: Sequence[Filter[Poll]] | None = None,
    middleware: Sequence[HandlerMiddleware[Poll]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Poll]:
    ...


def on_poll(
    __fn: HandlerCallable[Poll] | None = None,
    *,
    filters: Sequence[Filter[Poll]] | None = None,
    middleware: Sequence[HandlerMiddleware[Poll]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[Poll] | Handler[Poll]:
    """Poll handler decorator.

    Use this decorator to decorate handler for `poll` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[Poll]) -> Handler[Poll]:
        handler: Handler[Poll] = Handler(
            fn=fn,
            update_type=UpdateType.POLL,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_poll_answer(__fn: HandlerCallable[PollAnswer]) -> Handler[PollAnswer]:
    ...


@overload
def on_poll_answer(
    *,
    filters: Sequence[Filter[PollAnswer]] | None = None,
    middleware: Sequence[HandlerMiddleware[PollAnswer]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[PollAnswer]:
    ...


def on_poll_answer(
    __fn: HandlerCallable[PollAnswer] | None = None,
    *,
    filters: Sequence[Filter[PollAnswer]] | None = None,
    middleware: Sequence[HandlerMiddleware[PollAnswer]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[PollAnswer] | Handler[PollAnswer]:
    """Poll answer handler decorator.

    Use this decorator to decorate handler for `poll_answer` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(fn: HandlerCallable[PollAnswer]) -> Handler[PollAnswer]:
        handler: Handler[PollAnswer] = Handler(
            fn=fn,
            update_type=UpdateType.POLL_ANSWER,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_my_chat_member(
    __fn: HandlerCallable[ChatMemberUpdated]
) -> Handler[ChatMemberUpdated]:
    ...


@overload
def on_my_chat_member(
    *,
    filters: Sequence[Filter[ChatMemberUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatMemberUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatMemberUpdated]:
    ...


def on_my_chat_member(
    __fn: HandlerCallable[ChatMemberUpdated] | None = None,
    *,
    filters: Sequence[Filter[ChatMemberUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatMemberUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatMemberUpdated] | Handler[ChatMemberUpdated]:
    """My chat member handler decorator.

    Use this decorator to decorate handler for `my_chat_member` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChatMemberUpdated]
    ) -> Handler[ChatMemberUpdated]:
        handler: Handler[ChatMemberUpdated] = Handler(
            fn=fn,
            update_type=UpdateType.MY_CHAT_MEMBER,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_chat_member(
    __fn: HandlerCallable[ChatMemberUpdated]
) -> Handler[ChatMemberUpdated]:
    ...


@overload
def on_chat_member(
    *,
    filters: Sequence[Filter[ChatMemberUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatMemberUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatMemberUpdated]:
    ...


def on_chat_member(
    __fn: HandlerCallable[ChatMemberUpdated] | None = None,
    *,
    filters: Sequence[Filter[ChatMemberUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatMemberUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatMemberUpdated] | Handler[ChatMemberUpdated]:
    """Chat member handler decorator.

    Use this decorator to decorate handler for `chat_member` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChatMemberUpdated]
    ) -> Handler[ChatMemberUpdated]:
        handler: Handler[ChatMemberUpdated] = Handler(
            fn=fn,
            update_type=UpdateType.CHAT_MEMBER,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_chat_join_request(
    __fn: HandlerCallable[ChatJoinRequest]
) -> Handler[ChatJoinRequest]:
    ...


@overload
def on_chat_join_request(
    *,
    filters: Sequence[Filter[ChatJoinRequest]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatJoinRequest]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatJoinRequest]:
    ...


def on_chat_join_request(
    __fn: HandlerCallable[ChatJoinRequest] | None = None,
    *,
    filters: Sequence[Filter[ChatJoinRequest]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatJoinRequest]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatJoinRequest] | Handler[ChatJoinRequest]:
    """Chat join request handler decorator.

    Use this decorator to decorate handler for `chat_join_request` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChatJoinRequest]
    ) -> Handler[ChatJoinRequest]:
        handler: Handler[ChatJoinRequest] = Handler(
            fn=fn,
            update_type=UpdateType.CHAT_JOIN_REQUEST,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_chat_boost(
    __fn: HandlerCallable[ChatBoostUpdated]
) -> Handler[ChatBoostUpdated]:
    ...


@overload
def on_chat_boost(
    *,
    filters: Sequence[Filter[ChatBoostUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatBoostUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatBoostUpdated]:
    ...


def on_chat_boost(
    __fn: HandlerCallable[ChatBoostUpdated] | None = None,
    *,
    filters: Sequence[Filter[ChatBoostUpdated]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatBoostUpdated]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatBoostUpdated] | Handler[ChatBoostUpdated]:
    """Chat boost handler decorator.

    Use this decorator to decorate handler for `chat_boost` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChatBoostUpdated]
    ) -> Handler[ChatBoostUpdated]:
        handler: Handler[ChatBoostUpdated] = Handler(
            fn=fn,
            update_type=UpdateType.CHAT_BOOST,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)


@overload
def on_removed_chat_boost(
    __fn: HandlerCallable[ChatBoostRemoved]
) -> Handler[ChatBoostRemoved]:
    ...


@overload
def on_removed_chat_boost(
    *,
    filters: Sequence[Filter[ChatBoostRemoved]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatBoostRemoved]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatBoostRemoved]:
    ...


def on_removed_chat_boost(
    __fn: HandlerCallable[ChatBoostRemoved] | None = None,
    *,
    filters: Sequence[Filter[ChatBoostRemoved]] | None = None,
    middleware: Sequence[HandlerMiddleware[ChatBoostRemoved]] | None = None,
    sort_filters: bool = True,
    any_filter: bool = False,
) -> Wrapper[ChatBoostRemoved] | Handler[ChatBoostRemoved]:
    """Removed chat boost handler decorator.

    Use this decorator to decorate handler for `removed_chat_boost` update.

    See :class:`Handler` for parameters.
    """

    def wrapper(
        fn: HandlerCallable[ChatBoostRemoved]
    ) -> Handler[ChatBoostRemoved]:
        handler: Handler[ChatBoostRemoved] = Handler(
            fn=fn,
            update_type=UpdateType.REMOVED_CHAT_BOOST,
            filters=filters,
            middleware=middleware,
            sort_filters=sort_filters,
            any_filter=any_filter,
        )
        return handler

    if __fn is None:
        return wrapper
    return wrapper(__fn)
