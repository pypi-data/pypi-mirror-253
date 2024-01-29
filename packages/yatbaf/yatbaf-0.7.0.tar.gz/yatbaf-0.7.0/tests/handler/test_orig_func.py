import pytest

from yatbaf.enums import UpdateType
from yatbaf.handler import Handler


@pytest.mark.asyncio
async def test_orig_func(handler_func, message):
    handler = Handler(
        handler_func,
        update_type=UpdateType.MESSAGE,
    )
    await handler.orig(message)
    handler_func.assert_awaited_once_with(message)
