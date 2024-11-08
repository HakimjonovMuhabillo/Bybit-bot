from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TELEGRAM_TOKEN = '6901257804:AAEAZ2dP399pa75NLqHexhr7rhIhO0wYBuc'
TELEGRAM_CHAT_ID = '1380803567'

class TelegramService:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()

    async def send_message(self, message: str, chat_id: str|int):
        await self.bot.send_message(chat_id=chat_id, text=message)