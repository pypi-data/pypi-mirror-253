import pytest

from yatbaf.dispatcher import Dispatcher


def test_dispatcher(token):
    dispatcher = Dispatcher(token)
    assert dispatcher._routers
    assert not dispatcher._middleware
    assert not dispatcher._guards


def test_update_type(token):
    with pytest.raises(RuntimeError):
        Dispatcher(token)._update_type
