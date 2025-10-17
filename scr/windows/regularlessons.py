import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from windows.regexp.design_levelselection import Ui_MainWindow
from windows.regexp.design_regularlesson import Ui_MainWindow as Ui_MainWindow2
from database import Database
import sqlite3

class RegExpWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.db = Database()  # Инициализация подключения к базе данных
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.regExpWin2 = RegExpWin2()
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)
        # Подключение кнопок к методу onClick
        self.pushButton.pressed.connect(lambda: self.onClick(self.pushButton.objectName(), "A1", 1))
        self.pushButton_2.pressed.connect(lambda: self.onClick(self.pushButton_2.objectName(), "A1", 2))
        self.pushButton_3.pressed.connect(lambda: self.onClick(self.pushButton_3.objectName(), "A2", 1))
        self.pushButton_4.pressed.connect(lambda: self.onClick(self.pushButton_4.objectName(), "A2", 2))
        self.pushButton_5.pressed.connect(lambda: self.onClick(self.pushButton_5.objectName(), "A1", 3))
        self.pushButton_6.pressed.connect(lambda: self.onClick(self.pushButton_6.objectName(), "A1", 4))
        self.pushButton_7.pressed.connect(lambda: self.onClick(self.pushButton_7.objectName(), "A1", 5))
        self.pushButton_8.pressed.connect(lambda: self.onClick(self.pushButton_8.objectName(), "A2", 3))
        self.pushButton_9.pressed.connect(lambda: self.onClick(self.pushButton_9.objectName(), "A2", 4))
        self.pushButton_10.pressed.connect(lambda: self.onClick(self.pushButton_10.objectName(), "A2", 5))
        self.pushButton_11.pressed.connect(lambda: self.onClick(self.pushButton_11.objectName(), "A1", 6))
        self.pushButton_12.pressed.connect(lambda: self.onClick(self.pushButton_12.objectName(), "A1", 7))
        self.pushButton_13.pressed.connect(lambda: self.onClick(self.pushButton_13.objectName(), "A2", 6))
        self.pushButton_14.pressed.connect(lambda: self.onClick(self.pushButton_14.objectName(), "A2", 7))
        self.pushButton_15.pressed.connect(lambda: self.onClick(self.pushButton_15.objectName(), "A1", 8))

    def onClick(self, name, standart, num):
        """
        Открывает окно RegExpWin2 и передаёт параметры уровня (Standart и Num).
        """
        try:
            self.regExpWin2.show()
            self.regExpWin2.levelnumber.setText(f"Level {num} ({standart})")
            self.regExpWin2.levelmain(standart, num)
        except Exception as e:
            print(f"Ошибка при открытии уровня: {e}")

    def __del__(self):
        """
        Закрывает соединение с базой данных.
        """
        self.db.close()

class RegExpWin2(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.db = Database()  # Инициализация подключения к базе данных
        self.ui = Ui_MainWindow2()
        self.setupUi(self)
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)
        self.current_index = -1  # Начинаем с -1, так как увеличим в levelmain
        self.russianWord = ""
        self.englishWord = ""
        self.standart = None  # Инициализация атрибута standart
        self.num = None  # Инициализация атрибута num
        self.words = []  # Список слов для текущего уровня
        self.notready.pressed.connect(self.NotReadyPress)
        self.ready.pressed.connect(self.ReadyPress)

    def levelmain(self, standart, num):
        """
        Загружает слово и перевод из таблицы levels для указанного уровня (Standart и Num).
        """
        try:
            # Сохраняем standart и num как атрибуты
            self.standart = standart
            self.num = num
            # Получаем все слова для уровня один раз
            if not self.words or self.standart != standart or self.num != num:
                self.words = self.db.get_level_words(standart, num)
                self.current_index = -1  # Сбрасываем индекс при смене уровня
            # Увеличиваем индекс
            self.current_index += 1
            print(f"Loading word {self.current_index} for {standart}, Num {num}")
            if self.current_index < len(self.words):
                # Выбираем слово по текущему индексу
                word_data = self.words[self.current_index]
                self.russianWord = word_data[4]  # Translation
                self.englishWord = word_data[3]  # Word
                self.russianword.setText(self.russianWord)
                self.englishword.setText(self.englishWord)
                print(f"Loaded: {self.englishWord} - {self.russianWord}")
            else:
                print(f"Нет слов для {standart}, Num {num}")
                self.russianword.setText("Нет слов")
                self.englishword.setText("Нет слов")
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            self.russianword.setText("Ошибка")
            self.englishword.setText("Ошибка")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

    def NotReadyPress(self):
        print("NotReady")

    def ReadyPress(self):
        print("Ready")
        self.levelmain(self.standart, self.num)  # Передаем текущие standart и num

    def __del__(self):
        """
        Закрывает соединение с базой данных.
        """
        self.db.close()