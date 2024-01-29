from yatbaf.filters import Channel
from yatbaf.filters import Command
from yatbaf.filters import Content
from yatbaf.filters import User
from yatbaf.router import OnMessage


def test_sort_filters_router_true():
    user = User(123)
    channel = Channel()
    command = Command("start")
    content = Content("text")

    router = OnMessage()
    router.add_handler(
        object(), filters=[
            content,
            command,
            user,
            channel,
        ]
    )
    assert router._handlers[0]._filters == [channel, user, content, command]


def test_sort_filters_router_true_func_false():
    user = User(123)
    channel = Channel()
    command = Command("start")
    content = Content("text")

    router = OnMessage()
    router.add_handler(
        object(),
        filters=[
            content,
            command,
            user,
            channel,
        ],
        sort_filters=False,
    )
    assert router._handlers[0]._filters == [content, command, user, channel]


def test_sort_filters_router_false():
    user = User(123)
    channel = Channel()
    command = Command("start")
    content = Content("text")

    router = OnMessage(sort_filters=False)
    router.add_handler(
        object(), filters=[
            content,
            command,
            user,
            channel,
        ]
    )
    assert router._handlers[0]._filters == [content, command, user, channel]


def test_sort_filters_router_false_func_true():
    user = User(123)
    channel = Channel()
    command = Command("start")
    content = Content("text")

    router = OnMessage(sort_filters=False)
    router.add_handler(
        object(),
        filters=[
            content,
            command,
            user,
            channel,
        ],
        sort_filters=True,
    )
    assert router._handlers[0]._filters == [channel, user, content, command]
