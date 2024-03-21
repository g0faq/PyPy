import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Антиплагиат v0.0001.ui', self)

        self.sum = 0
        self.count = 0

        self.Start.clicked.connect(self.run)

    def run(self):
        text_1 = self.textEdit.toPlainText()
        text_2 = self.textEdit_2.toPlainText()
        sp_text_1 = text_1.split('\n')
        sp_text_2 = text_2.split('\n')
        self.sum = 0
        self.count = 0
        if sp_text_1 > sp_text_2:
            for i in range(len(sp_text_1) - len(sp_text_2)):
                sp_text_2.append('')
        elif sp_text_2 > sp_text_1:
            for i in range(len(sp_text_2) - len(sp_text_1)):
                sp_text_1.append('')
        for i in range(len(sp_text_1)):
            if sp_text_1[i] == sp_text_2[i]:
                self.count += 1
        self.sum = 100 / len(sp_text_1) * self.count
        self.label_4.setText(f'код похож на {self.sum}%')
        m = self.doubleSpinBox.value()
        if m <= self.sum:
            self.label_5.setText('!ПЛАГИАТ!')
        else:
            self.label_5.setText('Не плагиат')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


