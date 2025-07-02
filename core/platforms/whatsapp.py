from core.platforms.base import BasePlatform

class WhatsAppPlatform(BasePlatform):
    def extract_message(self, data: dict) -> str:
        try:
            return data["messages"][0]["text"]["body"]
        except (KeyError, IndexError, TypeError):
            return "Ошибка: нет текста"

    def extract_token(self, data: dict) -> str:
        return data.get("metadata", {}).get("token")

