import sys

from PyQt6 import QtWidgets
from design.design_autoritation import Ui_Form
import sqlite3

db = sqlite3.connect('main.db')
cursor = db.cursor()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec())


class Registration(QtWidgets.QMainWindow, Ui_Form):
    isEnter = False
    application = None

    def __init__(self, application):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)
        self.application = application

    def reg(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        cursor.execute(f'SELECT Login FROM users WHERE Login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users (Login, Password) VALUES ("{user_login}", "{user_password}")')
            db.commit()

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        try:
            cursor.execute(f'SELECT Login FROM users WHERE Login="{user_login}"')
            check_login = cursor.fetchall()

            cursor.execute(f'SELECT Password FROM users WHERE Login="{user_login}"')
            check_password = cursor.fetchall()

            if check_login[0][0] == user_login and check_password[0][0] == user_password:
                self.application.show()
                self.close()

            self.label_status.setText('Ошибка авторизации!')
            self.lineEdit_2.setText("")

        except:
            self.lineEdit_2.setText("")
            self.label_status.setText('Ошибка авторизации!')
