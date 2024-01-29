import unittest.mock as mock

import pytest

from yatbaf.dispatcher import Dispatcher
from yatbaf.exceptions import SkipRouterException
from yatbaf.models import UpdateInfo
from yatbaf.router import OnMessage
from yatbaf.router import OnPoll


@pytest.mark.asyncio
async def test_resolve_no_routers(token, update_info):
    dispatcher = Dispatcher(token)
    assert not await dispatcher._resolve(update_info)


@pytest.mark.asyncio
async def test_resolve(token, handler_func, update_info):
    dispatcher = Dispatcher(
        token,
        routers=[OnMessage(handlers=[handler_func])],
    )
    await dispatcher._resolve(update_info)
    handler_func.assert_awaited_once_with(update_info.content)


@pytest.mark.asyncio
async def test_resolve_none(token, handler_func, update_info):
    dispatcher = Dispatcher(token, routers=[OnPoll(handlers=[handler_func])])
    await dispatcher._resolve(update_info)
    handler_func.assert_not_awaited()


@pytest.mark.asyncio
async def test_resolve_guard_false(token, handler_func, update_info):

    def _guard(_):
        raise SkipRouterException

    dispatcher = Dispatcher(
        token,
        guards=[_guard],
        routers=[OnMessage(handlers=[handler_func])],
    )
    await dispatcher._resolve(update_info)
    handler_func.assert_not_awaited()


@pytest.mark.asyncio
async def test_resolve_guard_true(token, handler_func, update_info):
    dispatcher = Dispatcher(
        token,
        guards=[lambda _: True],
        routers=[OnMessage(handlers=[handler_func])],
    )
    await dispatcher._resolve(update_info)
    handler_func.assert_awaited_once_with(update_info.content)


@pytest.mark.asyncio
async def test_process_update(monkeypatch, token, update):
    monkeypatch.setattr(Dispatcher, "_bind_self", lambda _, v: v)  # noqa: U101
    monkeypatch.setattr(
        Dispatcher, "_resolve", resolve := mock.AsyncMock(return_value=None)
    )
    dispatcher = Dispatcher(token)
    await dispatcher.process_update(update)
    resolve.assert_awaited_once_with(
        UpdateInfo(
            id=update.update_id,
            content=update.message,
            name="message",
        )
    )
