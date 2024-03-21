import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Миникалькулятор')

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(150, 30)
        self.name_input1.move(10, 50)
        self.label_1 = QLabel(self)
        self.label_1.setText('Первое число:')
        self.label_1.move(10, 30)

        self.name_input2 = QLineEdit(self)
        self.name_input2.resize(150, 30)
        self.name_input2.move(10, 120)
        self.label_2 = QLabel(self)
        self.label_2.setText('Второе число:')
        self.label_2.move(10, 100)

        self.btn = QPushButton('->', self)
        self.btn.resize(30, 30)
        self.btn.move(200, 85)
        self.btn.clicked.connect(self.run)

        self.label_plus = QLabel(self)
        self.label_plus.setText('сумма:')
        self.label_plus.move(300, 25)

        self.label_minus = QLabel(self)
        self.label_minus.setText('разность:')
        self.label_minus.move(300, 75)

        self.label_umn = QLabel(self)
        self.label_umn.setText('произведение:')
        self.label_umn.move(300, 125)

        self.label_del = QLabel(self)
        self.label_del.setText('частное:')
        self.label_del.move(300, 175)

        self.LCD_plus = QLCDNumber(self)
        self.LCD_plus.move(400, 25)

        self.LCD_minus = QLCDNumber(self)
        self.LCD_minus.move(400, 75)

        self.LCD_umn = QLCDNumber(self)
        self.LCD_umn.move(400, 125)

        self.LCD_del = QLCDNumber(self)
        self.LCD_del.move(400, 175)

    def run(self):
        self.LCD_plus.display(int(self.name_input1.text()) + int(self.name_input2.text()))
        self.LCD_minus.display(int(self.name_input1.text()) - int(self.name_input2.text()))
        self.LCD_umn.display(int(self.name_input1.text()) * int(self.name_input2.text()))
        if self.name_input2.text() == '0':
            self.LCD_del.display('Error')
        else:
            self.LCD_del.display(int(self.name_input1.text()) // int(self.name_input2.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())