import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Текстовый флаг.ui', self)

        self.sp = ['', '', '']
        self.Start.clicked.connect(self.run)

    def run(self):
        if self.color_1_1.isChecked:
            self.sp[0] = 'белый'
        if self.color_1_2.isChecked:
            self.sp[0] = 'синий'
        if self.color_1_3.isChecked:
            self.sp[0] = 'красный'
        if self.color_2_1.isChecked:
            self.sp[1] = 'белый'
        if self.color_2_2.isChecked:
            self.sp[1] = 'синий'
        if self.color_2_3.isChecked:
            self.sp[1] = 'красный'
        if self.color_3_1.isChecked:
            self.sp[2] = 'белый'
        if self.color_3_2.isChecked:
            self.sp[2] = 'синий'
        if self.color_3_3.isChecked:
            self.sp[2] = 'красный'

        self.label_otvet.setText(f'Цвета: {self.sp[0]}, {self.sp[1]}, {self.sp[2]}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())