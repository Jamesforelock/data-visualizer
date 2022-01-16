# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from app.lib.chart.Chart import Chart
from app.lib.chart.ChartServiceException import ChartServiceException
from app.lib.file.FileService import FileService
from app.lib.chart.ChartService import ChartService
from app.ui.components.chartgenerator.ChartGeneratorView import ChartGeneratorView
from app.ui.components.dialogbox.DialogBoxComponent import DialogBoxComponent


class ChartGeneratorComponent:
    def __init__(self, object_name: str) -> None:
        self.view = ChartGeneratorView(object_name)
        self.selected_type = 'P'
        self.selected_file_name = ''
        self._register_event_handlers()

    def __call__(self) -> QtWidgets.QWidget:
        return self.view

    def _register_event_handlers(self):
        radiobuttons = self.view.findChildren(QtWidgets.QRadioButton)
        for button in radiobuttons:
            button.toggled.connect(lambda: self._set_selected_type())
        width = self.view.findChild(QtWidgets.QLineEdit, 'width')
        width.textChanged.connect(self._set_min_size)
        height = self.view.findChild(QtWidgets.QLineEdit, 'height')
        height.textChanged.connect(self._set_min_size)

        visualize_button = self.view.findChild(QtWidgets.QPushButton, 'visualize_button')
        visualize_button.clicked.connect(self._visualize)
        self.view.selected_file_name_changed.connect(self._set_selected_file_name)

    def _set_min_size(self) -> None:
        try:
            size = int(self.view.sender().text())
            if size > 0:
                return
            self.view.sender().setText('1')
        except ValueError:
            self.view.sender().setText('1')

    def _set_selected_type(self) -> None:
        radiobutton = self.view.sender()
        if radiobutton.isChecked():
            self.selected_type = radiobutton.type

    def _set_selected_file_name(self, file_name) -> None:
        self.selected_file_name = file_name

    def _visualize(self) -> None:
        chart_type = self.selected_type
        name = self.view.findChild(QtWidgets.QLineEdit, 'name').text().strip()
        if not name:
            DialogBoxComponent('Ошибка', 'Отображаемый график должен иметь название', 'error')()
            return

        width = int(self.view.findChild(QtWidgets.QLineEdit, 'width').text())
        height = int(self.view.findChild(QtWidgets.QLineEdit, 'height').text())

        file_name = self.selected_file_name
        if not file_name:
            DialogBoxComponent('Ошибка', 'Для отображения графика необходимо выбрать файл с данными', 'error')()
            return

        data = FileService.get_data(file_name)

        chart = Chart(chart_type, data, [width, height], name)
        try:
            ChartService.visualize_chart(chart)
        except ChartServiceException as e:
            DialogBoxComponent('Ошибка', str(e), 'error')()
