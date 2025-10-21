from aiogram import Bot, Router
from aiogram.types import BotCommand

async def set_main_menu(bot: Bot) -> None:
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/language", description="Change language"),
        BotCommand(command="/help", description="Get help information"),
        BotCommand(command="/choose_game", description="Choose a game")
    ]
    await bot.set_my_commands(commands)