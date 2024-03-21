import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class AWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mc.ui", self) # Загружаем дизайн

        self.btn.clicked.connect(self.f)

    def f(self):
        pass
        '''ans = ''
        if self.c3.isChecked():
            ans += 'картошка фри' + '\n'
        if self.c4.isChecked():
            ans += 'нагетсы' + '\n'
        if self.c2.isChecked():
            ans += 'чизбургер' + '\n'
        if self.c1.isChecked():
            ans += 'кока_кола' + '\n'
        self.text.setPlainText(ans)'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AWidget()
    ex.show()
    sys.exit(app.exec())