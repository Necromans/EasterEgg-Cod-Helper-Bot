from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.localization import translate
from keyboards.choose_game_kb import get_game_list_keyboard
from utils.database import get_user_language

router = Router()

@router.message(Command("choose_game"))
async def cmd_choose_game(message: Message) -> None:
    await message.answer(translate(get_user_language(message.from_user.id), "choose_game_message"), reply_markup=get_game_list_keyboard()) 