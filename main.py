from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow
from Menu import MainMenu
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QApplication([])
    window = MainMenu()
    window.show()
    app.exec_()
