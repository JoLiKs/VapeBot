import asyncio
import logging
import time

from aiogram import executor
from data.config import OFFICERS
from handlers import dp
from handlers.users import start_bot
from utils.datbase import create_base, get_officers
from multiprocessing import Process
from utils.sql_commands import get_bans


async def on_startup(dp):
    create_base()
    for off in get_officers():
        OFFICERS.append(off)


def tg():
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)


if __name__ == '__main__':
    p = Process(target=tg)
    p.start()
    p.join()


