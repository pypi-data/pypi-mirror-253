from yatbaf.router import OnMessage


def _guard_func(_):  # noqa: U101
    return


def test_init_guard():
    router = OnMessage(guards=[_guard_func])
    assert _guard_func in router._guards


def test_add_guard():
    router = OnMessage()
    router.add_guard(_guard_func)
    assert len(router._guards) == 1
    assert _guard_func in router._guards


def test_add_guard_duplicate():
    router = OnMessage()
    func = object()

    router.add_guard(func)
    router.add_guard(func)
    assert len(router._guards) == 1
    assert func in router._guards


def test_guard_decorator(router):

    @router.guard
    def func(_):  # noqa: U101
        pass

    assert len(router._guards) == 1
    assert func in router._guards
