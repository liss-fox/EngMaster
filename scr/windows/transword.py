import sys
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from windows.regexp.design_transword import Ui_MainWindow
from database import Database

class TransWordsWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.db = Database()  # Инициализация подключения к базе данных
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)
        self.pushButton.pressed.connect(self.check_user_answer)
        self.wordinput.returnPressed.connect(self.check_user_answer)
        self.pushButton_2.pressed.connect(self.advise)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clear_feedback)
        self.timer.setSingleShot(True)
        self.translation = ""
        self.rightanswers = 0
        self.falseanswers = 0
        self.random_word()

    def random_word(self):
        """
        Выбирает случайное слово и перевод из таблицы levels.
        """
        try:
            word_data = self.db.get_random_word()
            if word_data:
                self.wordshow.setText(word_data[0])  # Word
                self.translation = word_data[1]  # Translation
                self.wordinput.setFocus()
                print(f"Selected word: {word_data[0]}, translation: {word_data[1]}")
            else:
                print("Не удалось найти случайное слово.")
                self.wordshow.setText("Нет слов в базе")
                self.translation = ""
        except Exception as e:
            print(f"Ошибка при выборе слова: {e}")
            self.wordshow.setText("Ошибка")

    def check_user_answer(self):
        """
        Проверяет ответ пользователя и обновляет UI.
        """
        self.wordinput.setDisabled(True)
        user_answer = self.wordinput.text()
        if user_answer.lower() == self.translation.lower():
            self.wordshow.setStyleSheet("color: rgb(0, 200, 0)")
            self.wordshow.setText("Right!")
            self.rightanswers += 1
            self.right_ans.setText(f"Right: {self.rightanswers}")
            print("Верно")
        else:
            self.wordshow.setStyleSheet("color: rgb(255, 0, 0)")
            text = "Верный ответ: "
            sentence = f"{text}{self.translation}"
            self.wordshow.setText(sentence)
            self.falseanswers += 1
            self.false_ans.setText(f"False: {self.falseanswers}")
            print("Неверно")
        self.timer.start(2000)

    def advise(self):
        print("It's all right!")

    def clear_feedback(self):
        """
        Очищает обратную связь и загружает новое слово.
        """
        self.wordshow.setText("")
        self.wordinput.setText("")
        self.wordshow.setStyleSheet("color: rgb(255, 255, 255)")
        self.wordinput.setDisabled(False)
        self.random_word()

    def __del__(self):
        """
        Закрывает соединение с базой данных.
        """
        self.db.close()