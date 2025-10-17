import sqlite3

def create_database(db_name="main.db"):
    """
    Создаёт базу данных main.db с таблицами users, levels и knowledge_tests.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Login TEXT NOT NULL,
            Password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS levels (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Standart TEXT NOT NULL,
            Num INTEGER NOT NULL,
            Word TEXT NOT NULL,
            Translation TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge_tests (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Type TEXT NOT NULL,
            Num INTEGER NOT NULL,
            question TEXT NOT NULL,
            optionA TEXT NOT NULL,
            optionB TEXT NOT NULL,
            optionC TEXT NOT NULL,
            optionD TEXT NOT NULL,
            rightAnswer TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listening_urls (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL
        )
    ''')

    # Вставка начальных данных (пример, можно убрать или изменить)
    initial_users = [
        ("user1", "123"),
        ("admin", "admin")
    ]
    cursor.executemany('INSERT OR IGNORE INTO users (Login, Password) VALUES (?, ?)', initial_users)

    initial_levels = [
        # A1, уровень 1
        ("A1", 1, "hello", "привет"),
        ("A1", 1, "cat", "кот"),
        ("A1", 1, "dog", "собака"),
        ("A1", 1, "sun", "солнце"),
        ("A1", 1, "one", "один"),
        # A1, уровень 2
        ("A1", 2, "world", "мир"),
        ("A1", 2, "tree", "дерево"),
        ("A1", 2, "house", "дом"),
        ("A1", 2, "two", "два"),
        ("A1", 2, "water", "вода"),
        # A2, уровень 1
        ("A2", 1, "book", "книга"),
        ("A2", 1, "family", "семья"),
        ("A2", 1, "school", "школа"),
        ("A2", 1, "friend", "друг"),
        ("A2", 1, "morning", "утро"),
        # A2, уровень 2
        ("A2", 2, "city", "город"),
        ("A2", 2, "teacher", "учитель"),
        ("A2", 2, "time", "время"),
        ("A2", 2, "food", "еда"),
        ("A2", 2, "travel", "путешествие")
    ]
    cursor.executemany('INSERT OR IGNORE INTO levels (Standart, Num, Word, Translation) VALUES (?, ?, ?, ?)', initial_levels)

    initial_tests = [
        ("A1", 1, "What is the translation of 'hello'?", "привет", "пока", "дом", "книга", "привет"),
        ("A1", 2, "What is the translation of 'world'?", "книга", "мир", "дерево", "небо", "мир"),
        ("A1", 3, "What is the capital of France?", "London", "Berlin", "Paris", "Rome", "Paris"),
        ("A1", 4, "How many days are there in a week?", "5", "6", "7", "8", "7"),
        ("A1", 5, "Which of the following is a fruit?", "Carrot","Potato", "Apple", "Broccoli", "Apple"),
        ("A2", 1, "What is the translation of 'house'?", "дерево", "дом", "машина", "стол", "дом"),
        ("A2", 2, "Choose the correct form: She ___ to school every day.", "go", "goes", "going", "gone", "goes"),
        ("A2", 3, "What is the third day of the week?", "Monday", "Tuesday", "Wednesday", "Thursday", "Wednesday"),
        ("A2", 4, "Who is a 'sister' in a family?", "Father", "Mother", "Brother", "Female sibling", "Female sibling"),
        ("A2", 5, "Where is the book? It is ___ the table.", "on", "in", "at", "under", "on")
    ]
    cursor.executemany('INSERT OR IGNORE INTO knowledge_tests (Type, Num, question, optionA, optionB, optionC, optionD, rightAnswer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', initial_tests)

    initial_urls = [
        (1, "https://youtu.be/0UCs9_ckZrU?si=1SyGK9OD_aUlwqwE"),
        (2, "https://youtu.be/jbl8o7c48Uo?si=xAordAznMTaNrodw"),
        (3, "https://youtu.be/EajG5PnezOU?si=UlVTComuQCNFH1nk"),
        (4, "https://youtu.be/2h2abaL2Zhw?si=XJTeKmxW1aQR2A13"),
        (5, "https://youtu.be/nNcPsp9bqQ8?si=oXZsEqaUeQgFS8Hm"),
        (6, "https://youtu.be/-J4yxrA_7f4?si=pmt3saezLmyfjK2L"),
        (7, "https://youtu.be/7BKDaqY2kMI?si=RfCv_CpoLS-v8yK-"),
        (8, "https://youtu.be/yvPNKeT5plU?si=uPN6r3ROvGLvZu1H"),
        (9, "https://youtu.be/XDlyKx_Qw30?si=RLxxMhux5XNNYLFU"),
        (10, "https://youtu.be/GnYb4Xq24kA?si=MdCUJQY-iyTiYmR6"),
        (11, "https://youtu.be/S3Vud1ZuIsY?si=jyQSa4oUsuu0ETRD"),
        (12, "https://youtu.be/2Xj9R4y0O1s?si=S-DLMghop6vrc3Fi"),
        (13, "https://youtu.be/BzjUxSHkbYM?si=37k6t-xnDrelLmbz"),
        (14, "https://youtu.be/xugChZoZOHk?si=jn_0iYH0iHAaOGEb"),
        (15, "https://youtu.be/-RPemLPQ9-E?si=3x1UG0IWEI5pXYYn")
    ]
    cursor.executemany('INSERT OR IGNORE INTO listening_urls (id, url) VALUES (?, ?)', initial_urls)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print(f"База данных {db_name} успешно создана.")

if __name__ == "__main__":
    create_database()