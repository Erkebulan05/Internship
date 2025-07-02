from fastapi import APIRouter, HTTPException
from schemas.bot import BotCreateRequest  
import json
import os

CLIENTS_PATH = "config/clients.json"

router = APIRouter()

@router.post("/admin/add_bot")
def add_bot(bot: BotCreateRequest):
    if not os.path.exists(CLIENTS_PATH):
        return HTTPException(status_code=500, detail="clients.json not found")

    with open(CLIENTS_PATH, "r", encoding="utf-8") as f:
        clients = json.load(f)

    for existing in clients:
        if existing["id"] == bot.id:
            raise HTTPException(status_code=400, detail="ID уже существует")
        if existing["token"] == bot.token:
            raise HTTPException(status_code=400, detail="Такой токен уже существует")

    clients.append(bot.dict())

    with open(CLIENTS_PATH, "w", encoding="utf-8") as f:
        json.dump(clients, f, indent=2, ensure_ascii=False)

    return {"message": "Бот успешно добавлен ✅", "bot": bot}
