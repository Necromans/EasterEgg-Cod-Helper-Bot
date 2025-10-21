from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_maps_list_keyboard(game: str) -> InlineKeyboardMarkup:
    if game == "bo":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Nacht der Untoten", callback_data="map_nacht_der_untoten"),
            ],
            [
                InlineKeyboardButton(text="Verrückt", callback_data="map_verruckt"),
            ],
            [
                InlineKeyboardButton(text="Shi No Numa", callback_data="map_shi_no_numa"),
            ],
            [
                InlineKeyboardButton(text="Der Riese", callback_data="map_der_riese"),
            ],
            [
                InlineKeyboardButton(text="Kino der Toten", callback_data="map_kino_der_toten"),
            ],
            [
                InlineKeyboardButton(text="Ascension", callback_data="map_ascension"),
            ],
            [
                InlineKeyboardButton(text="Shangri-La", callback_data="map_shangri_la"),
            ],
            [
                InlineKeyboardButton(text="Moon", callback_data="map_moon"),
            ]
        ])
    elif game == "bo2":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Tranzit", callback_data="map_tranzit"),
            ],
            [
                InlineKeyboardButton(text="Nuketown Zombies", callback_data="map_nuketown_zombies"),
            ],
            [
                InlineKeyboardButton(text="Die Rise", callback_data="map_die_rise"),
            ],
            [
                InlineKeyboardButton(text="Mob of the Dead", callback_data="map_mob_of_the_dead"),
            ],
            [
                InlineKeyboardButton(text="Buried", callback_data="map_buried"),
            ],
            [
                InlineKeyboardButton(text="Origins", callback_data="map_origins"),
            ]
        ])
    elif game == "bo3":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Shadows of Evil", callback_data="map:shadows_of_evil"),
            ],
            [
                InlineKeyboardButton(text="The Giant", callback_data="map:the_giant"),
            ],
            [
                InlineKeyboardButton(text="Der Eisendrache", callback_data="map:CodBo3:der_eisendrache:step1"),
            ],
            [
                InlineKeyboardButton(text="Zetsubou No Shima", callback_data="map:zetsubou_no_shima"),
            ],
            [
                InlineKeyboardButton(text="Gorod Krovi", callback_data="map:gorod_krovi"),
            ],
            [
                InlineKeyboardButton(text="Revelations", callback_data="map:revelations"),
            ]
        ])
    elif game == "bo4":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Voyage of Despair", callback_data="map_voyage_of_despair"),
            ],
            [
                InlineKeyboardButton(text="IX", callback_data="map_ix"),
            ],
            [
                InlineKeyboardButton(text="Blood of the Dead", callback_data="map_blood_of_the_dead"),
            ],
            [
                InlineKeyboardButton(text="Classified", callback_data="map_classified"),
            ],
            [
                InlineKeyboardButton(text="Dead of the Night", callback_data="map_dead_of_the_night"),
            ],
            [
                InlineKeyboardButton(text="Ancient Evil", callback_data="map_ancient_evil"),
            ]
        ])
    elif game == "bocw":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Firebase Z", callback_data="map_firebase_z"),
            ],
            [
                InlineKeyboardButton(text="Mauer der Toten", callback_data="map_mauer_der_toten"),
            ],
            [
                InlineKeyboardButton(text="Forsaken", callback_data="map_forsaken"),
            ]
        ])
    elif game == "vanguard":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Der Anfang", callback_data="map_der_anfang"),
            ],
            [
                InlineKeyboardButton(text="Die Maschine", callback_data="map_die_maschine"),
            ],
            [
                InlineKeyboardButton(text="Nacht der Untoten (Vanguard)", callback_data="map_nacht_der_untoten_vanguard"),
            ]
        ])
    elif game == "bo6":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Map 1", callback_data="map_bo6_map1"),
            ],
            [
                InlineKeyboardButton(text="Map 2", callback_data="map_bo6_map2"),
            ]
        ])
    elif game == "bo7":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Map A", callback_data="map_bo7_mapa"),
            ],
            [
                InlineKeyboardButton(text="Map B", callback_data="map_bo7_mapb"),
            ]
        ])
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Nacht der Untoten", callback_data="map_nacht_der_untoten"),
            ],
            [
                InlineKeyboardButton(text="Verrückt", callback_data="map_verruckt"),
            ],
            [
                InlineKeyboardButton(text="Shi No Numa", callback_data="map_shi_no_numa"),
            ],
            [
                InlineKeyboardButton(text="Der Riese", callback_data="map_der_riese"),
            ],
            [
                InlineKeyboardButton(text="Kino der Toten", callback_data="map_kino_der_toten"),
            ],
            [
                InlineKeyboardButton(text="Ascension", callback_data="map_ascension"),
            ],
            [
                InlineKeyboardButton(text="Shangri-La", callback_data="map_shangri_la"),
            ],
            [
                InlineKeyboardButton(text="Moon", callback_data="map_moon"),
            ]
        ])
    return keyboard