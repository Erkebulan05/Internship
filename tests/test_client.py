from config.clients import get_client_by_token

def test_get_existing_client():
    client = get_client_by_token("telegram", "123:ABC")
    assert client is not None
    assert client["business"] == "restaurant"

def test_get_invalid_token():
    client = get_client_by_token("telegram", "wrong-token")
    assert client is None
