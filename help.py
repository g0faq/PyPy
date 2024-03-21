import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QSpinBox, QTableWidget


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


pprint(dir(QTableWidget))
sys.excepthook = except_hook
