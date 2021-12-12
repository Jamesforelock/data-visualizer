# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from app.ui.components.filelist.FileListComponent import FileListComponent
from app.ui.components.chartgenerator.ChartGeneratorComponent import ChartGeneratorComponent


class View(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(View, self).__init__()
        self.setObjectName('main_window')
        self._init_window()
        self._init_content()

    def _init_window(self) -> None:
        self.setFixedSize(600, 350)
        self.setWindowTitle('Data Visualizer')

    def _init_content(self) -> None:
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setObjectName('layout')
        main_layout.addWidget(FileListComponent('file_list')())
        main_layout.addWidget(ChartGeneratorComponent('chart_generator')())
