from random import randint
from Words import word_list
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from letter import Ui_Form
from random import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        def random():
            total_lines = len(word_list)  # Подсчет кол-ва строк в файле Words.py
            random_line = randint(1, total_lines)  # Случайный выбор строки
            hidden_word = word_list[random_line - 1][0]  # Загаданное слово
            hidden_question = word_list[random_line - 1][1]  # Загаданный вопрос
            print("Загаданное слово:", hidden_word)
            print("Внимание вопрос!", hidden_question)
            split(hidden_word)

        def split(hidden_word):
            letters_list = [char for char in hidden_word]  # Массив букв
            print("Массив букв:", letters_list)
            total = len(letters_list)  # Кол-во букв в слове
            print("Кол-во букв в слове:", total)

        random()

        hidden_word = "test"

        i = 0
        while i < len(hidden_word):

            new_letter_box = QTextEdit()

            new_letter_box.setReadOnly(True)
            letter = hidden_word[i]
            new_letter_box.setObjectName(letter)
            new_letter_box.setText(letter)
            self.ui.horizontalLayout.addWidget(new_letter_box)
            i += 1
        print(self.ui.horizontalLayout.itemAt(0).widget().toPlainText())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

