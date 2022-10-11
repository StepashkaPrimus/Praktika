import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from MainWindow import MainWindow

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setWindowTitle('Поле_Чудес')
        self.setFixedSize(400, 300)
        self.central_widget = QtWidgets.QWidget()
        self.window = None
        self.rules = None
        self.setCentralWidget(self.central_widget)
        self.buttons_layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.buttons_layout)
        self.start_game_button = QtWidgets.QPushButton()
        self.start_game_button.setText('Начать игру')
        self.start_game_button.clicked.connect(self.start_game)
        self.rules_button = QtWidgets.QPushButton()
        self.rules_button.setText('Правила игры')
        self.rules_button.clicked.connect(self.show_rules)
        self.exit_button = QtWidgets.QPushButton()
        self.exit_button.setText('Выход')
        self.exit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.buttons_layout.addWidget(self.start_game_button)
        self.buttons_layout.addWidget(self.rules_button)
        self.buttons_layout.addWidget(self.exit_button)

    def start_game(self):
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def show_rules(self):
        self.rules = RulesDialog()
        self.hide()
        self.rules.exec_()
        self.show()


class RulesDialog(QtWidgets.QDialog):

    def __init__(self):
        super(RulesDialog, self).__init__()
        self.setWindowTitle('Правила')
        self.widget = QtWidgets.QLabel(self)
        self.widget.setStyleSheet('''color:black;''')
        self.widget.setText('''        
    Игра начинается с того, что ведущий объявляет вопрос по которому необходимо найти ответ для победы в игре. 
    Необходимо отгадавать слово, ответ на который скрыт за квадратами на табло. 
    Под каждым квадратом содержится одна буква, поэтому игроки знают длину слова.
    Цель игры — угадать слово быстрее, чем его соперники.
    После каждого удачного хода игроку предлагается,назвать слово целиком, 
    а в случае неверно названной буквы ход переходит к следующему игроку. 
    Если слово названо верно, 
    то игрок становится победителем тура и проходит в финал, иначе он покидает игру, 
    а право хода переходит к следующему игроку.
    Слово может быть открыто буква за буквой и называнием по одной букве за ход. 
    В этом случае победителем тура/финала становится игрок, открывший последнюю букву.
    Игра заканчивается, если:
    игрок неверно назвал слово, которое было зашифровано;
    если игрок выиграл.
''')
        back_button = QtWidgets.QPushButton("Назад", self)
        back_button.setToolTip("Вернуться в главное меню")
        back_button.setFocusPolicy(QtCore.Qt.NoFocus)
        back_button.clicked.connect(self.close)
        back_button.move(350, 250)
        self.setFixedSize(600, 300)

