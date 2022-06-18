from data_base import word_list
from main_widget import Ui_Form
# from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow
from random import *
# import time
import Baraban

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
    return [hidden_question, hidden_word]


# def split(hidden_word):
# letters_list = [char for char in hidden_word]  # Массив букв
# print("Массив букв:", letters_list)
# total = len(letters_list)  # Кол-во букв в слове
# print("Кол-во букв в слове:", total)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
            letter = hidden_word[i]
            new_letter_box.setObjectName(letter)
            new_letter_box.setText('')
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
            show_question = "Внимание, вопрос!\n"
            self.add_phrase(show_question + self.random[0] + "\n")
            self.show_question()
            start_game = "Вращайте барабан!"
            self.add_phrase(start_game)
            self.ui.next_button.clicked.connect(lambda: self.start_game())

    def add_phrase(self, new_phrase):
        global dialogs
        self.ui.phrase.setText(dialogs + "\n" + new_phrase)
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

    def start_game(self):
        global number
        global winner
        global win

        while True:
            for turn in players:
                if turn == players[0]:
                    number = 0
                elif turn == players[1]:
                    number = 1
                elif turn == players[2]:
                    number = 2
                winner = turn
                # time.sleep(1)

                players_turn = str(turn) + ", ваш ход!"
                self.add_phrase(players_turn)

                # print("Скажите слово сразу или будете открывать буквы? (1 или 0)")
                question_1 = "Скажите слово сразу или будете угадывать по буквам? (1 или 0)"
                self.add_phrase(question_1)

                # answer = input()

                # if answer == '1':
                #     print('Итак слово...')
                #     answer = input()
                #     if answer == self.random[1]:
                #         print('И...')
                #         # time.sleep(3)
                #         print('...перед нами победитель!')
                #         # time.sleep(2)
                #         if points[number] == 0:
                #             print(turn, ', Вам присваивается 100000 очков')
                #             points[number] = 100000
                #         else:
                #             print(turn, ', Ваши очки умножены на 10')
                #             points[number] *= 10
                #         win = 1
                #         break
                #     else:
                #         print('И...')
                #         # time.sleep(3)
                #         print('...это неправильный ответ!')
                #         # time.sleep(2)
                #         print('Ход переходит к следующему игроку')
                #         # time.sleep(1)
                #         continue
                # elif answer == '0':
                #     # while True:
                #     #     print('Итак буква..')
                #     #     answer = input()
                #     #     for ltr in self.random[1]:
                #     #         if answer == ltr:
                #     #             print('Откройте букву', answer)
                #     #             ug = 1
                #     #             # for Let in Word:
                #     #             #     if answer == Let:
                #     #             #         Id = Word.index(answer)
                #     #             #         Word_clean[Id] = Word[Id]
                #     #             #         Word[Id] = ''
                #     #             # open()
                #     #     # if Word_clean.count('') == 0:
                #     #     #     time.sleep(1)
                #     #     #     print('И перед нами победитель!')
                #     #     #     time.sleep(1)
                #     #     #     print(turn, ', Ваши очки умножены на 10')
                #     #     #     points[number] *= 10
                #     #     #     time.sleep(1)
                #     #     #     win = 1
                #     #     #     break
                #     #     if ug == 1:
                #     #         print('Вы правильно угадали букву')
                #     #         ug = 0
                #     #         print('Назовите ещё букву')
                #     #     elif ug == 0:
                #     #         print('Такой буквы нет')
                #     #         break
                #     if win == 1:
                #         break
                #     else:
                #         print('Ход переходит к следующему игроку')
                #         # time.sleep(1)
                #         continue

            if win == 1:
                # print("Победитель: ", winner)
                victory = "Победитель: " + winner
                self.add_phrase(victory)
                break


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

