from __future__ import annotations

__all__ = (
    "OnMessage",
    "OnEditedMessage",
    "OnChannelPost",
    "OnEditedChannelPost",
    "OnMessageReaction",
    "OnMessageReactionCount",
    "OnInlineQuery",
    "OnChosenInlineResult",
    "OnCallbackQuery",
    "OnShippingQuery",
    "OnPreCheckoutQuery",
    "OnPoll",
    "OnPollAnswer",
    "OnMyChatMember",
    "OnChatMemeber",
    "OnChatJoinRequest",
    "OnChatBoost",
    "OnRemovedChatBoost",
)

import logging
from itertools import count
from typing import TYPE_CHECKING
from typing import Final
from typing import Literal
from typing import TypeAlias
from typing import TypeVar
from typing import cast
from typing import final
from typing import overload

from .abc import AbstractRouter
from .exceptions import FrozenInstanceError
from .exceptions import SkipRouterException
from .handler import Handler
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
from .typing import UpdateT
from .utils import ensure_unique
from .warnings import warn_duplicate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from .models import UpdateInfo
    from .typing import Filter
    from .typing import GuardCallable
    from .typing import HandlerCallable
    from .typing import HandlerMiddleware
    from .typing import MiddlewareType
    from .typing import RouterCallable
    from .typing import RouterMiddleware
    M = TypeVar("M", bound=RouterMiddleware | HandlerMiddleware)
else:
    M = TypeVar("M")

log = logging.getLogger(__name__)
_router_count = count(1).__next__

T = TypeVar("T")
UnionMiddlewareType: TypeAlias = (
    "Middleware[HandlerCallable[T]] "
    "| Middleware[RouterCallable[T]] "
)
InitMiddlewareType: TypeAlias = (
    "UnionMiddlewareType[T] "
    "| HandlerMiddleware[T]"
)


class BaseRouter(AbstractRouter[UpdateT]):
    """Common behaviour for :class:`Router` and
    :class:`~yatbaf.dispatcher.Dispatcher`.
    """

    __slots__ = (
        "_guards",
        "_parent",
        "_middleware",
    )

    _middleware_stack: RouterCallable[UpdateT]

    def __init__(
        self,
        guards: Sequence[GuardCallable[UpdateT]] | None = None,
        middleware: Sequence[InitMiddlewareType[UpdateT]] | None = None,
        routers: Sequence[AbstractRouter[UpdateT]] | None = None,
        handlers: Sequence[Handler[UpdateT]] | None = None,
    ) -> None:
        """
        :param guards: *Optional.* A sequence of :class:`~yatbaf.typing.Guard`.
        :param middleware: *Optional.* A sequence of :class:`~yatbaf.middleware.Middleware`
            or :class:`~yatbaf.typing.HandlerMiddleware`.
        :param routers: *Optional.* A sequence of :class:`~yatbaf.abc.AbstractRouter`.
        :param handlers: *Optional.* A sequence of :class:`~yatbaf.typing.Handler`.
        """  # noqa: E501
        self._parent = None
        self._guards: list[GuardCallable[UpdateT]] = ensure_unique(guards or [])
        self._middleware = ensure_unique([  # yapf: disable  # type: ignore[assignment]  # noqa: E501
            Middleware(m, is_handler=True)  # type: ignore[misc]
            if not isinstance(m, Middleware) else m
            for m in (middleware or [])
        ])
        self._register_routers(routers or [])
        self._register_handlers(handlers or [])

    def _register_middleware(
        self, middleware: Sequence[UnionMiddlewareType[UpdateT]]
    ) -> None:
        outer = []
        inner = []
        for obj in middleware:
            if obj.is_handler:
                inner.append(obj)
            else:
                outer.append(obj)
        for cls in reversed(cast("list[RouterMiddleware[UpdateT]]", outer)):
            self._middleware_stack = cls(self._middleware_stack)
        self._middleware = cast(
            "list[Middleware[HandlerCallable[UpdateT]]]", inner
        )

    def _check_guards(self, update: UpdateT) -> tuple[bool, bool]:
        try:
            for guard in self._guards:
                guard(update)
        except SkipRouterException as e:
            return (False, e.skip_nested)
        return (True, False)


