import pytest

from yatbaf.enums import UpdateType
from yatbaf.filters import Command
from yatbaf.handler import Handler
from yatbaf.router import OnMessage


@pytest.fixture
def filter():
    return Command("foo")


@pytest.fixture
def handler(handler_func):
    return Handler(handler_func, UpdateType.MESSAGE)


@pytest.fixture
def router():
    return OnMessage()
