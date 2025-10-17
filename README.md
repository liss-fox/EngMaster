# EngMaster

EngMaster is a Python-based application built with PyQt6 and SQLite, designed to help beginners learn English at A1 and A2 levels. It offers interactive modules for studying vocabulary, taking knowledge tests, practicing listening skills via YouTube audio, and translating words. The application features a modular structure and an intuitive interface, making it easy to extend and maintain.

## Features
- **User Authentication**: Login and registration system with data stored in a database.
- **Vocabulary Learning**: Exercises for memorizing words and translations for A1 and A2 levels.
- **Knowledge Tests**: Multiple-choice questions to test vocabulary and grammar.
- **Listening Practice**: Playback of YouTube audio for listening exercises.
- **Word Translation**: Interactive mode for practicing word translations.
- **Translator**: Text translation functionality.
- **User Interface**: Built with PyQt6, fixed window size (1600x900).

## Database Structure
The application uses a SQLite database (`main.db`), automatically created on startup. The database includes the following tables:
- **users**: Stores user login and password (`ID`, `Login`, `Password`).
- **levels**: Contains vocabulary for learning (20 words for A1 and A2, fields: `ID`, `Standart`, `Num`, `Word`, `Translation`).
- **knowledge_tests**: Stores test questions (10 questions for A1 and A2, fields: `ID`, `Type`, `Num`, `question`, `optionA`, `optionB`, `optionC`, `optionD`, `rightAnswer`).
- **listening_urls**: Stores YouTube links for audio exercises (15 links, fields: `id`, `url`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/liss-fox/EngMaster.git
   cd EngMaster
   ```
2. Ensure you have Python 3.8+ installed (3.10 recommended).
3. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Contents of `requirements.txt`:
   ```
   PyQt6==6.9.1
   googletrans==4.0.0-rc1
   ```

## Usage
1. Run the application:
   ```bash
   python src/main.py
   ```
   This will create `main.db` with initial data.
2. Log in using default credentials (e.g., `user1`/`password123` or `admin`/`adminpass`).
3. Select a mode from the main menu:
   - **Regular Lessons**: Study words with "Ready"/"NotReady" buttons.
   - **Ear Training**: Listen to audio via YouTube links.
   - **Knowledge Test**: Answer multiple-choice questions.
   - **Transword**: Practice translating random words.
   - **Translator**: Translate what you need.
4. Follow the on-screen instructions to complete exercises.

## Project Structure
```
EngMaster/
├── src/
│   ├── main.py                 # Main application file
│   ├── create_db.py            # Creates the main.db database
│   ├── database.py             # Database class for interacting with main.db
│   ├── autoritation.py         # User authentication and registration
│   ├── design/
│   │   ├── design_autoritation.py      # UI for authentication
│   │   ├── design_mainpage.py         # UI for the main window
│   │   ├── design_knowledgetest.py    # UI for knowledge tests
│   │   ├── design_levelselection.py   # UI for level selection
│   │   ├── design_regularlesson.py    # UI for regular lessons
│   │   ├── design_transword.py        # UI for word translation
│   │   ├── design_translator.py       # UI for the translator
│   │   ├── UIFiles/                   # Source .ui files (if present)
│   ├── windows/
│   │   ├── eartraining.py      # Listening practice module
│   │   ├── knowledgetest.py    # Knowledge test module
│   │   ├── regularlessons.py   # Vocabulary learning module
│   │   ├── transword.py        # Word translation practice
│   │   ├── translator.py       # Translator module
│   │   ├── regexp/
│   │   │   ├── design_knowledgetest.py   # UI for knowledge tests
│   │   │   ├── design_levelselection.py  # UI for level selection
│   │   │   ├── design_regularlesson.py   # UI for regular lessons
│   │   │   ├── design_transword.py       # UI for word translation
│   │   │   ├── design_translator.py      # UI for the translator
│   │   │   ├── question.png             # Question icon
│   │   │   ├── whiteangle.png           # Additional image
│   │   │   ├── ico/                     # Icon folder
├── Screenshots/                # Screenshots of the application
│   ├── Autorization.png
│   ├── Main menu.png
│   ├── Regular lessons.png
│   ├── Selecting level.png
│   ├── Test mode.png
│   ├── Translate the word mode.png
│   ├── Translator.png
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Ignored files
```

## Requirements
- Python 3.8+ (3.10 recommended)
- PyQt6 6.9.1
- SQLite (built into Python)

## Future Improvements
- Add support for B1 and higher levels.
- Implement storage of test results and progress in the database.
- Optimize the interface for responsive design.
- Add automated tests using `pytest`.
- Support localization for other languages.
- Enhance the translator module functionality.

## License
MIT License

## Contact
- GitHub: [liss-fox](https://github.com/liss-fox)
- Email: no8borders@tutamail.com
