import pytest

from yatbaf.filters import Command


def test_empty():
    with pytest.raises(ValueError):
        Command()


def test_true(message):
    message.text = "/ping"
    assert Command("ping").check(message)


def test_false(message):
    message.text = "/pong"
    assert not Command("ping").check(message)


def test_mix_true(message):
    message.text = "/pong"
    assert Command("ping", "pong").check(message)


def test_text_is_none(message):
    message.text = None
    assert not Command("ping").check(message)


@pytest.mark.parametrize("filter", ["start", "/start", "START", "Start"])
def test_case(message, filter):
    message.text = "/start"
    assert Command(filter).check(message)
