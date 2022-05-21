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

        def random_index():
            return randint(1, len(word_list))

        def split(hidden_word):
            letters_list = [char for char in hidden_word]  # Массив букв
            print("Массив букв:", letters_list)
            total = len(letters_list)  # Кол-во букв в слове
            print("Кол-во букв в слове:", total)

        random()

        index = random_index()
        hidden_word = word_list[index][0]
        hidden_question = word_list[index][1]
        print(hidden_question)

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


