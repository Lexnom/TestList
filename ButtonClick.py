from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QDesktopWidget, QMessageBox
from PyQt5 import *

import change_bd
class add(QWidget):

    def __init__(self, parent = None    ):
        super().__init__()

        self.initUI()

    # Создание формы на добавление в БД
    def initUI(self):

        self.lblName = QLabel('Имя:', self)
        self.lblName.move(5, 10)

        self.NameEdit = QLineEdit(self)
        self.NameEdit.move(45, 10)

        self.lblLastN = QLabel("Фамилия:", self)
        self.lblLastN.move(5, 45)

        self.lName = QLineEdit(self)
        self.lName.move(80, 45)

        self.lblPhone = QLabel("Телефон:", self)
        self.lblPhone.move(5, 75)

        self.PhoneEdit = QLineEdit(self)
        self.PhoneEdit.move(75, 75)

        self.lblSex = QLabel("Пол:", self)
        self.lblSex.move(5, 105)

        self.SexEdit = QLineEdit(self)
        self.SexEdit.move(75, 105)

        self.BtnAdd = QPushButton("Добавить", self)
        self.BtnAdd.move(5, 135)
        self.BtnAdd.clicked.connect(self.insert)

        self.setFixedSize(250, 350)
        self.setWindowTitle("Добвать пользователя")
        q = QDesktopWidget().availableGeometry()
        self.move(q.width() / 4, q.height() / 4)
        self.show()

    # Отправка информации в бд
    def insert(self):

        change_bd.insert_person(self.NameEdit.text(), self.lName.text(), self.PhoneEdit.text(), self.SexEdit.text())
        QMessageBox.about(self, "Сообщение", "Пользователь успешно добавлен!")
        self.close()