class Router(BaseRouter[UpdateT]):
    """Base class for routers."""

    __slots__ = (
        "_routers",
        "_sort_filters",
        "_update_type",
        "_handlers",
        "_name",
        "_frozen",
        "_middleware_stack",
    )

    def __init__(
        self,
        *,
        handlers: Sequence[Handler[UpdateT]] | None = None,
        middleware: Sequence[InitMiddlewareType[UpdateT]] | None = None,
        routers: Sequence[AbstractRouter[UpdateT]] | None = None,
        guards: Sequence[GuardCallable[UpdateT]] | None = None,
        name: str | None = None,
        sort_filters: bool = True,
    ) -> None:
        """
        :param handlers: *Optional.* A sequence of :class:`~yatbaf.typing.Handler`.
        :param middleware: *Optional.* A sequence of :class:`~yatbaf.middleware.Middleware`
            or :class:`~yatbaf.typing.HandlerMiddleware`.
        :param routers: *Optional.* A sequence of :class:`~yatbaf.abc.AbstractRouter`.
        :param guards: *Optional.* A sequence of :class:`~yatbaf.typing.Guard`.
        :param name: *Optional.* Router name.
        :param sort_filters: *Optional.* Sort handler filters by priority.
        :param skip_with_nested: *Optional.* Guard will also skip nested routers.
        """  # noqa: E501
        self._sort_filters: Final[bool] = sort_filters
        self._routers: list[AbstractRouter[UpdateT]] = []
        self._handlers: list[Handler[UpdateT]] = []
        self._name: Final[str] = name if name else f"router-{_router_count()}"
        self._frozen = False
        self._middleware_stack = self.__resolve

        super().__init__(
            routers=routers,
            handlers=handlers,
            guards=guards,
            middleware=middleware,
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}[name={self._name}]>"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Router) and (  # yapf: disable
            other is self or (
                other._update_type == self._update_type
                and other._handlers == self._handlers
                and other._guards == self._guards
                and other._middleware == self._middleware
                and other._routers == self._routers
            )
        )

    @property
    def name(self) -> str:
        """Router name."""
        return self._name

    def _register_routers(
        self, routers: Sequence[AbstractRouter[UpdateT]]
    ) -> None:
        for router in routers:
            self.add_router(router)

    def _register_handlers(self, handlers: Sequence[Handler[UpdateT]]) -> None:
        for handler in handlers:
            self.add_handler(handler)

    def add_guard(self, func: GuardCallable[UpdateT], /) -> None:
        """Add a new guard function.

        :param func: :class:`Guard <yatbaf.typing.Guard>` function.
        :raises FrozenInstanceError: If you try to register a Guard after Bot
            object has been initialized.
        """
        if self._frozen:
            raise FrozenInstanceError(
                "It is not possible to add a new Guard at runtime "
                "after Bot object has been initialized."
            )

        if func not in self._guards:
            self._guards.append(func)

    def add_middleware(
        self,
        func: HandlerMiddleware[UpdateT] | RouterMiddleware[UpdateT],
        *,
        is_handler: bool = True,
        is_local: bool = False,
    ) -> None:
        """Add a new middleware.

        Add a new middleware which will be applied to all handlers in router.
        Function must return a new Handler functoin. Usage::

            def middleware(handler: Handler) -> Handler:
                async def wrapper(update: UpdateT) -> None:
                    await handler(update)
                return wrapper

            router.add_middleware(middleware)

        :param func: :class:`Middleware <yatbaf.types.Middleware>` function.
        :param is_handler: *Optional.* Pass ``False`` if it is an router
            middleware.
        :param is_local: *Optional.* Pass ``True`` if it is a middleware only
            for handlers in current router. For handler middleware only
            (``is_handler``=``True``).
        :raises FrozenInstanceError: If you try to register a Middleware after
            Bot object has been initialized.
        """
        if self._frozen:
            raise FrozenInstanceError(
                "It is not possible to add a new Middleware at runtime "
                "after Bot object has been initialized."
            )

        middleware = cast(
            "Middleware[RouterCallable[UpdateT]] | Middleware[HandlerCallable[UpdateT]]",  # noqa: E501
            Middleware(
                func,
                is_handler=is_handler,
                is_local=is_local,
            )
        )

        # skip duplicate
        if middleware not in self._middleware:
            self._middleware.append(middleware)  # type: ignore[arg-type]

    @overload
    def add_handler(self, handler: Handler[UpdateT]) -> None:
        ...

    @overload
    def add_handler(
        self,
        handler: HandlerCallable[UpdateT],
        *,
        filters: Sequence[Filter[UpdateT]] | None = None,
        middleware: Sequence[HandlerMiddleware[UpdateT]] | None = None,
        sort_filters: bool | None = None,
        any_filter: bool = False,
    ) -> None:
        ...

    def add_handler(
        self,
        handler: HandlerCallable[UpdateT] | Handler[UpdateT],
        *,
        filters: Sequence[Filter[UpdateT]] | None = None,
        middleware: Sequence[HandlerMiddleware[UpdateT]] | None = None,
        sort_filters: bool | None = None,
        any_filter: bool = False,
    ) -> None:
        """Use this method to register a new handler.

        :param handler: :class:`~yatbaf.handler.Handler` instance or function.
        :param filters: *Optional.* A sequence of :class:`~yatbaf.typing.Filter`.
        :param middleware: *Optional.* A sequence of :class:`~yatbaf.typing.HandlerMiddleware`.
        :param sort_filters: *Optional.* Pass ``False`` if you want to use your
            filter order. Default to :attr:`Router.sort_filters`.
        :param any_filter: Pass ``True`` if matching one of the filters is enough.
        :raises FrozenInstanceError: If you try to register a Handler after Bot
            object has been initialized.
        """  # noqa: E501
        if self._frozen:
            raise FrozenInstanceError(
                f"{self!r} is frozen. It is not possible to add a new Handler "
                "at runtime after Bot object has been initialized."
            )

        if not isinstance(handler, Handler):
            handler = Handler(
                fn=handler,
                update_type=self._update_type,
                filters=filters,
                middleware=middleware,
                sort_filters=(  # yapf: disable
                    self._sort_filters
                    if sort_filters is None
                    else sort_filters
                ),
                any_filter=any_filter,
            )

        if handler.update_type != self._update_type:
            raise ValueError(
                f"Wrong handler type! Cannot add {handler!r} to {self!r}"
            )

        parent = handler._parent
        if parent is not None and parent is not self:
            raise ValueError(f"{handler!r} alredy registered in {parent!r}")

        # skip duplicate
        if parent or handler in self._handlers:
            warn_duplicate(handler, self)
            return

        self._handlers.append(handler)
        handler._parent = self

    @overload
    def __call__(  # yapf: disable
        self, __fn: HandlerCallable[UpdateT], /
    ) -> HandlerCallable[UpdateT]:
        ...

    @overload
    def __call__(
        self,
        *,
        filters: Sequence[Filter[UpdateT]] | None = None,
        middleware: Sequence[HandlerMiddleware[UpdateT]] | None = None,
        sort_filters: bool | None = None,
        any_filter: bool = False,
    ) -> HandlerMiddleware[UpdateT]:
        ...

    def __call__(
        self,
        __fn: HandlerCallable[UpdateT] | None = None,
        *,
        filters: Sequence[Filter[UpdateT]] | None = None,
        middleware: Sequence[HandlerMiddleware[UpdateT]] | None = None,
        sort_filters: bool | None = None,
        any_filter: bool = False,
    ) -> HandlerMiddleware[UpdateT] | HandlerCallable[UpdateT]:
        """Handler decorator.

        See :meth:`add_handler`.

        Use this decorator to register a new handler::

            @router
            async def handler(update):
                ...

            @router(filters=[filter1, filter2])
            async def handler(update):
                ...
        """

        def wrapper(fn: HandlerCallable[UpdateT]) -> HandlerCallable[UpdateT]:
            self.add_handler(
                handler=fn,
                filters=filters,
                middleware=middleware,
                sort_filters=sort_filters,
                any_filter=any_filter,
            )
            return fn

        if __fn is not None:
            return wrapper(__fn)
        return wrapper

    def add_router(self, router: AbstractRouter[UpdateT], /) -> None:
        """Use this method to add a nested router.

        .. warning::

            The nested router must handle the same type of updates as the
            current one.

        :param router: :class:`~yatbaf.abc.AbstractRouter` instance.
        :raises ValueError: If ``router`` already registered in another router
            or router type is different.
        :raises FrozenInstanceError: If you try to register a Router after Bot
            object has been initialized.
        """
        if self._frozen:
            raise FrozenInstanceError(
                f"{self!r} is frozen. It is not possible to add a new Router "
                "at runtime after Bot object has been initialized."
            )

        if self._update_type != router._update_type:
            raise ValueError(
                f"Wrong router type! Cannot add {router!r} to {self!r}"
            )

        if router is self:
            raise ValueError(f"It is not possible to add {router!r} to itself.")

        parent = router._parent
        if parent is not None and parent is not self:
            raise ValueError(f"{router!r} already registered in {parent!r}")

        if parent or router in self._routers:
            warn_duplicate(router, self)
            return

        self._routers.append(router)
        router._parent = self

    def _find_handler(self, update: UpdateT) -> Handler[UpdateT] | None:
        result: Handler[UpdateT] | None = None
        for handler in self._handlers:
            if handler._match(update):
                if not handler._is_fallback:
                    return handler
                result = handler
        return result

    async def __resolve(self, update: UpdateInfo[UpdateT], /) -> bool:
        content = update.content
        guard, skip_nested = self._check_guards(content)
        if guard:
            if (handler := self._find_handler(content)) is not None:
                await handler(content)
                return True

        # guard failed
        elif skip_nested:
            return False

        # try to find the handler in nested routers
        for router in self._routers:
            if await router._resolve(update):
                return True

        return False

    async def _resolve(self, update: UpdateInfo[UpdateT], /) -> bool:
        return await self._middleware_stack(update)

    @overload
    def middleware(
        self, __fn: HandlerMiddleware[UpdateT]
    ) -> HandlerMiddleware[UpdateT]:
        ...

    @overload
    def middleware(
        self,
        *,
        is_handler: bool = False,
    ) -> MiddlewareType[RouterMiddleware[UpdateT]]:
        ...

    @overload
    def middleware(
        self,
        *,
        is_local: bool,
        is_handler: bool = True,
    ) -> MiddlewareType[HandlerMiddleware[UpdateT]]:  # noqa: E501
        ...

    def middleware(
        self,
        __fn: HandlerMiddleware[UpdateT] | None = None,
        *,
        is_handler: bool = True,
        is_local: bool = False,
    ) -> (  # yapf: disable
        MiddlewareType[HandlerMiddleware[UpdateT]]
        | MiddlewareType[RouterMiddleware[UpdateT]]
        | HandlerMiddleware[UpdateT]
    ):
        """Middleware decorator.

        Use this decorator to register a middleware for router::

            @router.middleware
            def middleware(handler):
                async def wrapper(update):
                    await handler(update)
                return wrapper
        """

        def wrapper(
            __fn: RouterMiddleware[UpdateT] | HandlerMiddleware[UpdateT]
        ) -> RouterMiddleware[UpdateT] | HandlerMiddleware[UpdateT]:
            self.add_middleware(
                __fn,
                is_handler=is_handler,
                is_local=is_local,
            )
            return __fn

        if __fn is not None:
            return cast("HandlerMiddleware[UpdateT]", wrapper(__fn))
        return cast(
            "MiddlewareType[RouterMiddleware[UpdateT]] | MiddlewareType[HandlerMiddleware[UpdateT]]",  # noqa: E501
            wrapper
        )

    def guard(self, fn: GuardCallable[UpdateT], /) -> GuardCallable[UpdateT]:
        """Guard decorator.

        Use this decorator to register a guard for router::

            @router.guard
            async def guard(update):
                return True
        """
        self.add_guard(fn)
        return fn

    def _on_registration(self) -> None:
        self._frozen = True
        self._register_middleware(self._middleware)

        middleware = []
        local_middleware = []
        for obj in self._middleware:
            if obj.is_local:
                local_middleware.append(obj)
            else:
                middleware.append(obj)
        self._middleware = middleware + local_middleware

        for handler in self._handlers:
            handler._on_registration()
        self._middleware = middleware

        for router in self._routers:
            router._on_registration()


