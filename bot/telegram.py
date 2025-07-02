import requests

# def send_telegram_message(token: str, chat_id: int, text: str):
#     print(f"📤 Отправка Telegram: {text}")
#     """
#     Отправляет сообщение в Telegram от имени бота
#     """
#     url = f"https://api.telegram.org/bot{token}/sendMessage"
#     payload = {
#         "chat_id": chat_id,
#         "text": text,
#         "parse_mode": "HTML"  # можно убрать или заменить на Markdown
#     }
#     try:
#         response = requests.post(url, json=payload)
#         if not response.ok:
#             print("❌ Ошибка отправки сообщения в Telegram:", response.text)
#     except Exception as e:
#         print("❌ Исключение при отправке в Telegram:", str(e))

def send_telegram_message(token: str, chat_id: int, text: str):
    print(f"📨 Отправка в Telegram -> chat_id: {chat_id}, text: {text}")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    print("🔁 Ответ от Telegram:", response.status_code, response.text)
