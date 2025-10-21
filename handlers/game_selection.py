from aiogram import Router, F
from aiogram.types import CallbackQuery, BotCommand, BotCommandScopeChat
from utils.database import set_user_language, get_user_language
from utils.localization import translate
from keyboards.choos_maps_kb import get_maps_list_keyboard

router = Router()

@router.callback_query(F.data.startswith("game_cod"))
async def select_game_handler(callback: CallbackQuery) -> None: 
    game = callback.data.split("_")[2]

    await callback.message.edit_text(translate(get_user_language(callback.from_user.id), 'game_selected').format(game=game), reply_markup=get_maps_list_keyboard(game))
    await callback.answer()