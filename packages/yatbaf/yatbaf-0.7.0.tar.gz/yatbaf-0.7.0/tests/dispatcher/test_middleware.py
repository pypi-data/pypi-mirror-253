import unittest.mock as mock

from yatbaf.dispatcher import Dispatcher
from yatbaf.middleware import Middleware


def test_middleware(token):
    fn = mock.Mock(return_value=(mdwl := mock.Mock))
    dispatcher = Dispatcher(token, middleware=[Middleware(fn)])
    assert not dispatcher._middleware
    assert dispatcher._middleware_stack is mdwl


def test_middleware_order(token):
    fn1 = mock.Mock(return_value=(mdwl1 := mock.Mock))
    fn2 = mock.Mock()
    dispatcher = Dispatcher(
        token, middleware=[
            Middleware(fn1),
            Middleware(fn2),
        ]
    )
    assert not dispatcher._middleware
    assert dispatcher._middleware_stack is mdwl1