@final
class OnMessage(Router[Message]):
    """message router.

    See :attr:`Update.message <yatbaf.types.update.Update.message>`
    """

    __slots__ = ()
    _update_type: Literal["message"] = "message"


@final
class OnEditedMessage(Router[Message]):
    """edited_message router.

    See :attr:`Update.edited_message <yatbaf.types.update.Update.edited_message>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["edited_message"] = "edited_message"


@final
class OnChannelPost(Router[Message]):
    """channel_post router.

    See :attr:`Update.channel_post <yatbaf.types.update.Update.channel_post>`
    """

    __slots__ = ()
    _update_type: Literal["channel_post"] = "channel_post"


@final
class OnEditedChannelPost(Router[Message]):
    """edited_channel_post router.

    See :attr:`Update.edited_channel_post <yatbaf.types.update.Update.edited_channel_post>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["edited_channel_post"] = "edited_channel_post"


@final
class OnMessageReaction(Router[MessageReactionUpdated]):
    """message_reaction router.

    See :attr:`Update.message_reaction <yatbaf.types.update.Update.message_reaction>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["message_reaction"] = "message_reaction"


@final
class OnMessageReactionCount(Router[MessageReactionCountUpdated]):
    """message_reaction router.

    See :attr:`Update.message_reaction_count <yatbaf.types.update.Update.message_reaction_count>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["message_reaction_count"] = "message_reaction_count"


@final
class OnInlineQuery(Router[InlineQuery]):
    """inline_query router.

    See :attr:`Update.inline_query <yatbaf.types.update.Update.inline_query>`
    """

    __slots__ = ()
    _update_type: Literal["inline_query"] = "inline_query"


@final
class OnChosenInlineResult(Router[ChosenInlineResult]):
    """chosen_inline_result router.

    See :attr:`Update.chosen_inline_result <yatbaf.types.update.Update.chosen_inline_result>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["chosen_inline_result"] = "chosen_inline_result"


@final
class OnCallbackQuery(Router[CallbackQuery]):
    """callback_query router.

    See :attr:`Update.callback_query <yatbaf.types.update.Update.callback_query>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["callback_query"] = "callback_query"


