from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton    

def get_game_list_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops", callback_data="game_cod_bo"),
        ],
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops 2", callback_data="game_cod_bo2"),
        ],
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops 3", callback_data="game_cod_bo3"),
        ], 
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops 4", callback_data="game_cod_bo4"),
        ],
        [   
            InlineKeyboardButton(text="Call of Duty: Black Ops Cold War", callback_data="game_cod_bocw"),
        ],
        [
            InlineKeyboardButton(text="Call of Duty: Vanguard", callback_data="game_cod_vanguard"),
        ], 
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops 6", callback_data="game_cod_bo6"),
        ],
        [
            InlineKeyboardButton(text="Call of Duty: Black Ops 7", callback_data="game_cod_bo7"),
        ]
    ])
    return keyboard