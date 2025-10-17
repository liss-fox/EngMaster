# EngMaster

EngMaster — это приложение для изучения английского языка, разработанное на Python с использованием PyQt6 и SQLite. Оно предназначено для начинающих (уровни A1 и A2) и включает модули для изучения слов, тестирования знаний, тренировки аудирования и перевода слов. Приложение имеет интуитивный интерфейс и модульную структуру, что делает его удобным для расширения.

## Особенности
- **Авторизация**: Регистрация и вход пользователей с сохранением данных в базе.
- **Изучение слов**: Упражнения для запоминания слов и переводов (уровни A1 и A2).
- **Тесты знаний**: Вопросы с множественным выбором для проверки лексики и грамматики.
- **Тренировка аудирования**: Воспроизведение YouTube-видео для тренировки восприятия на слух.
- **Перевод слов**: Интерактивный режим для тренировки перевода случайных слов.
- **Переводчик**: (В разработке, если функционал ограничен) Перевод текста.
- **Интерфейс**: Разработан на PyQt6, фиксированный размер окна (1600x900).

## Структура базы данных
Приложение использует базу данных SQLite (`main.db`), создаваемую автоматически при запуске. Таблицы:
- **users**: Хранит логины и пароли (`ID`, `Login`, `Password`).
- **levels**: Слова для изучения (20 слов для A1 и A2, поля: `ID`, `Standart`, `Num`, `Word`, `Translation`).
- **knowledge_tests**: Тестовые вопросы (10 вопросов для A1 и A2, поля: `ID`, `Type`, `Num`, `question`, `optionA`, `optionB`, `optionC`, `optionD`, `rightAnswer`).
- **listening_urls**: YouTube-ссылки для аудиоупражнений (15 ссылок, поля: `id`, `url`).

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/liss-fox/EngMaster.git
   cd EngMaster
   ```
2. Установите Python 3.8+ (рекомендуется 3.10).
3. Создайте и активируйте виртуальное окружение (опционально):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   Содержимое `requirements.txt`:
   ```
   PyQt6==6.9.1
   googletrans==4.0.0-rc1
   ```

## Использование
1. Запустите приложение:
   ```bash
   python src/main.py
   ```
   Это создаст `main.db` с начальными данными.
2. Войдите с логином и паролем (по умолчанию: `user1`/`password123` или `admin`/`admin`).
3. Выберите режим в главном меню:
   - **Regular Lessons**: Изучение слов с переключением через кнопки "Ready"/"NotReady".
   - **Ear Training**: Прослушивание аудио через YouTube-ссылки.
   - **Knowledge Test**: Тесты с множественным выбором.
   - **Transword**: Тренировка перевода случайных слов.
   - **Translator**: Переводчик.
4. Следуйте инструкциям в интерфейсе для прохождения упражнений.

## Структура проекта
```
EngMaster/
├── src/
│   ├── main.py                 # Главный файл приложения
│   ├── create_db.py            # Создание базы данных main.db
│   ├── database.py             # Класс Database для работы с main.db
│   ├── autoritation.py         # Авторизация и регистрация пользователей
│   ├── design/
│   │   ├── design_autoritation.py      # UI для авторизации
│   │   ├── design_mainpage.py         # UI главного окна
│   │   ├── design_knowledgetest.py    # UI для тестов
│   │   ├── design_levelselection.py   # UI для выбора уровня
│   │   ├── design_regularlesson.py    # UI для уроков
│   │   ├── design_transword.py        # UI для перевода слов
│   │   ├── design_translator.py       # UI для переводчика
│   │   ├── UIFiles/                   # Исходные .ui файлы
│   ├── windows/
│   │   ├── eartraining.py      # Тренировка аудирования
│   │   ├── knowledgetest.py    # Тесты знаний
│   │   ├── regularlessons.py   # Упражнения по изучению слов
│   │   ├── transword.py        # Тренировка перевода слов
│   │   ├── translator.py       # Переводчик
│   │   ├── regexp/
│   │   │   ├── design_knowledgetest.py   # UI для тестов (дубликат)
│   │   │   ├── design_levelselection.py  # UI для выбора уровня
│   │   │   ├── design_regularlesson.py   # UI для уроков
│   │   │   ├── design_transword.py       # UI для перевода слов
│   │   │   ├── design_translator.py      # UI для переводчика
│   │   │   ├── question.png             # Иконка вопроса
│   │   │   ├── whiteangle.png           # Дополнительное изображение
│   │   │   ├── ico/                     # Папка с иконками
├── Screenshots/                # Скриншоты приложения
│   ├── Autorization.png
│   ├── Main menu.png
│   ├── Regular lessons.png
│   ├── Selecting level.png
│   ├── Test mode.png
│   ├── Translate the word mode.png
│   ├── Translator.png
├── requirements.txt            # Зависимости
├── README_ru.md                # Описание проекта
├── .gitignore                  # Игнорируемые файлы
```

## Требования
- Python 3.8+ (рекомендуется 3.10)
- PyQt6 6.9.1
- SQLite (встроен в Python)

## Будущие улучшения
- Добавить поддержку уровней B1 и выше.
- Реализовать сохранение результатов тестов и прогресса в базе данных.
- Оптимизировать интерфейс для адаптивного дизайна.
- Добавить автоматические тесты с использованием `pytest`.
- Внедрить локализацию для других языков.
- Расширить функционал переводчика (`translator.py`).

## Лицензия
MIT License

## Контакты
- GitHub: [liss-fox](https://github.com/liss-fox)
- Email: no8borders@tutamail.com
