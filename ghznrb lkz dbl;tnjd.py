import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Вычисление выражений')

        self.edit1 = QCheckBox(self)
        self.edit1.toggle()
        self.edit1.move(10, 10)
        self.edit1.stateChanged.connect(self.run)

        self.label_edit1 = QLabel(self)
        self.label_edit1.setText('edit1')
        self.label_edit1.move(30, 12)

        self.nume_edit1 = QLineEdit(self)
        self.nume_edit1.move(70, 10)

        self.edit2 = QCheckBox(self)
        self.edit2.toggle()
        self.edit2.move(10, 30)
        self.edit2.stateChanged.connect(self.run_2)

        self.label_edit2 = QLabel(self)
        self.label_edit2.setText('edit2')
        self.label_edit2.move(30, 32)

        self.nume_edit2 = QLineEdit(self)
        self.nume_edit2.move(70, 30)

        self.edit3 = QCheckBox(self)
        self.edit3.toggle()
        self.edit3.move(10, 50)
        self.edit3.stateChanged.connect(self.run_3)

        self.label_edit3 = QLabel(self)
        self.label_edit3.setText('edit3')
        self.label_edit3.move(30, 52)

        self.nume_edit3 = QLineEdit(self)
        self.nume_edit3.move(70, 50)

        self.edit4 = QCheckBox(self)
        self.edit4.toggle()
        self.edit4.move(10, 70)
        self.edit4.stateChanged.connect(self.run_4)

        self.label_edit = QLabel(self)
        self.label_edit.setText('edit4')
        self.label_edit.move(30, 72)

        self.nume_edit4 = QLineEdit(self)
        self.nume_edit4.move(70, 70)

    def run(self, s1):
         if s1:
             self.nume_edit1.show()
         else:
             self.nume_edit1.hide()

    def run_2(self, s1):
         if s1:
             self.nume_edit2.show()
         else:
             self.nume_edi2.hide()

    def run_3(self, s1):
         if s1:
             self.nume_edit3.show()
         else:
             self.nume_edit3.hide()

    def run_4(self, s1):
         if s1:
             self.nume_edit4.show()
         else:
             self.nume_edit4.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())