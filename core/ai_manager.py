import importlib
import pkgutil
import os
import openai
import json
from datetime import datetime
from typing import Callable, Dict, Awaitable

from core.business_logic import restaurant  # для совместимости

openai.api_key = os.getenv("OPENAI_API_KEY")

BUSINESS_HANDLERS: Dict[str, Callable[[str, str], Awaitable[str]]] = {}

def register_business_handlers():
    package_path = os.path.join(os.path.dirname(__file__), "business_logic")
    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        module = importlib.import_module(f"core.business_logic.{module_name}")
        if hasattr(module, "handle_message"):
            BUSINESS_HANDLERS[module_name] = getattr(module, "handle_message")

register_business_handlers()

LOG_PATH = "logs/openai.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_openai_interaction(user_id: str, platform: str, business: str, prompt: str, response: str):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "platform": platform,
        "business": business,
        "prompt": prompt,
        "response": response
    }
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

async def handle_message(text: str, platform: str, business: str, user_id: str = "default") -> str:
    handler = BUSINESS_HANDLERS.get(business)
    if handler:
        response = await handler(text, user_id)
        log_openai_interaction(user_id, platform, business, text, response)
        return response
    return f"️ Бизнес-логика для '{business}' не найдена."
