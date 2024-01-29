from yatbaf.middleware import Middleware
from yatbaf.router import OnMessage


def test_init_middleware_handler():
    func = object()
    router = OnMessage(middleware=[func])
    assert Middleware(func, is_handler=True) in router._middleware


def test_init_middleware_router():
    func = object()
    router = OnMessage(middleware=[Middleware(func)])
    assert Middleware(func) in router._middleware


def test_init_middleware_handler_local():
    func = object()
    router = OnMessage(
        middleware=[
            Middleware(
                func,
                is_handler=True,
                is_local=True,
            ),
        ]
    )
    middleware = Middleware(
        func,
        is_handler=True,
        is_local=True,
    )
    assert middleware in router._middleware
    router._on_registration()
    assert middleware not in router._middleware


def test_add_middleware(router):
    func = object()
    router.add_middleware(func)
    assert Middleware(func, is_handler=True) in router._middleware


def test_middleware_handler_decorator(router):

    @router.middleware
    def func(_):  # noqa: U101
        pass

    assert len(router._middleware) == 1
    assert Middleware(func, is_handler=True) in router._middleware


def test_middleware_router_decorator(router):

    @router.middleware(is_handler=False)
    def func(_):  # noqa: U101
        pass

    assert len(router._middleware) == 1
    assert Middleware(func) in router._middleware


def test_middleware_decorator_duplicate(router):

    @router.middleware
    @router.middleware
    def func(_):  # noqa: U101
        pass

    assert len(router._middleware) == 1
    assert Middleware(func, is_handler=True) in router._middleware
