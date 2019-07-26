import sys

from UIMain import Example
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())