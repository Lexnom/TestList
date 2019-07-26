import change_bd
import ButtonClick
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QDesktopWidget, QTableWidget, QTableWidgetItem


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    # Создание главной формы
    def initUI(self):

        self.createTable()

        self.btnAdd = QPushButton('Добваить', self)
        self.btnAdd.setToolTip('Добавить нового Клиента')
        self.btnAdd.move(10, 3)
        self.btnAdd.clicked.connect(self.clickAdd)

        self.btnSelect = QPushButton('Обновить', self)
        self.btnSelect.setToolTip('Обновить таблицу')
        self.btnSelect.move(95, 3)
        self.btnSelect.clicked.connect(self.updateTable)

        self.btnDlt = QPushButton('Удалить', self)
        self.btnDlt.setToolTip('Удалить Пользователя')
        self.btnDlt.move(180, 3)
        self.btnDlt.clicked.connect(self.delete)

        self.btnUpdate = QPushButton('Изменить', self)
        self.btnUpdate.setToolTip("Подтверждение изменения ячейки")
        self.btnUpdate.move(265, 3)
        self.btnUpdate.clicked.connect(self.update)

        self.setFixedSize(1090, 550)
        self.setWindowTitle('Manager')
        q = QDesktopWidget().availableGeometry()
        self.move(q.width()/4, q.height()/4)
        self.show()

    # Активация формы на добавление
    def clickAdd(self):

        self.ex = ButtonClick.add()
        self.ex.show()

    # Обновление таблицы
    def updateTable(self):
        self.Table.clear()
        self.incell()

    # Создание таблицы
    def createTable(self):

        self.Table = QTableWidget(self)
        self.Table.move(10, 30)
        self.Table.resize(1060, 500)

        self.incell()

    def incell(self):
        self.Table.setRowCount(change_bd.count())
        self.Table.setColumnCount(4)
        self.Table.setHorizontalHeaderLabels(('Имя', 'Фамилия', 'Телефон', 'Пол'))

        print('выполняю incell')
        result = change_bd.selct_table()
        rng = change_bd.count()
        j = 0
        for i in range(rng):
            for tmp in result:
                for cell in tmp:
                    self.Table.setItem(i, j, QTableWidgetItem(cell))
                    j = j + 1

    # Удаление из БД
    def delete(self):

        row = self.Table.currentIndex().row()
        print(row)
        result = change_bd.selct_table()
        rng = change_bd.count()
        for i in range(rng):
                if i == row:
                    print(result[i])
                    change_bd.delete_person(result[i])
                    break

    # Изменение информации в ячейках
    def update(self):
        row = self.Table.currentIndex().row()
        column = self.Table.currentIndex().column()
        print(row, column)
        rng = change_bd.count()
        result = change_bd.selct_table()
        for i in range(rng):
            if i == row:
                change_bd.update_cell(result[i], self.Table.item(row,column).text(), column)