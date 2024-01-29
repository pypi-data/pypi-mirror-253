import pytest

from yatbaf.dispatcher import Dispatcher
from yatbaf.enums import UpdateType
from yatbaf.handler import Handler


def test_add_handler(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            Handler(handler_func, UpdateType.MESSAGE),
        ],
    )
    assert dispatcher._routers["message"]
    assert len(dispatcher._routers["message"]) == 1


def test_duplicate_equal_objects(token, handler_func):
    with pytest.warns(UserWarning):
        dispatcher = Dispatcher(
            token,
            handlers=[
                Handler(handler_func, UpdateType.MESSAGE),
                Handler(handler_func, UpdateType.MESSAGE),
            ],
        )
    assert dispatcher._routers["message"]
    assert len(dispatcher._routers["message"]) == 1


def test_duplicate_same_object(token, handler_func):
    handler = Handler(handler_func, UpdateType.MESSAGE)
    with pytest.warns(UserWarning):
        dispatcher = Dispatcher(
            token,
            handlers=[
                handler,
                handler,
            ],
        )
    assert dispatcher._routers["message"]
    assert len(dispatcher._routers["message"]) == 1


def test_order(token):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h1 := Handler(object(), UpdateType.MESSAGE),
            h3 := Handler(object(), UpdateType.MESSAGE),
            h2 := Handler(object(), UpdateType.MESSAGE),
        ]
    )
    assert len(dispatcher._routers["message"]) == 1
    assert len(dispatcher._routers["message"][-1]._handlers) == 3
    assert dispatcher._routers["message"][-1]._handlers[0] is h1
    assert dispatcher._routers["message"][-1]._handlers[1] is h3
    assert dispatcher._routers["message"][-1]._handlers[2] is h2


def test_add_handler_message(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.MESSAGE),
        ],
    )
    assert dispatcher._routers["message"][-1]._handlers[0] is h


def test_add_handler_edited_message(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.EDITED_MESSAGE),
        ],
    )
    assert dispatcher._routers["edited_message"][-1]._handlers[0] is h


def test_add_handler_channel_post(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CHANNEL_POST),
        ],
    )
    assert dispatcher._routers["channel_post"][-1]._handlers[0] is h


def test_add_handler_edited_channel_post(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.EDITED_CHANNEL_POST),
        ],
    )
    assert dispatcher._routers["edited_channel_post"][-1]._handlers[0] is h


def test_add_handler_inline_query(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.INLINE_QUERY),
        ],
    )
    assert dispatcher._routers["inline_query"][-1]._handlers[0] is h


def test_add_handler_chosen_inline_result(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CHOSEN_INLINE_RESULT),
        ],
    )
    assert dispatcher._routers["chosen_inline_result"][-1]._handlers[0] is h


def test_add_handler_callback_query(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CALLBACK_QUERY),
        ],
    )
    assert dispatcher._routers["callback_query"][-1]._handlers[0] is h


def test_add_handler_shipping_query(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.SHIPPING_QUERY),
        ],
    )
    assert dispatcher._routers["shipping_query"][-1]._handlers[0] is h


def test_add_handler_pre_checkout_query(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.PRE_CHECKOUT_QUERY),
        ],
    )
    assert dispatcher._routers["pre_checkout_query"][-1]._handlers[0] is h


def test_add_handler_poll(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.POLL),
        ],
    )
    assert dispatcher._routers["poll"][-1]._handlers[0] is h


def test_add_handler_poll_answer(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.POLL_ANSWER),
        ],
    )
    assert dispatcher._routers["poll_answer"][-1]._handlers[0] is h


def test_add_handler_my_chat_member(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.MY_CHAT_MEMBER),
        ],
    )
    assert dispatcher._routers["my_chat_member"][-1]._handlers[0] is h


def test_add_handler_chat_member(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CHAT_MEMBER),
        ],
    )
    assert dispatcher._routers["chat_member"][-1]._handlers[0] is h


def test_add_handler_chat_join_request(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CHAT_JOIN_REQUEST),
        ],
    )
    assert dispatcher._routers["chat_join_request"][-1]._handlers[0] is h


def test_add_handler_message_reaction(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.MESSAGE_REACTION),
        ],
    )
    assert dispatcher._routers["message_reaction"][-1]._handlers[0] is h


def test_add_handler_message_reaction_count(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.MESSAGE_REACTION_COUNT),
        ],
    )
    assert dispatcher._routers["message_reaction_count"][-1]._handlers[0] is h


def test_add_handler_chat_boost(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.CHAT_BOOST),
        ],
    )
    assert dispatcher._routers["chat_boost"][-1]._handlers[0] is h


def test_add_handler_removed_chat_boost(token, handler_func):
    dispatcher = Dispatcher(
        token,
        handlers=[
            h := Handler(handler_func, UpdateType.REMOVED_CHAT_BOOST),
        ],
    )
    assert dispatcher._routers["removed_chat_boost"][-1]._handlers[0] is h
