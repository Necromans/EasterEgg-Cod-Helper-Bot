from aiogram import Router, F
from aiogram.types import CallbackQuery, BotCommand, BotCommandScopeChat
from utils.database import set_user_language, get_user_language
from utils.localization import translate    

router = Router()
@router.callback_query(F.data.startswith("lang_"))
async def change_language_handler(callback: CallbackQuery) -> None:
    lang = callback.data.split("_")[1]
    set_user_language(callback.from_user.id, lang)

    commands = [
        BotCommand(command="/start", description=translate(get_user_language(callback.from_user.id), "start_command_description")),
        BotCommand(command="/language", description=translate(get_user_language(callback.from_user.id), "language_command_description")),
        BotCommand(command="/help", description=translate(get_user_language(callback.from_user.id), "help_command_description")),
        BotCommand(command="/choose_game", description=translate(get_user_language(callback.from_user.id), "choose_game_command_description"))
    ]

    await callback.bot.set_my_commands(commands, scope=BotCommandScopeChat(chat_id=callback.from_user.id))
    await callback.message.edit_text(translate(get_user_language(callback.from_user.id), 'language_changed'))
    await callback.answer()

    