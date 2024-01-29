import unittest.mock as mock

import pytest

from yatbaf.exceptions import SkipRouterException
from yatbaf.filters import Command
from yatbaf.handler import Handler
from yatbaf.middleware import Middleware
from yatbaf.router import OnMessage


def guard_true(_):
    return


def guard_false(_):
    raise SkipRouterException


@pytest.mark.asyncio
async def test_resolve_no_handlers(router, update_info):
    router._on_registration()
    assert not await router._resolve(update_info)


@pytest.mark.asyncio
async def test_resolve_catch_all(router, update_info, handler_func):
    router.add_handler(handler_func)
    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_resolve_none(router, update_info, handler_func):
    filter = Command("foo")
    router.add_handler(handler_func, filters=[filter])
    router._on_registration()
    assert not await router._resolve(update_info)
    handler_func.assert_not_awaited()


@pytest.mark.asyncio
async def test_resolve_nested_vert(update_info, handler_func):

    def find_router(router):
        r = router
        while r._routers:
            r = r._routers[-1]
        return r

    router = OnMessage()
    for _ in range(5):
        find_router(router).add_router(OnMessage())

    filter = Command("foo")
    update_info.content.text = "/foo"
    find_router(router).add_handler(handler_func, filters=[filter])
    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_resolve_nested_horiz(update_info, handler_func):
    router = OnMessage(
        routers=[
            OnMessage(
                handlers=[
                    Handler(
                        mock.AsyncMock(),
                        filters=[Command(f"bar{i}")],
                        update_type="message",
                    ),
                ]
            ) for i in range(5)
        ],
    )
    router.add_router(
        OnMessage(
            handlers=[
                Handler(
                    handler_func,
                    filters=[Command("foo")],
                    update_type="message",
                ),
            ]
        )
    )
    router._on_registration()
    update_info.content.text = "/foo"
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_guard_false(handler_func, router, update_info):
    router.add_guard(guard_false)
    router.add_handler(handler_func)
    router._on_registration()
    assert not await router._resolve(update_info)
    handler_func.assert_not_awaited()


@pytest.mark.asyncio
async def test_guard_true(handler_func, router, update_info):
    router.add_guard(guard_true)
    router.add_handler(handler_func)
    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_parent_guard_true(handler_func, update_info, asyncdef):
    router = OnMessage(
        guards=[guard_true],
        handlers=[handler_func],
        routers=[OnMessage(handlers=[asyncdef()])],
    )
    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_parent_guard_false(handler_func, update_info, asyncdef):
    router = OnMessage(
        handlers=[asyncdef()],
        guards=[guard_false],
        routers=[OnMessage(handlers=[handler_func])]
    )
    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once()


@pytest.mark.asyncio
async def test_guard_false_both(handler_func, update_info, asyncdef):
    router = OnMessage(
        guards=[guard_false],
        handlers=[asyncdef()],
        routers=[
            OnMessage(
                guards=[guard_false],
                handlers=[handler_func],
            ),
        ],
    )
    router._on_registration()
    assert not await router._resolve(update_info)
    handler_func.assert_not_awaited()


@pytest.mark.asyncio
async def test_guard_skip_nested(handler_func, update_info):
    router = OnMessage(
        routers=[
            OnMessage(
                guards=[guard_true],
                handlers=[handler_func],
            ),
        ]
    )

    @router.guard
    def _guard(_):
        raise SkipRouterException(skip_nested=True)

    router._on_registration()
    assert not await router._resolve(update_info)
    handler_func.assert_not_awaited()


# yapf: disable
def middleware_factory(mark):
    def middleware(handler):
        async def wrapper(update):
            mark()
            await handler(update)
        return wrapper
    return middleware
# yapf: enable


@pytest.mark.asyncio
async def test_resolve_wrap_router_middlewares(
    router, update_info, handler_func
):
    m = mock.Mock()
    router.add_handler(handler_func)
    for _ in range(5):
        router.add_middleware(
            Middleware(
                middleware_factory(m),
                is_handler=True,
            )
        )
    assert len(router._middleware) == 5

    router._on_registration()
    assert await router._resolve(update_info)
    handler_func.assert_awaited_once_with(update_info.content)
    assert m.call_count == 5


@pytest.mark.asyncio
async def test_resolve_wrap_handler_middlewares(
    router, handler_func, update_info
):
    m = mock.Mock()
    router.add_handler(
        handler_func,
        middleware=[middleware_factory(m) for _ in range(5)],
    )
    router._on_registration()
    assert await router._resolve(update_info)
    assert m.call_count == 5
    handler_func.assert_awaited_once_with(update_info.content)


@pytest.mark.asyncio
async def test_resolve_wrap_middlewares(router, update_info, handler_func):
    m = mock.Mock()
    router.add_handler(
        handler_func,
        middleware=[middleware_factory(m) for _ in range(5)],
    )
    for _ in range(5):
        router.add_middleware(
            Middleware(
                middleware_factory(m),
                is_handler=True,
            )
        )
    router._on_registration()
    assert await router._resolve(update_info)
    assert m.call_count == 10
    handler_func.assert_awaited_once_with(update_info.content)
