def test_ctx_empty(message):
    assert not message.ctx


def test_ctx(message):
    message.ctx["foo"] = "bar"
    assert "foo" in message.__usrctx__
