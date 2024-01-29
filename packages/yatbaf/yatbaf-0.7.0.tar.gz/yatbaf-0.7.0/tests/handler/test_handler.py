import pytest

from yatbaf.enums import UpdateType
from yatbaf.filters import Chat
from yatbaf.handler import Handler


def test_new_hander(handler_func):
    handler = Handler(handler_func, update_type=UpdateType.MESSAGE)
    assert not handler._filters
    assert handler._is_fallback
    assert not handler._middleware
    assert handler._update_type is UpdateType.MESSAGE
    assert str(handler) == "<Handler[type=message]>"
    assert handler._match_fn is all


@pytest.mark.parametrize(
    "objs",
    [
        (
            Handler(f := object(), update_type=UpdateType.MESSAGE),
            Handler(f, update_type=UpdateType.MESSAGE),
        ),
        (
            Handler(f := object(), update_type=UpdateType.MESSAGE),
            Handler(f, update_type=UpdateType.MESSAGE, filters=[Chat()]),
        ),
        (
            Handler(
                f := object(),
                update_type=UpdateType.MESSAGE,
                middleware=[m := object()]
            ),
            Handler(f, update_type=UpdateType.MESSAGE, middleware=[m]),
        ),
    ]
)
def test_eq(objs):
    handler1, handler2 = objs
    assert handler1 == handler2


@pytest.mark.parametrize(
    "h1", [Handler(f := object(), update_type=UpdateType.MESSAGE)]
)
@pytest.mark.parametrize(
    "h2",
    [
        Handler(f, update_type=UpdateType.EDITED_MESSAGE),
        Handler(f, update_type=UpdateType.MESSAGE, middleware=[object()]),
        Handler(object(), update_type=UpdateType.MESSAGE),
    ]
)
def test_not_eq(h1, h2):
    assert h1 != h2
