import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Арифмометр')

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(58, 29)
        self.name_input1.move(10, 10)

        self.name_input2 = QLineEdit(self)
        self.name_input2.resize(58, 29)
        self.name_input2.move(160, 10)

        self.name_output = QLineEdit(self)
        self.name_output.resize(58, 29)
        self.name_output.move(230, 10)

        self.btn_plus = QPushButton('+', self)
        self.btn_plus.resize(29, 29)
        self.btn_plus.move(70, 10)
        self.btn_plus.clicked.connect(self.run)

        self.btn_minus = QPushButton('-', self)
        self.btn_minus.resize(29, 29)
        self.btn_minus.move(100, 10)
        self.btn_minus.clicked.connect(self.run)

        self.btn_mult = QPushButton('*', self)
        self.btn_mult.resize(29, 29)
        self.btn_mult.move(130, 10)
        self.btn_mult.clicked.connect(self.run)

        self.label = QLabel(self)
        self.label.setText("=")
        self.label.move(220, 17.5)

    def run(self):
        a = int(self.name_input1.text())
        b = int(self.name_input2.text())
        self.name_output.setText(str(eval(f'{a} {self.sender().text()} {b}')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())