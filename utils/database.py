import sqlite3

DP_PATH = 'database.db'

def init_db(): 
    connection = sqlite3.connect(DP_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            language TEXT DEFAULT 'en'
        )
    ''')
    connection.commit()
    connection.close()

def set_user_language(user_id: int, language: str) -> None:
    connection = sqlite3.connect(DP_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users (user_id, language)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET language=excluded.language
    ''', (user_id, language))
    connection.commit()
    connection.close()


def get_user_language(user_id: int) -> str: 
    connection = sqlite3.connect(DP_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT language FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else 'en'