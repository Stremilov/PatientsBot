import logging

from aiogram.types import BotCommand

from app.loader import dp, bot
from app.models import Base
from app.database import engine
from app import handlers

import asyncio


logging.basicConfig(level=logging.INFO)


async def main() -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Начать"),
            BotCommand(command="/add_patient", description="Добавить пациента"),
            BotCommand(
                command="/get_today_patients",
                description="Получить информацию о сегодняшних пациентах",
            ),
            BotCommand(
                command="/get_patients_count_by_day",
                description="Получить пациентов за каждый день недели",
            ),
        ]
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    asyncio.run(main())
