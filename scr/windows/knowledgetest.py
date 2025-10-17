import sys

from PyQt6.QtWidgets import QLabel
from windows.regexp.design_knowledgetest import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer, QEventLoop

import sqlite3
import random
from database import Database 


class KnowledgeTestWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)
        
        self.db = Database()

        self.button_a.pressed.connect(self.check_user_answer)
        self.button_b.pressed.connect(self.check_user_answer)
        self.button_c.pressed.connect(self.check_user_answer)
        self.button_d.pressed.connect(self.check_user_answer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clear_feedback)

        loop = QEventLoop()
        self.timer.timeout.connect(loop.quit)

        self.rightanswers = 0
        self.falseanswers = 0
        self.current_question_index = 0
        self.correct_answer = ""

        # Загружаем первый вопрос при инициализации окна
        self.load_question()

    def load_question(self, level="A1"):
        """
        Загружает вопрос из таблицы knowledge_tests для указанного уровня (например, A1).
        """
        try:
            # Увеличиваем индекс вопроса
            self.current_question_index += 1
            # Выбираем вопрос по Type и Num
            self.db.cursor.execute(
                "SELECT question, optionA, optionB, optionC, optionD, rightAnswer FROM knowledge_tests WHERE Type = ? AND Num = ?",
                (level, self.current_question_index)
            )
            question = self.db.cursor.fetchone()
            print(f"Loading question for {level}, Num {self.current_question_index}: {question}")  # Отладочный вывод

            if question:
                # Загружаем текст вопроса и варианты ответов
                self.Question.appendPlainText(question[0])  # question
                self.answer_a.setText(f"A: {question[1]}")  # optionA
                self.answer_b.setText(f"B: {question[2]}")  # optionB
                self.answer_c.setText(f"C: {question[3]}")  # optionC
                self.answer_d.setText(f"D: {question[4]}")  # optionD
                self.correct_answer = question[5]  # rightAnswer
            else:
                # Если вопросы закончились, показываем результаты
                print(f"No more questions found for {level}.")
                self.Question.appendPlainText(
                    f"Правильных ответов: {self.rightanswers} \nНеправильных ответов: {self.falseanswers}"
                )
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            self.Question.appendPlainText("Ошибка при загрузке вопроса.")
        finally:
            # Не закрываем соединение здесь, так как оно может понадобиться для других запросов
            pass

    def check_user_answer(self):

        # Определяем, какая кнопка была нажата
        selected_button = self.sender()
        selected_answer = ""

        # Определяем выбранный ответ в зависимости от нажатой кнопки
        if selected_button == self.button_a:
            selected_answer = self.answer_a.text()
        elif selected_button == self.button_b:
            selected_answer = self.answer_b.text()
        elif selected_button == self.button_c:
            selected_answer = self.answer_c.text()
        elif selected_button == self.button_d:
            selected_answer = self.answer_d.text()

        print(selected_answer)
        print(self.correct_answer)

        # Сравниваем выбранный ответ с правильным ответом
        if selected_answer[3:] == self.correct_answer:
            self.rightanswers += 1
            print("ok")
            self.Question.appendPlainText("Правильно!")
            selected_button.setStyleSheet("background-color: green")
        else:
            self.falseanswers += 1
            print("notok")
            self.Question.appendPlainText("Неправильно!")
            selected_button.setStyleSheet("background-color: red")

        # Блокировка ввода перед стартом таймера
        for button in [self.button_a, self.button_b, self.button_c, self.button_d]:
            button.setDisabled(True)
        # Запускаем таймер для очистки сообщения обратной связи
        self.timer.start(2000)

    def clear_feedback(self):
        self.Question.clear()

        # Очистить вывод
        for answer in [self.answer_a, self.answer_b, self.answer_c, self.answer_d]:
            answer.setText("")  # Очистить вывод

        # Возвращение цвета кнопок на исходный
        for button in [self.button_a, self.button_b, self.button_c, self.button_d]:
            button.setStyleSheet("")

        # Разблокировка ввода после остановки таймера
        for button in [self.button_a, self.button_b, self.button_c, self.button_d]:
            button.setEnabled(True)

        self.timer.stop()
        self.load_question()
