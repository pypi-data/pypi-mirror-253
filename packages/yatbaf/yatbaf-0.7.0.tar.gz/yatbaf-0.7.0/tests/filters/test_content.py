import pytest

from yatbaf.enums import ContentType
from yatbaf.filters import Content


def test_empty():
    with pytest.raises(ValueError):
        Content()


def test_wrong_type():
    with pytest.raises(ValueError):
        Content("typo")


@pytest.mark.parametrize("content", ["text", ContentType.TEXT])
def test_true(message, content):
    message.text = "123"
    assert Content(content).check(message)


@pytest.mark.parametrize("content", ["document", ContentType.DOCUMENT])
def test_filter_content_false(message, content):
    message.text = "123"
    message.document = None
    assert not Content(content).check(message)
