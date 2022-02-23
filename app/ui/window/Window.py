# @author Denis Chuprynin <denischuprynin@gmail.com>


import sys
from PyQt5 import QtWidgets
from app.ui.window.View import View
from app.ui.components.filelist.FileListView import FileListView
from app.ui.components.chartgenerator.ChartGeneratorView import ChartGeneratorView


class Window:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.view = View()
        self._register_event_handlers()

    def __call__(self) -> None:
        self.view.show()
        self.app.exec()

    def _register_event_handlers(self):
        file_list = self.view.findChild(FileListView, 'file_list')
        file_list.selected_file_name_changed.connect(self._set_selected_file_name)
        chart_generator = self.view.findChild(ChartGeneratorView, 'chart_generator')
        chart_generator.is_selected_surface_type.connect(self._toggle_file_list)

    def _set_selected_file_name(self, file_name: str) -> None:
        chart_generator = self.view.findChild(ChartGeneratorView, 'chart_generator')
        chart_generator.selected_file_name_changed.emit(file_name)

    def _toggle_file_list(self, is_selected_surface_type: bool) -> None:
        file_list = self.view.findChild(FileListView, 'file_list')
        if is_selected_surface_type:
            file_list.hide()
            self.view.setFixedHeight(420)
            return
        file_list.show()
        self.view.setFixedHeight(480)
