import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Вычисление выражений')

        self.name_input = QLineEdit(self)
        self.name_input.resize(150, 29)
        self.name_input.move(10, 10)

        self.name_output = QLineEdit(self)
        self.name_output.resize(150, 29)
        self.name_output.move(190, 10)

        self.btn = QPushButton('->', self)
        self.btn.resize(29, 29)
        self.btn.move(160, 10)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.name_output.setText(str(eval(self.name_input.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())