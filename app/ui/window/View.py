# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from app.ui.components.filelist.Component import Component as FileListComponent


class View(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(View, self).__init__()
        self.setObjectName('main-window')
        self._init_window()
        self._init_content()

    def _init_window(self) -> None:
        self.setFixedSize(400, 500)
        self.setWindowTitle('Data Visualizer')

    def _init_content(self) -> None:
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setObjectName('layout')
        main_layout.addWidget(FileListComponent('file-list')())
