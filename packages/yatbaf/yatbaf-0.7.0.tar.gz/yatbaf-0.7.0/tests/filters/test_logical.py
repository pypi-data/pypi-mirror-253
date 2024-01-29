from yatbaf.filters import And
from yatbaf.filters import Channel
from yatbaf.filters import Command
from yatbaf.filters import Content
from yatbaf.filters import Not
from yatbaf.filters import Or
from yatbaf.filters import User


class FalseFilter:
    priority = 100

    def check(self, _):
        return False


class TrueFilter:
    priority = 100

    def check(self, _):
        return True


def test_not_true(message):
    assert Not(FalseFilter()).check(message)


def test_not_false(message):
    assert not Not(TrueFilter()).check(message)


def test_or_true(message):
    assert Or(FalseFilter(), TrueFilter()).check(message)


def test_or_false(message):
    assert not Or(FalseFilter(), FalseFilter()).check(message)


def test_and_true(message):
    assert And(TrueFilter(), TrueFilter()).check(message)


def test_and_false(message):
    assert not And(TrueFilter(), FalseFilter()).check(message)


def test_priority():
    user = User(123)
    channel = Channel()
    command = Command("start")
    content = Content("text")

    assert Not(channel).priority == channel.priority
    assert And(command, user).priority == user.priority
    assert Or(channel, content).priority == channel.priority
