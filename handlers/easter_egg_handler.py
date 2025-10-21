from aiogram import Router, F, Bot
from aiogram.types import (
    CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton,
    FSInputFile
)
import os
import json
from utils.database import get_user_language
from utils.localization import translate

router = Router()

# --- Храним активные сообщения каждого пользователя ---
active_messages: dict[int, list[int]] = {}

# --- Храним историю шагов (для кнопки "Назад") ---
user_steps: dict[int, list[str]] = {}


async def clear_user_messages(bot: Bot, user_id: int):
    """
    Удаляет все активные сообщения пользователя.
    """
    if user_id in active_messages:
        for msg_id in active_messages[user_id]:
            try:
                await bot.delete_message(user_id, msg_id)
                print(f"🧹 [DEBUG] Deleted message {msg_id}")
            except Exception as e:
                print(f"⚠️ [DEBUG] Failed to delete message {msg_id}: {e}")
        active_messages[user_id].clear()


async def send_user_message(bot: Bot, user_id: int, text: str = None,
                            photo: str = None, gif: str = None,
                            reply_markup=None):
    """
    Отправляет сообщение и сохраняет его ID как активное.
    """
    msg = None
    try:
        if photo:
            msg = await bot.send_photo(user_id, FSInputFile(photo), caption=text, reply_markup=reply_markup)
        elif gif:
            msg = await bot.send_animation(user_id, FSInputFile(gif), caption=text, reply_markup=reply_markup)
        else:
            msg = await bot.send_message(user_id, text, reply_markup=reply_markup)

        if user_id not in active_messages:
            active_messages[user_id] = []
        active_messages[user_id].append(msg.message_id)
    except Exception as e:
        print(f"❌ [DEBUG] Failed to send message: {e}")
    return msg


def load_map(game: str, map_name: str, user_id: int) -> dict | None:
    language = get_user_language(user_id)
    path = os.path.join("map_ee_structures", game, f"{map_name}_{language}.json")
    print(f"📘 [DEBUG] Loading map file: {path}")

    if not os.path.exists(path):
        print("❌ [DEBUG] Map file not found!")
        return None

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"✅ [DEBUG] Map file loaded successfully, steps: {len(data.get('steps', {}))}")
    return data


@router.callback_query(F.data.startswith("map:"))
async def map_step_handler(callback_query: CallbackQuery, bot: Bot):
    print("🔄 [DEBUG] map_step_handler triggered!")
    try:
        parts = callback_query.data.split(":")
        if len(parts) == 4:
            _, game, map_name, step_key = parts
            back = False
        elif len(parts) == 5 and parts[-1] == "back":
            _, game, map_name, step_key, _ = parts
            back = True
        else:
            raise ValueError("Invalid callback data")
    except Exception as e:
        print(f"❌ [DEBUG] Failed to parse callback data: {callback_query.data} | Error: {e}")
        return

    user_id = callback_query.from_user.id
    language = get_user_language(user_id)
    map_data = load_map(game, map_name, user_id)

    if not map_data:
        await send_user_message(bot, user_id, text=translate(language, "map_not_found"))
        return

    steps = map_data.get("steps", {})
    step = steps.get(step_key)
    if not step:
        await send_user_message(bot, user_id, text=translate(language, "next_step_not_found"))
        return

    # === История шагов ===
    if user_id not in user_steps:
        user_steps[user_id] = []

    if back:
        if user_steps[user_id]:
            user_steps[user_id].pop()  # удаляем текущий шаг из истории
    else:
        if not user_steps[user_id] or user_steps[user_id][-1] != step_key:
            user_steps[user_id].append(step_key)

    prev_step = user_steps[user_id][-2] if len(user_steps[user_id]) > 1 else None

    # === Удаляем старые сообщения (старый блок) ===
    await clear_user_messages(bot, user_id)

    # === Показываем новый шаг ===
    step_type = step.get("type")

    if step_type == "text":
        await send_user_message(bot, user_id, text=step["content"])

    elif step_type == "photo":
        await send_user_message(bot, user_id, text=step["content"], photo=step["image"])

    elif step_type == "gif":
        await send_user_message(bot, user_id, text=step["content"], gif=step["gif"])

    elif step_type == "multi_photo":
        for item in step["content"]:
            if "image" in item:
                await send_user_message(bot, user_id, text=item.get("text", ""), photo=item["image"])
            else:
                await send_user_message(bot, user_id, text=item.get("text", ""))

    # === Кнопки ===
    buttons = []

    # Кнопки выбора
    if "choices" in step:
        for text, target in step["choices"].items():
            buttons.append([InlineKeyboardButton(text=text, callback_data=f"map:{game}:{map_name}:{target}")])

    # Кнопка "Дальше"
    elif step.get("next_step"):
        buttons.append([InlineKeyboardButton(
            text="➡ Дальше",
            callback_data=f"map:{game}:{map_name}:{step['next_step']}"
        )])

    # Кнопка "Назад"
    if prev_step:
        buttons.append([InlineKeyboardButton(
            text="⬅ Назад",
            callback_data=f"map:{game}:{map_name}:{prev_step}:back"
        )])

    if buttons:
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await send_user_message(bot, user_id, text=translate(language, "choose_next_step"), reply_markup=keyboard)

    print(f"✅ [DEBUG] Step '{step_key}' displayed successfully")
