from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token='5764376730:AAHIpk4zZUABoadvShhvdgKfNKa7VSOAb_E', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

