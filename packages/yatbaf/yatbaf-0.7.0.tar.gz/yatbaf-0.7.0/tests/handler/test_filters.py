from yatbaf.enums import UpdateType
from yatbaf.filters import Chat
from yatbaf.filters import Command
from yatbaf.handler import Handler


def test_filter(handler_func):
    cmd_filter = Command("cmd")
    chat_filter = Chat()
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        filters=[cmd_filter, chat_filter],
    )
    assert len(handler._filters) == 2
    assert handler._filters[0] is chat_filter
    assert handler._filters[1] is cmd_filter


def test_filter_sort_false(handler_func):
    cmd_filter = Command("cmd")
    chat_filter = Chat()
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
        filters=[cmd_filter, chat_filter],
        sort_filters=False,
    )
    assert len(handler._filters) == 2
    assert handler._filters[0] is cmd_filter
    assert handler._filters[1] is chat_filter
