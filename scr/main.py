import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from design.design_mainpage import Ui_MainWindow
import autoritation
from create_db import create_database

from windows.regularlessons import RegExpWin
from windows.eartraining import RegExpWinListening
from windows.transword import TransWordsWin
from windows.translator import TranslatorWin
from windows.knowledgetest import KnowledgeTestWin


class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        # Initialize the database
        create_database()

        # Initialize windows
        self.regExpWin = RegExpWin()
        self.regExpWinListening = RegExpWinListening()
        self.transwordWin = TransWordsWin()
        self.translatorWin = TranslatorWin()
        self.knowledgetestWin = KnowledgeTestWin()

        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.init_UI()

        self.pushButton_regularlessons.pressed.connect(self.regularlessons)
        self.pushButton_eartraining.pressed.connect(self.eartraining)
        self.pushButton_knowledgetest.pressed.connect(self.knowledgetest)
        self.pushButton_settings.pressed.connect(self.settings)
        self.pushButton_transword.pressed.connect(self.transword)
        self.pushButton_translator.pressed.connect(self.translator)

    def init_UI(self):
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)

    def regularlessons(self):
        self.regExpWin.show()

    def eartraining(self):
        self.regExpWinListening.show()
        print('eartraining')

    def knowledgetest(self):
        self.knowledgetestWin.show()
        print('knowledgetest')

    def settings(self):
        print('settings')

    def transword(self):
        self.transwordWin.show()
        print('transword')

    def translator(self):
        self.translatorWin.show()
        print('translator')


app = QtWidgets.QApplication([])
start = autoritation.Registration(Main())
start.show()
sys.exit(app.exec())
