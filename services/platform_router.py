# from config.clients import get_client_by_token
#
# from core.platforms.telegram import TelegramPlatform
# from core.platforms.whatsapp import WhatsAppPlatform
# from core.platforms.instagram import InstagramPlatform
#
# PLATFORM_CLASSES = {
#     "telegram": TelegramPlatform(),
#     "whatsapp": WhatsAppPlatform(),
#     "instagram": InstagramPlatform()
# }
#
#
# def detect_client(data: dict, platform: str):
#     handler = get_platform_handler(platform)
#     if not handler:
#         return None
#     token = handler.extract_token(data)
#     return get_client_by_token(platform, token)
#
# def get_platform_handler(platform: str):
#     return PLATFORM_CLASSES.get(platform)
#
# # def detect_client(data: dict, platform: str):
# #     token = extract_token(data, platform)
# #     return get_client_by_token(platform, token)
# #
# # def extract_token(data: dict, platform: str) -> str:
# #     try:
# #         if platform == "telegram":
# #             return data.get("token")
# #         elif platform == "whatsapp":
# #             return data["metadata"]["token"]
# #         elif platform == "instagram":
# #             return data.get("token")
# #     except (KeyError, TypeError):
# #         return None
# #
# #     return None
#
#
#
#

from config.clients import get_client_by_token
from core.platforms.telegram import TelegramPlatform
from core.platforms.whatsapp import WhatsAppPlatform
from core.platforms.instagram import InstagramPlatform

PLATFORM_CLASSES = {
    "telegram": TelegramPlatform(),
    "whatsapp": WhatsAppPlatform(),
    "instagram": InstagramPlatform()
}

def get_platform_handler(platform: str):
    return PLATFORM_CLASSES.get(platform)

def detect_client(data: dict, platform: str, bot_token: str = None):

    if bot_token :
        return get_client_by_token(platform, bot_token)


    handler = get_platform_handler(platform)
    if not handler:
        return None
    token = handler.extract_token(data)
    return get_client_by_token(platform, token)
