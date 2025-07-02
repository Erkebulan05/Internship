import pytest
from bot.router import router_messages

@pytest.mark.asyncio
async def test_router_with_invalid_client():
    data = {
        "message": {"text": "Привет"},
        "token": "invalid-token"
    }
    result = await router_messages(data, platform="telegram")
    assert "Client is not found" in result["reply"]

