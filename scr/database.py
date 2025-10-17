import sqlite3

class Database:
    def __init__(self, db_name="main.db"):
        """
        Инициализирует подключение к базе данных main.db.
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

    def get_user(self, login):
        """
        Получает пользователя по логину.
        Возвращает кортеж (ID, Login, Password) или None, если пользователь не найден.
        """
        try:
            self.cursor.execute('SELECT * FROM users WHERE Login = ?', (login,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Ошибка при получении пользователя: {e}")
            return None

    def get_level_words(self, standart, num):
        """
        Получает слова для указанного уровня (Standart) и номера (Num).
        Возвращает список кортежей (ID, Standart, Num, Word, Translation).
        """
        try:
            self.cursor.execute(
                'SELECT * FROM levels WHERE Standart = ? AND Num = ?',
                (standart, num)
            )
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении слов: {e}")
            return []

    def get_test_question(self, type_, num):
        """
        Получает вопрос теста по типу (Type) и номеру (Num).
        Возвращает кортеж (question, optionA, optionB, optionC, optionD, rightAnswer) или None.
        """
        try:
            self.cursor.execute(
                'SELECT question, optionA, optionB, optionC, optionD, rightAnswer '
                'FROM knowledge_tests WHERE Type = ? AND Num = ?',
                (type_, num)
            )
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Ошибка при получении вопроса: {e}")
            return None
        
    def get_listening_url(self, id_):
        """
        Получает YouTube-ссылку по ID из таблицы listening_urls.
        Возвращает URL (строка) или None, если не найдено.
        """
        try:
            self.cursor.execute('SELECT url FROM listening_urls WHERE id = ?', (id_,))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Ошибка при получении URL: {e}")
            return None
        
    def get_random_word(self):
        """
        Получает случайное слово и перевод из таблицы levels.
        Возвращает кортеж (Word, Translation) или None, если слов нет.
        """
        try:
            self.cursor.execute('SELECT Word, Translation FROM levels ORDER BY RANDOM() LIMIT 1')
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Ошибка при получении случайного слова: {e}")
            return None

    def close(self):
        """
        Сохраняет изменения и закрывает соединение с базой данных.
        """
        try:
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Ошибка при закрытии базы данных: {e}")

    def __del__(self):
        """
        Гарантирует закрытие соединения при уничтожении объекта.
        """
        self.close()