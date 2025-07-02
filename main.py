from fastapi import FastAPI, Request
from bot.router import router_messages
from admin.admin_router import router as admin_router
from config.clients import get_client_by_token
from bot.telegram import send_telegram_message
from urllib.parse import unquote



app = FastAPI()
app.include_router(admin_router)

@app.post("/wenbook/telegram")
async def telegram_wenbook(request: Request):
    data = await request.json()
    return await router_messages(data, platform="telegram" )

@app.post("/wenbook/whatsapp")
async def whatsapp_wenbook(request: Request):
    data = await request.json()
    return await router_messages(data , platform="whatsapp")


@app.post("/wenbook/instagram")
async def instagram_wenbook(request: Request):
    data = await request.json()
    return await router_messages(data , platform="instagram")
