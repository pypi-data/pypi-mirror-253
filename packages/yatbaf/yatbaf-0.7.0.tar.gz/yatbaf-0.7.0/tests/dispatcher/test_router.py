import pytest

from yatbaf.dispatcher import Dispatcher
from yatbaf.enums import UpdateType
from yatbaf.exceptions import BotWarning
from yatbaf.router import OnEditedChannelPost
from yatbaf.router import OnEditedMessage
from yatbaf.router import OnMessage
from yatbaf.router import OnPoll


def test_routers(token):
    dispatcher = Dispatcher(token)
    for type_ in UpdateType:
        dispatcher._routers[type_]


def test_add_router(token, router):
    dispatcher = Dispatcher(token, routers=[router])
    assert len(routers := dispatcher._routers[router._update_type]) == 1
    assert routers[0] is router
    assert router._parent is dispatcher


def test_add_router_duplicate_same_object(token):
    router = OnMessage()
    with pytest.warns(BotWarning):
        dispatcher = Dispatcher(
            token,
            routers=[
                router,
                router,
            ],
        )
    assert len(routers := dispatcher._routers[router._update_type]) == 1
    assert router in routers


def test_add_router_duplicate_equal_objects(token):
    router1 = OnMessage(name="router1")
    router2 = OnMessage(name="router1")
    with pytest.warns(BotWarning):
        dispatcher = Dispatcher(
            token,
            routers=[
                router1,
                router2,
            ],
        )
    assert len(routers := dispatcher._routers["message"]) == 1
    assert routers[0] is router1


def test_add_routers(token):
    dispatcher = Dispatcher(
        token,
        routers=[
            message := OnMessage(),
            poll := OnPoll(),
            edited_message := OnEditedMessage(),
            edited_post := OnEditedChannelPost(),
        ],
    )
    assert message in dispatcher._routers["message"]
    assert poll in dispatcher._routers["poll"]
    assert edited_message in dispatcher._routers["edited_message"]
    assert edited_post in dispatcher._routers["edited_channel_post"]


def test_add_router_registered(token):
    router = OnMessage()
    nested = OnMessage()
    router.add_router(nested)
    with pytest.raises(ValueError):
        Dispatcher(
            token,
            routers=[
                router,
                nested,
            ],
        )
