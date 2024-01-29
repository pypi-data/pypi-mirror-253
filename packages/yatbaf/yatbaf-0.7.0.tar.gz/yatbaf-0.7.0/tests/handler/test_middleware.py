import unittest.mock as mock

from yatbaf.enums import UpdateType
from yatbaf.handler import Handler
from yatbaf.router import OnMessage


def test_middleware(handler_func):
    middleware = mock.Mock()
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        middleware=[middleware],
    )
    assert middleware in handler._middleware


def test_wrap_middlewares(handler_func):
    middleware = mock.Mock(return_value=(func := mock.AsyncMock()))
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        middleware=[middleware],
    )
    assert handler._build_middleware_stack() is func


def test_wrap_middlewares_empty(handler_func):
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
    )
    assert handler._build_middleware_stack() is handler_func


def test_wrap_middleware_order(handler_func):
    middleware1 = mock.Mock(return_value=(func1 := mock.AsyncMock()))
    middleware2 = mock.Mock()
    middleware3 = mock.Mock()
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        middleware=[
            middleware1,
            middleware2,
            middleware3,
        ],
    )
    assert handler._build_middleware_stack() is func1


def test_wrap_middleware_parent(handler_func):
    middleware1 = mock.Mock(return_value=(func1 := mock.AsyncMock()))
    middleware2 = mock.Mock()
    middleware3 = mock.Mock()
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        middleware=[
            middleware2,
            middleware3,
        ],
    )
    _ = OnMessage(
        middleware=[middleware1],
        handlers=[handler],
    )
    assert handler._build_middleware_stack() is func1
