import unittest.mock as mock

import pytest

from yatbaf.enums import UpdateType
from yatbaf.exceptions import BotWarning
from yatbaf.filters import Command
from yatbaf.handler import Handler
from yatbaf.router import OnMessage


def test_add_handler(router, handler_func):
    router.add_handler(handler_func)
    assert isinstance(router._handlers[0], Handler)
    assert router._handlers[0]._fn is handler_func
    assert router._handlers[0]._parent is router


def test_add_handler_obj(router, handler_func):
    handler = Handler(handler_func, UpdateType.MESSAGE)
    router.add_handler(handler)
    assert router._handlers[0] is handler


def test_add_handler_type_error(router, handler_func):
    handler = Handler(handler_func, UpdateType.POLL)
    with pytest.raises(ValueError):
        router.add_handler(handler)


def test_add_handler_registered(handler_func):
    handler = Handler(handler_func, UpdateType.MESSAGE)
    _ = OnMessage(handlers=[handler])
    with pytest.raises(ValueError):
        OnMessage(handlers=[handler])


def test_add_handler_registered_same_router(handler_func):
    handler = Handler(handler_func, UpdateType.MESSAGE)
    router = OnMessage(handlers=[handler])
    with pytest.warns(BotWarning):
        router.add_handler(handler)
    assert len(router._handlers) == 1


def test_add_handler_duplicate_func(router, handler_func, filter):
    handler1 = Handler(handler_func, UpdateType.MESSAGE)
    handler2 = Handler(handler_func, UpdateType.MESSAGE, filters=[filter])
    router.add_handler(handler1)
    with pytest.warns(BotWarning):
        router.add_handler(handler2)
    assert len(router._handlers) == 1
    assert router._handlers[0] is handler1


def test_add_handler_duplicate_func1(router, handler_func, filter):
    handler1 = Handler(handler_func, UpdateType.MESSAGE)
    router.add_handler(handler1)
    with pytest.warns(BotWarning):
        router.add_handler(handler_func, filters=[filter])
    assert len(router._handlers) == 1
    assert router._handlers[0] is handler1


def test_add_handler_duplicate_func2(router, handler_func, filter):
    router.add_handler(handler_func)
    with pytest.warns(BotWarning):
        router.add_handler(handler_func, filters=[filter])
    assert len(router._handlers) == 1
    assert not router._handlers[0]._filters


def test_add_handler_decorator(router):

    @router
    async def handler(_):  # noqa: U101
        pass

    assert isinstance(router._handlers[0], Handler)
    assert router._handlers[0]._fn is handler


def test_add_handler_decorator_duplicate(router):

    with pytest.warns(UserWarning):

        @router
        @router
        async def handler(_):  # noqa: U101
            pass

    assert isinstance(router._handlers[0], Handler)
    assert len(router._handlers) == 1
    assert router._handlers[0]._fn is handler


def test_handler_decorator_filter(router):
    filter = Command("foo")

    @router(filters=[filter])
    async def handler(_):  # noqa: U101
        pass

    assert isinstance(router._handlers[0], Handler)
    assert router._handlers[0]._fn is handler
    assert filter in router._handlers[0]._filters


def test_handler_decorator_middleware(router):
    middleware = mock.Mock()

    @router(middleware=[middleware])
    async def handler(_):  # noqa: U101
        pass

    assert isinstance(router._handlers[0], Handler)
    assert router._handlers[0]._fn is handler
    assert middleware in router._handlers[0]._middleware


def test_handler_decorator_middleware_filter_mix(router, filter):
    middleware = mock.Mock()

    @router(
        middleware=[middleware],
        filters=[filter],
    )
    async def handler(_) -> None:  # noqa: U101
        pass

    assert isinstance(router._handlers[0], Handler)
    assert router._handlers[0]._fn is handler
    assert middleware in router._handlers[0]._middleware
    assert filter in router._handlers[0]._filters