# Question = randint(0, len(word_list) - 1)
# word = word_list[Question]
# print(word)
# Word = []
# for letter in word[0]:
#     Word.append(letter)
#     # print(letter)
#     # Word = ['и', 'н', 'ф', 'л', 'я', 'ц', 'и', 'я']
# Word_clean = []
# for i in range(len(Word)):
#     Word_clean.append('')
#     # Word_clean = ['', '', '', '', '', '', '', '']
# # Якубович:
# print(
#     'Добрый вечер, здравствуйте, уважаемые дамы и господа! В эфире капитал-шоу Поле чудес!')
# time.sleep(2)
# print('Первая тройка игроков в студию!')
# time.sleep(2)
# print('Первый игрок, представьтесь')
# Player_1 = input()
# print('Здравствуйте,', Player_1)
# time.sleep(2)
# print('Второй игрок, представьтесь')
# Player_2 = input()
# print('Здравствуйте,', Player_2)
# time.sleep(2)
# print('Третий игрок, представьтесь')
# Player_3 = input()
# print('Здравствуйте,', Player_3)
# Players = (Player_1, Player_2, Player_3)
# Points = [0, 0, 0]
# Presents = [[], [], []]
# win = 0
# winner = ''
# number = 0
#
#
# class Questions:
#     pass


# while True:
#     for turn in players:
#         if turn == players[0]:
#             number = 0
#         elif turn == players[1]:
#             number = 1
#         elif turn == players[2]:
#             number = 2
#         winner = turn
#         time.sleep(1)
#         print('Внимание вопрос!')
#         print(word[1])
#         time.sleep(2)
#         print(turn, ', ваш ход', sep='')
#         print("Скажите слово сразу или будете открывать буквы? (1 или 0)")
#         Choice = input()
#         if Choice == '1':
#             print('Итак слово...')
#             Choice = input()
#             if Choice == word[0]:
#                 print('И...')
#                 time.sleep(3)
#                 print('...перед нами победитель!')
#                 time.sleep(2)
#                 if Points[number] == 0:
#                     print(turn, ', Вам присваивается 100000 очков')
#                     Points[number] = 100000
#                 else:
#                     print(turn, ', Ваши очки умножены на 10')
#                     Points[number] *= 10
#                 win = 1
#                 break
#             else:
#                 print('И...')
#                 time.sleep(3)
#                 print('...это неправильный ответ!')
#                 time.sleep(2)
#                 print('Ход переходит к следующему игроку')
#                 time.sleep(1)
#                 continue
#         elif Choice == '0':
#             while True:
#                 print('Итак буква..')
#                 Choice = input()
#                 for ltr in Word:
#                     if Choice == ltr:
#                         print('Откройте букву', Choice)
#                         ug = 1
#                         for Let in Word:
#                             if Choice == Let:
#                                 Id = Word.index(Choice)
#                                 Word_clean[Id] = Word[Id]
#                                 Word[Id] = ''
#                         open()
#                 if Word_clean.count('') == 0:
#                     time.sleep(1)
#                     print('И перед нами победитель!')
#                     time.sleep(1)
#                     print(turn, ', Ваши очки умножены на 10')
#                     Points[number] *= 10
#                     time.sleep(1)
#                     win = 1
#                     break
#                 if ug == 1:
#                     print('Вы правильно угадали букву')
#                     ug = 0
#                     print('Назовите ещё букву')
#
#                 elif ug == 0:
#                     print('Такой буквы нет')
#                     break
#             if win == 1:
#                 break
#             else:
#                 print('Ход переходит к следующему игроку')
#                 continue
#     if win == 1:
#         break
# time.sleep(1)
# print('Победитель сегодняшней игры', winner, '\n', 'он уходит с', Points[number], 'очков')
# if len(Presents[2]) != 0:
#     print('А также с', end='')
#     for i in Presents[3]:
#         print(i)
# time.sleep(3)
# print('До новых встреч, уважаемые дамы и господа, в эфире было капитал-шоу Поле чудес')
# time.sleep(20)
