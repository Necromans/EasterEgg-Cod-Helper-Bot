from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.language_kb import get_language_keyboard
from utils.database import get_user_language
from utils.localization import translate

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(translate(get_user_language(message.from_user.id), "start_message"), reply_markup=get_language_keyboard())