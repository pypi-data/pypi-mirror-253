import unittest.mock as mock

from yatbaf.enums import UpdateType
from yatbaf.filters import Command
from yatbaf.handler import Handler


def test_empty_router(router, message):
    router._on_registration()
    assert router._find_handler(message) is None


def test_handler_no_filters(router, message, handler):
    router.add_handler(handler)
    router._on_registration()
    assert router._find_handler(message) is handler


def test_fallback_handler(router, message):
    fallback = Handler(object(), update_type=UpdateType.MESSAGE)
    router.add_handler(fallback)
    router.add_handler(object(), filters=[Command("foo")])
    router._on_registration()
    message.text = "/bar"
    assert router._find_handler(message) is fallback


def test_filter(router, message):
    router._handlers = [
        Handler(
            object(),
            filters=[Command("ewq")],
            update_type=UpdateType.MESSAGE,
        ),
        handler := Handler(
            object(),
            filters=[Command("foo")],
            update_type=UpdateType.MESSAGE,
        ),
        handler_mock := mock.Mock(),
    ]
    router._on_registration()
    message.text = "/foo"
    assert router._find_handler(message) is handler
    handler_mock._match.assert_not_called()
