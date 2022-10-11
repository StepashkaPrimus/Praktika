from data_base import word_list
from main_widget import Ui_Form
from PyQt5.QtWidgets import QTextEdit, QMainWindow, QWidget, QListWidgetItem, QListWidget
from PyQt5.QtGui import QTransform
from PyQt5 import QtCore
from random import randint



step = 1
dialogs = ""
player_1 = ""
player_2 = ""
player_3 = ""
players = ()
points = [0, 0, 0]
presents = [[], [], []]
win = 0
winner = ""
number = 0


def random():
    total_lines = len(word_list)  # Подсчет кол-ва строк в файле data.py
    random_line = randint(1, total_lines)  # Случайный выбор строки
    hidden_question = word_list[random_line - 1][1]  # Вопрос
    hidden_word = word_list[random_line - 1][0]  # Загаданное слово
    print("Вопрос: ", hidden_question)
    print("Слово: ", hidden_word)
    global a
    a = list(hidden_word)
    return [hidden_question, hidden_word]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rotate_transform = QTransform().rotate(-90)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show_title()
        self.random = random()
        self.show_words()
        self.show_dialogs()

    def show_title(self):
        title = "[Игра] Поле Чудес"
        self.ui.title_label.setText(title)

    def show_question(self):
        question = self.random[0]
        self.ui.question_label.setText(question)

    def show_words(self):
        hidden_word = self.random[1]
        for i in range(len(hidden_word)):
            new_letter_box = QTextEdit()
            new_letter_box.setReadOnly(True)
            letter = hidden_word[i]  #
            new_letter_box.setObjectName(letter)
            new_letter_box.setText(hidden_word[i]) #Можете его переместить в другую часть кода для отображения только после ответа игрока,
            self.ui.show_words.addWidget(new_letter_box)
        print(self.ui.show_words.itemAt(0).widget().toPlainText())

    def show_dialogs(self):
        global step

        if step == 1:
            greetings = "Ведущий:\nЗдравствуйте, уважаемые дамы и господа!\nВ эфире капитал-шоу Поле чудес!\n"
            self.add_phrase(greetings)
            step = 2

        if step == 2:
            invitation = "Первая тройка игроков - в студию!\n"
            self.add_phrase(invitation)
            step = 3

        if step == 3:
            hello_player_1 = "Первый игрок, представьтесь\n"
            self.add_phrase(hello_player_1)
            self.add_name()

        if step == 4:
            hello_player_2 = "Второй игрок, представьтесь\n"
            self.add_phrase(hello_player_2)
            self.add_name()

        if step == 5:
            hello_player_3 = "Третий игрок, представьтесь\n"
            self.add_phrase(hello_player_3)
            self.add_name()

        if step == 6:
            global choosing_an_answer
            choosing_an_answer = "Скажите слово сразу или будете открывать буквы? (1 или 0)\n"
            show_question = "Внимание, вопрос!\n"
            self.add_phrase(show_question + self.random[0] + "\n" + "\n" + choosing_an_answer)
            self.show_question()



    def add_phrase(self, new_phrase):
        global dialogs
        self.ui.phrase.setText(dialogs + "\n" + str(new_phrase))
        dialogs = self.ui.phrase.text()

    def type_phrase(self):
        self.ui.next_button.clicked.connect(lambda: self.add_phrase(self.ui.type_phrase.text()))

    def add_name(self):
        self.ui.next_button.clicked.connect(lambda: define_name(self.ui.type_phrase.text()))

        def define_name(name):
            global player_1
            global player_2
            global player_3
            global players
            global step
            if step == 3 and name != "":
                player_1 = name
                self.add_phrase("Игрок №1:\n" + player_1 + "\n")
                name = ""
                self.ui.type_phrase.setText(name)
                if player_1 != "":
                    step = 4
                    self.show_dialogs()
            if step == 4 and name != "":
                player_2 = name
                self.add_phrase("Игрок №2:\n" + player_2 + "\n")
                name = ""
                self.ui.type_phrase.setText(name)
                if player_2 != "":
                    step = 5
                    self.show_dialogs()
            if step == 5 and name != "":
                player_3 = name
                self.add_phrase("Игрок №3:\n" + player_3 + "\n")
                players = (player_1, player_2, player_3)
                name = ""
                self.ui.type_phrase.setText(name)
                if player_3 != "":
                    step = 6
                    self.show_dialogs()

