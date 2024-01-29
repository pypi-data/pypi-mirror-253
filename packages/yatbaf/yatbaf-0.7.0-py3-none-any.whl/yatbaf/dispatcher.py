from __future__ import annotations

__all__ = ("Dispatcher",)

import logging
from collections import defaultdict
from typing import TYPE_CHECKING
from typing import Any

from .enums import BotEnvi
from .models import UpdateInfo
from .router import BaseRouter
from .router import router_map
from .telegram import TelegramClient
from .utils import decode_webhook
from .utils import extract_bot_id
from .warnings import warn_duplicate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from .abc import AbstractClient
    from .abc import AbstractRouter
    from .handler import Handler
    from .methods.abc import TelegramMethod
    from .middleware import Middleware
    from .types import Update
    from .typing import GuardCallable
    from .typing import HandlerMiddleware
    from .typing import ResultModelT

log = logging.getLogger(__name__)


class Dispatcher(BaseRouter):
    """Dispatcher"""

    __slots__ = (
        "_api_client",
        "_id",
        "_routers",
        "_ctx",
        "_middleware_stack",
    )

    def __init__(
        self,
        token: str,
        handlers: Sequence[Handler] | None = None,
        routers: Sequence[AbstractRouter] | None = None,
        middleware: Sequence[Middleware | HandlerMiddleware] | None = None,
        guards: Sequence[GuardCallable] | None = None,
        api_url: str | None = None,
        environment: BotEnvi | None = None,
        client: AbstractClient | None = None,
    ) -> None:
        """
        :param token: Bot API token.
        :param middleware: *Optional.* A sequence of :class:`~yatbaf.middleware.Middleware`
            or :class:`~yatbaf.typing.HandlerMiddleware`.
        :param guards: *Optional.* A sequence of :class:`~yatbaf.typing.Guard`.
        :param handlers: *Optional.* A sequence of :class:`~yatbaf.handler.Handler`.
        :param routers: *Optional.* A sequence of :class:`~yatbaf.abc.AbstractRouter`.
        :param api_url: *Optional.* Api server address. Defautl to :attr:`~yatbaf.telegram.SERVER_URL`.
        :param environment: *Optional.* Bot environment (see :class:`~yatbaf.enums.BotEnvi`).
        :param client: *Optional.* Http client.
        """  # noqa: E501
        self._api_client = TelegramClient(
            token=token,
            api_url=api_url,
            environment=environment,
            client=client,
        )
        self._routers: dict[str, list[AbstractRouter]] = {
            "message": [],
            "edited_message": [],
            "channel_post": [],
            "edited_channel_post": [],
            "message_reaction": [],
            "message_reaction_count": [],
            "inline_query": [],
            "chosen_inline_result": [],
            "callback_query": [],
            "shipping_query": [],
            "pre_checkout_query": [],
            "poll": [],
            "poll_answer": [],
            "my_chat_member": [],
            "chat_member": [],
            "chat_join_request": [],
            "chat_boost": [],
            "removed_chat_boost": [],
        }
        self._id = extract_bot_id(token)
        self._ctx: dict[str, Any] = {}
        self._middleware_stack = self.__resolve

        super().__init__(
            routers=routers,
            handlers=handlers,
            middleware=middleware,
            guards=guards,
        )
        self._on_registration()

    @property
    def id(self) -> int:  # noqa: A003
        """Bot ID"""
        return self._id

    @property
    def ctx(self) -> dict[str, Any]:
        """Dict object.

        Use it to store extra state on bot instance.
        """
        return self._ctx

    @property
    def _update_type(self) -> str:
        raise RuntimeError(
            "Dispatcher can't be used here. "
            "You are trying to do something illegal ._."
        )

    def _register_routers(self, routers: Sequence[AbstractRouter]) -> None:
        for router in routers:
            parent = router._parent
            if parent is not None and parent is not self:
                raise ValueError(f"{router!r} already registered in {parent!r}")

            router_list = self._routers[router._update_type]
            if parent or router in router_list:
                warn_duplicate(router, self)
                continue

            router_list.append(router)
            router._parent = self

    def _register_handlers(self, handlers: Sequence[Handler]) -> None:
        routers: dict[str, list[Handler]] = defaultdict(list)
        for handler in handlers:
            routers[handler.update_type].append(handler)

        self._register_routers([
            router_map[t](handlers=h) for t, h in routers.items()
        ])

    def _bind_self(self, update: ResultModelT, /) -> ResultModelT:
        raise NotImplementedError()

    def _on_registration(self) -> None:
        self._register_middleware(self._middleware)
        for routers in self._routers.values():
            for router in routers:
                router._on_registration()

    async def _call_api(
        self, method: TelegramMethod[ResultModelT]
    ) -> ResultModelT:
        """:meta private:"""
        return self._bind_self((await self._api_client.invoke(method)).result)

    async def __resolve(self, update: UpdateInfo, /) -> bool:
        """:meta private:"""
        content = update.content
        if self._check_guards(content)[0]:
            routers = self._routers[update.name]
            for router in routers:
                if await router._resolve(update):
                    return True
        return False

    async def _resolve(self, update: UpdateInfo, /) -> bool:
        return await self._middleware_stack(update)

    async def process_update(self, data: Update | bytes, /) -> None:
        """Process incoming update.

        :param data: :class:`~yatbaf.types.update.Update` instance (long
            polling) or :class:`bytes` (webhook content).
        """
        # catch any exceptions in guard/middleware/handler
        try:
            if isinstance(data, bytes):
                data = decode_webhook(data)

            content, name = data.filter()
            await self._resolve(
                UpdateInfo(
                    id=data.update_id,
                    name=name,
                    content=self._bind_self(content),
                )
            )

        except Exception as error:
            log.error("Unexpected error!", exc_info=error)

    async def shutdown(self) -> None:
        """Cleanup resources."""
        log.debug("bot shutting down...")
        # close http client
        await self._api_client.close()
