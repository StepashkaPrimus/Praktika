from random import randint
from Words import word_list
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QMainWindow
from letter import Ui_Form
from random import *
import time

hidden_word = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        global hidden_word
        self.args = random()
        self.show_word()
        self.show_question()

    def show_word(self):
        hidden_word  = self.args[0]
        for i in range(len(hidden_word)):
            new_letter_box = QTextEdit()
            new_letter_box.setReadOnly(True)
            letter = hidden_word[i]
            new_letter_box.setObjectName(letter)
            new_letter_box.setText('')
            self.ui.horizontalLayout.addWidget(new_letter_box)
        print(self.ui.horizontalLayout.itemAt(0).widget().toPlainText())

    def show_question(self):
        question = self.args[1]
        self.ui.question_field.setText(question)

def random():
    global hidden_word
    total_lines = len(word_list)  # Подсчет кол-ва строк в файле Words.py
    random_line = randint(1, total_lines)  # Случайный выбор строки
    hidden_word = word_list[random_line - 1][0]  # Загаданное слово
    hidden_question = word_list[random_line - 1][1]  # Загаданный вопрос
    print("Загаданное слово:", hidden_word)
    print("Внимание вопрос!", hidden_question)
    return [hidden_word, hidden_question]


def split(hidden_word):
    letters_list = [char for char in hidden_word]  # Массив букв
    print("Массив букв:", letters_list)
    total = len(letters_list)  # Кол-во букв в слове
    print("Кол-во букв в слове:", total)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

Question = randint(0, len(word_list) - 1)
word = word_list[Question]
print(word)
Word = []
for letter in word[0]:
    Word.append(letter)
    # print(letter)
    # Word = ['и', 'н', 'ф', 'л', 'я', 'ц', 'и', 'я']
Word_clean = []
for i in range(len(Word)):
    Word_clean.append('')
    # Word_clean = ['', '', '', '', '', '', '', '']
# Якубович:
print(
    'Добрый вечер, здравствуйте, уважаемые дамы и господа! В эфире капитал-шоу Поле чудес! И с вами его ведущий Леонид Якубович!')
time.sleep(2)
print('Первая тройка игроков в студию!')
time.sleep(2)
print('Первый игрок, представьтесь')
Player_1 = input()
print('Здравствуйте,', Player_1)
time.sleep(2)
print('Второй игрок, представьтесь')
Player_2 = input()
print('Здравствуйте,', Player_2)
time.sleep(2)
print('Третий игрок, представьтесь')
Player_3 = input()
print('Здравствуйте,', Player_3)
Players = (Player_1, Player_2, Player_3)
Points = [0, 0, 0]
Presents = [[], [], []]
win = 0
winner = ''
number = 0


class Questions:
    pass


while True:
    for hod in Players:
        if hod == Players[0]:
            number = 0
        elif hod == Players[1]:
            number = 1
        elif hod == Players[2]:
            number = 2
        winner = hod
        time.sleep(1)
        print('Внимание вопрос!')
        print(word[1])
        time.sleep(2)
        print(hod, ', ваш ход', sep='')
        print("Скажите слово сразу или будете открывать буквы? (1 или 0)")
        Choice = input()
        if Choice == '1':
            print('Итак слово...')
            Choice = input()
            if Choice == word[0]:
                print('И...')
                time.sleep(3)
                print('...перед нами победитель!')
                time.sleep(2)
                if Points[number] == 0:
                    print(hod, ', Вам присваивается 100000 очков')
                    Points[number] = 100000
                else:
                    print(hod, ', Ваши очки умножены на 10')
                    Points[number] *= 10
                win = 1
                break
            else:
                print('И...')
                time.sleep(3)
                print('...это неправильный ответ!')
                time.sleep(2)
                print('Ход переходит к следующему игроку')
                time.sleep(1)
                continue
        elif Choice == '0':
            while True:
                print('Итак буква..')
                Choice = input()
                for ltr in Word:
                    if Choice == ltr:
                        print('Откройте букву', Choice)
                        ug = 1
                        for Let in Word:
                            if Choice == Let:
                                Id = Word.index(Choice)
                                Word_clean[Id] = Word[Id]
                                Word[Id] = ''
                        open()
                if Word_clean.count('') == 0:
                    time.sleep(1)
                    print('И перед нами победитель!')
                    time.sleep(1)
                    print(hod, ', Ваши очки умножены на 10')
                    Points[number] *= 10
                    time.sleep(1)
                    win = 1
                    break
                if ug == 1:
                    print('Вы правильно угадали букву')
                    ug = 0
                    print('Назовите ещё букву')

                elif ug == 0:
                    print('Такой буквы нет')
                    break
            if win == 1:
                break
            else:
                print('Ход переходит к следующему игроку')
                continue
    if win == 1:
        break
time.sleep(1)
print('Победитель сегодняшней игры', winner, '\n', 'он уходит с', Points[number], 'очков')
if len(Presents[2]) != 0:
    print('А также с', end='')
    for i in Presents[3]:
        print(i)
time.sleep(3)
print('До новых встреч, уважаемые дамы и господа, в эфире было капитал-шоу Поле чудес')
time.sleep(20)
