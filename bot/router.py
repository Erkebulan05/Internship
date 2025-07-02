from fastapi import APIRouter
from core.ai_manager import handle_message
from services.platform_router import detect_client, get_platform_handler



async def router_messages(data: dict, platform: str, bot_token: str = None):
    platform_handler = get_platform_handler(platform) # detected the platform

    if not platform_handler:
        return {"reply": "The platform is not supported"}

    user_message = platform_handler.extract_message(data)

    bot_token = platform_handler.extract_token(data)


    if not bot_token:
        return {"reply": "The bot token is not valid"}


    client = detect_client(data, platform, bot_token=bot_token)

    if not client:
        return {"reply": "Client is not found"}

    business = client["business"]
    reply = await handle_message(user_message, platform, business)

    return {"reply": reply, "token": client["token"]}







