import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import start, language, game_selection, easter_egg_handler
from menu_items.main_menu import set_main_menu
from utils.database import init_db
from commands import choose_game

# t.me/EasterEggCodBot

async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(language.router)
    dp.include_router(choose_game.router)
    dp.include_router(game_selection.router)
    dp.include_router(easter_egg_handler.router)
    # Setup bot main menu
    await set_main_menu(bot)

    logging.info("Bot is starting and listening...")

    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":  
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    asyncio.run(main())