import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Файловая статистика.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        name_file = self.lineEdit.text()
        try:
            with open(name_file, 'r', encoding='utf8') as file:
                read_data = file.read()
                numbers = [int(x) for x in read_data.split()]
                self.maxzn.setValue(max(numbers))
                self.minzn.setValue(min(numbers))
                self.midzn.setText(sum(numbers) / len(numbers))
        except FileNotFoundError:
            self.statusBar().showMessage(f'Файл {name_file} не найден')
        except ValueError:
            self.statusBar().showMessage(f'В файле {name_file} содержатся некоректные данные')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())