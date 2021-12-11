# @author Denis Chuprynin <denischuprynin@gmail.com>


import sys
from PyQt5 import QtWidgets
from app.ui.window.View import View


class Window:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.view = View()

    def __call__(self) -> None:
        self.view.show()
        self.app.exec()
