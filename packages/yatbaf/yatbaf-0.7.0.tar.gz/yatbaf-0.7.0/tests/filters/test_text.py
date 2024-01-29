import re

import pytest

from yatbaf.filters import Text


def test_no_params():
    with pytest.raises(ValueError):
        Text()


def test_is_text(message):
    message.text = None
    assert not Text(startswith="foo").check(message)


@pytest.mark.parametrize("f,ic", (("FOO", False), ("foo", True)))
def test_startswith(message, f, ic):
    message.text = "FOO bar"
    assert Text(startswith=f, ignore_case=ic).check(message)


@pytest.mark.parametrize("f,ic", (("BAR", False), ("bar", True)))
def test_endswith(message, f, ic):
    message.text = "foo BAR"
    assert Text(endswith=f, ignore_case=ic).check(message)


def test_start_end(message):
    message.text = "foo baz bar"
    assert Text(startswith="foo", endswith="bar").check(message)


def test_start_end_any(message):
    message.text = "foo bar baz"
    assert (Text(startswith="foo", endswith="bar", any_=True).check(message))


@pytest.mark.parametrize("m,ic", (("Foo Bar", False), ("foo bar", True)))
def test_match(message, m, ic):
    message.text = "Foo Bar"
    assert Text(match=m, ignore_case=ic).check(message)


def test_match_false(message):
    message.text = "foo bar"
    assert not Text(match="foo b").check(message)


@pytest.mark.parametrize("c", ("bar", ["oof", "foo"]))
def test_contains(message, c):
    message.text = "foo bar baz"
    assert Text(contains=c).check(message)


def test_contains_false(message):
    message.text = "foo bar baz"
    assert not Text(contains="foobar").check(message)


@pytest.mark.parametrize("t", ("foobarbaz", "foo bar baz"))
def test_start_end_contains(message, t):
    message.text = t
    assert Text(
        startswith="fo",
        endswith="az",
        contains="bar",
    ).check(message)


@pytest.mark.parametrize("exp", (".+baz.*$", re.compile("^f.+az$")))
def test_regexp(message, exp):
    message.text = "foo bar baz"
    assert Text(regexp=exp).check(message)
