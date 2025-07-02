from core.platforms.telegram import TelegramPlatform

def test_telegram_extract_message():
    platform = TelegramPlatform()
    data = {"message": {"text": "Привет!"}}
    assert platform.extract_message(data) == "Привет!"

def test_telegram_extract_token():
    platform = TelegramPlatform()
    data = {"token": "123:ABC"}
    assert platform.extract_token(data) == "123:ABC"
