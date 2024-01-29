import pytest

from yatbaf.enums import UpdateType
from yatbaf.middleware import Middleware
from yatbaf.router import OnCallbackQuery
from yatbaf.router import OnChannelPost
from yatbaf.router import OnChatBoost
from yatbaf.router import OnChatJoinRequest
from yatbaf.router import OnChatMemeber
from yatbaf.router import OnChosenInlineResult
from yatbaf.router import OnEditedChannelPost
from yatbaf.router import OnEditedMessage
from yatbaf.router import OnInlineQuery
from yatbaf.router import OnMessage
from yatbaf.router import OnMessageReaction
from yatbaf.router import OnMessageReactionCount
from yatbaf.router import OnMyChatMember
from yatbaf.router import OnPoll
from yatbaf.router import OnPollAnswer
from yatbaf.router import OnPreCheckoutQuery
from yatbaf.router import OnRemovedChatBoost
from yatbaf.router import OnShippingQuery
from yatbaf.router import router_map


def test_router_map():
    for type_ in UpdateType:
        assert type_ in router_map


def test_update_type():
    assert OnCallbackQuery._update_type == UpdateType.CALLBACK_QUERY
    assert OnChannelPost._update_type == UpdateType.CHANNEL_POST
    assert OnChatJoinRequest._update_type == UpdateType.CHAT_JOIN_REQUEST
    assert OnChatMemeber._update_type == UpdateType.CHAT_MEMBER
    assert OnChosenInlineResult._update_type == UpdateType.CHOSEN_INLINE_RESULT
    assert OnEditedChannelPost._update_type == UpdateType.EDITED_CHANNEL_POST
    assert OnEditedMessage._update_type == UpdateType.EDITED_MESSAGE
    assert OnInlineQuery._update_type == UpdateType.INLINE_QUERY
    assert OnMessage._update_type == UpdateType.MESSAGE
    assert OnMyChatMember._update_type == UpdateType.MY_CHAT_MEMBER
    assert OnPoll._update_type == UpdateType.POLL
    assert OnPollAnswer._update_type == UpdateType.POLL_ANSWER
    assert OnPreCheckoutQuery._update_type == UpdateType.PRE_CHECKOUT_QUERY
    assert OnShippingQuery._update_type == UpdateType.SHIPPING_QUERY
    assert OnChatBoost._update_type == UpdateType.CHAT_BOOST
    assert OnRemovedChatBoost._update_type == UpdateType.REMOVED_CHAT_BOOST
    assert OnMessageReaction._update_type == UpdateType.MESSAGE_REACTION
    assert OnMessageReactionCount._update_type == UpdateType.MESSAGE_REACTION_COUNT  # noqa: E501


def test_new_router():
    router = OnMessage()
    assert not router._handlers
    assert not router._middleware
    assert not router._guards


@pytest.mark.parametrize(
    "objs",
    [
        (
            OnMessage(),
            OnMessage(),
        ),
        (
            OnMessage(guards=[g := object()]),
            OnMessage(guards=[g]),
        ),
        (
            OnMessage(handlers=[h := object()]),
            OnMessage(handlers=[h]),
        ),
        (
            OnMessage(guards=[g := object()], handlers=[h := object()]),
            OnMessage(guards=[g], handlers=[h]),
        ),
        (
            OnMessage(
                middleware=[m := object()],
                guards=[g := object()],
                handlers=[h := object()]
            ),
            OnMessage(
                middleware=[m],
                guards=[g],
                handlers=[h],
            ),
        ),
        (
            OnMessage(
                middleware=[Middleware(m := object())],
                guards=[g := object()],
                handlers=[h := object()]
            ),
            OnMessage(
                middleware=[Middleware(m)],
                guards=[g],
                handlers=[h],
            ),
        ),
    ]
)
def test_eq(objs):
    router1, router2 = objs
    assert router1 == router2


@pytest.mark.parametrize("r1", [OnMessage()])
@pytest.mark.parametrize(
    "r2",
    [
        OnMessage(handlers=[object]),
        OnMessage(middleware=[object()]),
        OnMessage(guards=[object()]),
        OnMessage(handlers=[object], middleware=[object()]),
        OnMessage(handlers=[object], middleware=[object()], guards=[object()]),
    ]
)
def test_not_eq(r1, r2):
    assert r1 != r2
