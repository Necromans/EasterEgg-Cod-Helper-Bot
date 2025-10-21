import json
import os

# Кэш переводов, чтобы не читать файлы каждый раз
_locales_cache = {}

def load_locale(language_code: str) -> dict: 
    global _locales_cache
    if language_code in _locales_cache:
        return _locales_cache[language_code]

    path = os.path.join("locales", f"{language_code}.json")
    if not os.path.exists(path):
        path = os.path.join("locales", "en.json") 

    with open(path, "r", encoding="utf-8") as file:
        _locales_cache[language_code] = json.load(file)

    return _locales_cache[language_code]

def translate(language_code: str, key: str) -> str:
    locale = load_locale(language_code)
    return locale.get(key, key)  # Возвращаем ключ, если перевод не найден