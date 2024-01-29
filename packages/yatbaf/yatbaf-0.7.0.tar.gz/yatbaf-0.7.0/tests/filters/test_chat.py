import pytest

from yatbaf.enums import ChatType
from yatbaf.filters import Channel
from yatbaf.filters import Group

CHAT_ID = 123232


@pytest.fixture(autouse=True)
def _set_chat_id(chat):
    chat.id = CHAT_ID


@pytest.mark.parametrize("t", [ChatType.GROUP, ChatType.SUPERGROUP])
def test_filter_group(message, t):
    message.chat.type = t
    assert Group().check(message)


@pytest.mark.parametrize("t", [ChatType.GROUP, ChatType.SUPERGROUP])
def test_filter_group_ids(message, t):
    message.chat.type = t
    assert Group(CHAT_ID).check(message)
    assert not Group(123).check(message)


def test_filter_channel(message):
    message.chat.type = ChatType.CHANNEL
    assert Channel().check(message)


def test_filter_channel_ids(message):
    message.chat.type = ChatType.CHANNEL
    assert Channel(CHAT_ID).check(message)
    assert not Channel(123).check(message)
