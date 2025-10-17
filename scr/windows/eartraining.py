import webbrowser
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from windows.regexp.design_levelselection import Ui_MainWindow
from database import Database
import sqlite3

class RegExpWinListening(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.db = Database()  # Инициализация подключения к базе данных
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)
        # Подключение кнопок к методу onClick
        self.pushButton.pressed.connect(lambda: self.onClick(self.pushButton.objectName(), "1"))
        self.pushButton_2.pressed.connect(lambda: self.onClick(self.pushButton_2.objectName(), "2"))
        self.pushButton_3.pressed.connect(lambda: self.onClick(self.pushButton_3.objectName(), "3"))
        self.pushButton_4.pressed.connect(lambda: self.onClick(self.pushButton_4.objectName(), "4"))
        self.pushButton_5.pressed.connect(lambda: self.onClick(self.pushButton_5.objectName(), "5"))
        self.pushButton_6.pressed.connect(lambda: self.onClick(self.pushButton_6.objectName(), "6"))
        self.pushButton_7.pressed.connect(lambda: self.onClick(self.pushButton_7.objectName(), "7"))
        self.pushButton_8.pressed.connect(lambda: self.onClick(self.pushButton_8.objectName(), "8"))
        self.pushButton_9.pressed.connect(lambda: self.onClick(self.pushButton_9.objectName(), "9"))
        self.pushButton_10.pressed.connect(lambda: self.onClick(self.pushButton_10.objectName(), "10"))
        self.pushButton_11.pressed.connect(lambda: self.onClick(self.pushButton_11.objectName(), "11"))
        self.pushButton_12.pressed.connect(lambda: self.onClick(self.pushButton_12.objectName(), "12"))
        self.pushButton_13.pressed.connect(lambda: self.onClick(self.pushButton_13.objectName(), "13"))
        self.pushButton_14.pressed.connect(lambda: self.onClick(self.pushButton_14.objectName(), "14"))
        self.pushButton_15.pressed.connect(lambda: self.onClick(self.pushButton_15.objectName(), "15"))

    def onClick(self, name, level_name):
        """
        Открывает YouTube-ссылку для указанного уровня из таблицы listening_urls и закрывает окно.
        """
        try:
            # Получаем URL из таблицы listening_urls по id
            url = self.db.get_listening_url(int(level_name))
            if url:
                webbrowser.open_new(url)
                self.close()
            else:
                print(f"No URL found for id {level_name}")
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

    def __del__(self):
        """
        Закрывает соединение с базой данных при уничтожении объекта.
        """
        self.db.close()