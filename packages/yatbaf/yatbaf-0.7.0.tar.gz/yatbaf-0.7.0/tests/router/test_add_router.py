import pytest

from yatbaf.dispatcher import Dispatcher
from yatbaf.exceptions import BotWarning
from yatbaf.router import OnMessage
from yatbaf.router import OnPoll


def test_add_router():
    router = OnMessage()
    nested = OnMessage()
    router.add_router(nested)
    assert len(router._routers) == 1
    assert router._routers[0] is nested
    assert nested._parent is router


def test_add_router_self(router):
    with pytest.raises(ValueError):
        router.add_router(router)


def test_add_router_wrong_type(router):
    with pytest.raises(ValueError):
        router.add_router(OnPoll())


def test_add_router_registered(router):
    nested = OnMessage()
    router.add_router(nested)
    router2 = OnMessage()
    with pytest.raises(ValueError):
        router2.add_router(nested)


def test_add_router_registered_same_router(router):
    nested = OnMessage()
    router.add_router(nested)
    with pytest.warns(BotWarning):
        router.add_router(nested)


def test_add_router_dispatcher(router, token):
    dispatcher = Dispatcher(token)
    with pytest.raises(RuntimeError):
        router.add_router(dispatcher)


def test_add_router_duplicate_same_obj():
    router = OnMessage()
    nested = OnMessage()
    router.add_router(nested)
    with pytest.warns(BotWarning):
        router.add_router(nested)
    assert len(router._routers) == 1
    assert router._routers[0] is nested


def test_add_router_duplicate_equal_obj():
    router = OnMessage()
    nested1 = OnMessage(name="router")
    nested2 = OnMessage(name="router")
    router.add_router(nested1)
    with pytest.warns(BotWarning):
        router.add_router(nested2)
    assert len(router._routers) == 1
    assert router._routers[0] is nested1
