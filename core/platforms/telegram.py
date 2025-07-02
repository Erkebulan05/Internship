from core.platforms.base import BasePlatform

class TelegramPlatform(BasePlatform):
    def extract_message(self, data: dict) -> str:
        return data.get("message", {}).get("text", "Ошибка: нет текста")

    def extract_token(self, data: dict) -> str:
        return data.get("token")
