import pytest

from yatbaf.filters import Not
from yatbaf.filters import User

USER_ID = 1212
USER_USERNAME = "test_user"


@pytest.fixture(autouse=True)
def _set_user_attrs(user):
    user.id = USER_ID
    user.username = USER_USERNAME


@pytest.mark.parametrize("username", ("@test_user", "test_user", USER_ID))
def test_true(message, username):
    assert User(username).check(message)


@pytest.mark.parametrize("username", ("@testuser", "test_user1", 23345678))
def test_false(message, username):
    assert not User(username).check(message)


@pytest.mark.parametrize("username", ("@test_user", "test_user", USER_ID))
def test_invert(message, username):
    assert not Not(User(username)).check(message)
