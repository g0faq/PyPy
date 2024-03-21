import sqlite3
import sys
import csv

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from random import randint


con = sqlite3.connect('Bulls_and_cows.sqlite')
cur = con.cursor()


class Bull_Cow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('интерфейс быки и коровы.ui', self)

        self.WinLose.setText('       ')

        self.go.clicked.connect(self.run)

        self.pc_number = str(randint(100, 999))

        self.pk.setText(str(randint(100, 999)))


    def run(self):
        i = self.tableWidget.rowCount()
        row = (self.pk.text(), self.Bull.text(), self.Cows.text())
        for j, elem in enumerate(row):
            self.tableWidget.setItem(i - 1, j, QTableWidgetItem(elem))
        self.tableWidget.setRowCount(i + 1)

        my_number = self.player.text()
        count_bulls = 0
        count_cows = 0
        for elem in range(3):
            if self.pc_number[elem] == my_number[elem]:
                count_bulls += 1
            elif my_number[elem] in self.pc_number:
                count_cows += 1
        if count_bulls == 3:
            self.WinLose.setText('WIN')
        elif self.Bull.text() == '3':
            self.WinLose.setText('LOSE')


        i2 = self.tableWidget_2.rowCount()
        if len(my_number) != 3:
            row = (self.player.text(), str('ERROR'), str('ERROR'))
            for j2, elem in enumerate(row):
                self.tableWidget_2.setItem(i2 - 1, j2, QTableWidgetItem(elem))
        elif str(my_number)[0] == str(my_number)[1] or\
            str(my_number)[0] == str(my_number)[2] or\
                str(my_number)[1] == str(my_number)[2]:
            row = (self.player.text(), str('ERROR'), str('ERROR'))
            for j2, elem in enumerate(row):
                self.tableWidget_2.setItem(i2 - 1, j2, QTableWidgetItem(elem))
        else:
            row = (self.player.text(), str(count_bulls), str(count_cows))
        for j2, elem in enumerate(row):
            self.tableWidget_2.setItem(i2 - 1, j2, QTableWidgetItem(elem))
        self.tableWidget_2.setRowCount(i2 + 1)
        self.pk.setText(str(randint(100, 999)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Bull_Cow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
    con.close()