@final
class OnShippingQuery(Router[ShippingQuery]):
    """shipping_query router.

    See :attr:`Update.shipping_query <yatbaf.types.update.Update.shipping_query>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["shipping_query"] = "shipping_query"


@final
class OnPreCheckoutQuery(Router[PreCheckoutQuery]):
    """pre_checkout_query router.

    See :attr:`Update.pre_checkout_query <yatbaf.types.update.Update.pre_checkout_query>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["pre_checkout_query"] = "pre_checkout_query"


@final
class OnPoll(Router[Poll]):
    """poll router.

    See :attr:`Update.poll <yatbaf.types.update.Update.poll>`
    """

    __slots__ = ()
    _update_type: Literal["poll"] = "poll"


@final
class OnPollAnswer(Router[PollAnswer]):
    """poll_answer router.

    See :attr:`Update.poll_answer <yatbaf.types.update.Update.poll_answer>`
    """

    __slots__ = ()
    _update_type: Literal["poll_answer"] = "poll_answer"


@final
class OnMyChatMember(Router[ChatMemberUpdated]):
    """my_chat_member router.

    See :attr:`Update.my_chat_member <yatbaf.types.update.Update.my_chat_member>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["my_chat_member"] = "my_chat_member"


@final
class OnChatMemeber(Router[ChatMemberUpdated]):
    """chat_member router.

    See :attr:`Update.chat_member <yatbaf.types.update.Update.chat_member>`
    """

    __slots__ = ()
    _update_type: Literal["chat_member"] = "chat_member"


