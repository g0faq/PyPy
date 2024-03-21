import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


# Отнаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 400, 100)
        # А также его заголовок
        self.setWindowTitle('Фокус со словами')

        # Создаем кнопку.
        # Передаем 2 параметра:
        # надпись и виджет, на котором будет размещена кнопка
        self.btn = QPushButton('->', self)
        # Изменяем рамер кнопки. Теперь он 100 на 100 пикселей
        self.btn.resize(30, 30)
        # Размещаем кпопку на родительском виджете
        # по координатам (100, 100)
        self.btn.move(180, 45)
        self.btn.clicked.connect(self.fokus)

        self.name_input_left = QLineEdit(self)
        self.name_input_left.move(10, 50)

        self.name_input_right = QLineEdit(self)
        self.name_input_right.move(250, 50)

    def fokus(self):
        


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())