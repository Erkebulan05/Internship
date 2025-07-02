from pydantic import BaseModel, Field

class BotCreateRequest(BaseModel):
    id: str = Field(..., description="Уникальный ID бота")
    platform: str = Field(..., description="Название платформы: telegram, whatsapp, instagram")
    token: str = Field(..., description="Токен бота")
    business: str = Field(..., description="Тип бизнеса: restaurant, barbershop, dentist и т.д.")

