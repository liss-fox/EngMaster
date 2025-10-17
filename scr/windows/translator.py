import sys

from PyQt6.QtWidgets import QLabel
from windows.regexp.design_translator import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from googletrans import Translator

class TranslatorWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('EngMaster')
        self.setFixedSize(1600, 900)

        self.langchange.pressed.connect(self.language_change)
        self.translate_but.pressed.connect(self.translate_text)

        self.translator = Translator()


    def language_change(self):
        lang1info = self.lang1.text()
        lang2info = self.lang2.text()
        self.lang1.setText(lang2info)
        self.lang2.setText(lang1info)
        print("language has been changed")


    def translate_text(self):
        print("works")
        source_text = self.input.toPlainText()
        print("works")
        print(self.lang1.text())
        try:
        # Определяем язык введенного текста
            if self.lang1.text() == "Русский":
                source_lang = "ru"
                target_lang = "en"
            elif self.lang1.text() == "Английский":
                source_lang = "en"
                target_lang = "ru"
            else:
                source_lang = self.translator.detect(source_text).lang
                target_lang = "kk"

            translated_text = self.translator.translate(source_text, src=source_lang, dest=target_lang)
            self.result.clear()
            self.result.appendPlainText(translated_text.text)

        except Exception as e:
            print("text has been translated")
