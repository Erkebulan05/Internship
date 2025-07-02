
import pytest
from core.business_logic.restaurant import handle_restaurant_message

@pytest.mark.asyncio
async def test_restaurant_response():
    result = await handle_restaurant_message("Привет")
    assert isinstance(result, str)
    assert len(result) > 0
