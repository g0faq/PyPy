import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import choice


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Случайная строка из файла — 2.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open("lines.txt", encoding='utf-8') as file:
            data = file.readlines()
        if data:
            self.textEdit.setText(choice(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())