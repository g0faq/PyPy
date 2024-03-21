import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Записная книжка.ui', self)

        self.Start.clicked.connect(self.run)

    def run(self):
        self.listWidget.addItem(f'{self.name.text()} {self.number.text()}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())