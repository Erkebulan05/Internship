import openai
from datetime import datetime, timedelta
import re
import os
import json

LOG_PATH = "logs/bookings.log"
PENDING_PATH = "logs/pending.json"

def log_booking(guests: int, time: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{booking_time}] Бронирование: {guests} гостей в {time}\n")

def is_time_available(time: str) -> bool:
    if not os.path.exists(LOG_PATH):
        return True
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        return not any(f"в {time}" in line for line in f)

def find_next_available_time(start_time: str, interval_minutes=30, max_attempts=5):
    try:
        base = datetime.strptime(start_time, "%H:%M")
    except ValueError:
        return None
    for i in range(1, max_attempts + 1):
        new_time = base + timedelta(minutes=i * interval_minutes)
        formatted = new_time.strftime("%H:%M")
        if is_time_available(formatted):
            return formatted
    return None

def save_pending(user_id: str, guests: int, time: str):
    pending = {}
    if os.path.exists(PENDING_PATH):
        with open(PENDING_PATH, "r", encoding="utf-8") as f:
            pending = json.load(f)
    pending[user_id] = {"guests": guests, "time": time}
    with open(PENDING_PATH, "w", encoding="utf-8") as f:
        json.dump(pending, f)

def load_pending(user_id: str):
    if not os.path.exists(PENDING_PATH):
        return None
    with open(PENDING_PATH, "r", encoding="utf-8") as f:
        pending = json.load(f)
    return pending.get(user_id)

def clear_pending(user_id: str):
    if not os.path.exists(PENDING_PATH):
        return
    with open(PENDING_PATH, "r", encoding="utf-8") as f:
        pending = json.load(f)
    if user_id in pending:
        del pending[user_id]
        with open(PENDING_PATH, "w", encoding="utf-8") as f:
            json.dump(pending, f)

def is_confirmation(text: str) -> bool:
    return text.lower().strip() in ["да", "ок", "подходит", "согласен", "хорошо"]

async def handle_restaurant_message(text: str, user_id: str = "default") -> str:

    if is_confirmation(text):
        pending = load_pending(user_id)
        if pending:
            guests = pending["guests"]
            time = pending["time"]
            log_booking(guests, time)
            clear_pending(user_id)
            return f"✅ Отлично! Забронировали столик на {guests} гостей в {time}."
        else:
            return "❌ У нас нет ожидающей брони. Пожалуйста, уточните время и количество гостей."


    system_prompt = (
        "Ты помощник ресторана. Задача — понять, на сколько гостей и на какое время клиент хочет забронировать столик. "
        "Верни только JSON в формате: {\"guests\": 2, \"time\": \"18:00\"}. "
        "Если информация неполная — спроси, что не хватает."
    )

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )

        content = response.choices[0].message.content.strip()
        match = re.search(r'\"guests\"\s*:\s*(\d+)[,}]\s*\"time\"\s*:\s*\"([\d:apm\s]+)\"', content)

        if not match:
            return "Не удалось понять время или количество гостей. Пожалуйста, уточните."

        guests = int(match.group(1))
        time = match.group(2).strip()

        if is_time_available(time):
            log_booking(guests, time)
            return f"✅ Готово! Забронировали столик на {guests} гостей в {time}."
        else:
            alternative = find_next_available_time(time)
            if alternative:
                save_pending(user_id, guests, alternative)
                return (
                    f"❌ Время {time} уже занято.\n"
                    f"✅ Могу предложить в {alternative}. Подходит?"
                )
            else:
                return (
                    f"❌ Время {time} занято и нет свободных слотов рядом.\n"
                    f"Попробуйте указать другое время."
                )

    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {str(e)}"