@final
class OnChatJoinRequest(Router[ChatJoinRequest]):
    """chat_join_request router.

    See :attr:`Update.chat_join_request <yatbaf.types.update.Update.chat_join_request>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["chat_join_request"] = "chat_join_request"


@final
class OnChatBoost(Router[ChatBoostUpdated]):
    """chat_boost router.

    See :attr:`Update.chat_boost <yatbaf.types.update.Update.chat_boost>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["chat_boost"] = "chat_boost"


@final
class OnRemovedChatBoost(Router[ChatBoostRemoved]):
    """removed_chat_boost router.

    See :attr:`Update.removed_chat_boost <yatbaf.types.update.Update.removed_chat_boost>`
    """  # noqa: E501

    __slots__ = ()
    _update_type: Literal["removed_chat_boost"] = "removed_chat_boost"


router_map: dict[str, type[BaseRouter]] = {
    "message": OnMessage,
    "edited_message": OnEditedMessage,
    "channel_post": OnChannelPost,
    "edited_channel_post": OnEditedChannelPost,
    "message_reaction": OnMessageReaction,
    "message_reaction_count": OnMessageReactionCount,
    "inline_query": OnInlineQuery,
    "chosen_inline_result": OnChosenInlineResult,
    "callback_query": OnCallbackQuery,
    "shipping_query": OnShippingQuery,
    "pre_checkout_query": OnPreCheckoutQuery,
    "poll": OnPoll,
    "poll_answer": OnPollAnswer,
    "my_chat_member": OnMyChatMember,
    "chat_member": OnChatMemeber,
    "chat_join_request": OnChatJoinRequest,
    "chat_boost": OnChatBoost,
    "removed_chat_boost": OnRemovedChatBoost,
}
