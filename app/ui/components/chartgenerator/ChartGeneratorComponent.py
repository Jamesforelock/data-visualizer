# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from app.lib.chart.Chart import Chart
from app.lib.chart.ChartServiceException import ChartServiceException
from app.lib.chart.Surface import Surface
from app.lib.chart.SurfaceService import SurfaceService
from app.lib.chart.SurfaceServiceException import SurfaceServiceException
from app.lib.file.FileService import FileService
from app.lib.chart.ChartService import ChartService
from app.ui.components.chartgenerator.ChartGeneratorView import ChartGeneratorView
from app.ui.components.dialogbox.DialogBoxComponent import DialogBoxComponent


class ChartGeneratorComponent:
    def __init__(self, object_name: str) -> None:
        self.view = ChartGeneratorView(object_name)
        self.selected_type = ChartService.DOT_CHART_TYPE
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
            self.view.is_selected_surface_type.emit(self._is_selected_surface_type())
            self._toggle_surface_params()

    def _is_selected_surface_type(self) -> bool:
        if self.selected_type == SurfaceService.WIREFRAME_TYPE \
                or self.selected_type == SurfaceService.SURFACE_TYPE:
            return True
        return False

    def _toggle_surface_params(self) -> None:
        x_section = self.view.findChild(QtWidgets.QLineEdit, 'x_section')
        y_section = self.view.findChild(QtWidgets.QLineEdit, 'y_section')
        points_number = self.view.findChild(QtWidgets.QLineEdit, 'points_number')
        z_function = self.view.findChild(QtWidgets.QLineEdit, 'z_function')
        if self._is_selected_surface_type():
            x_section.show()
            y_section.show()
            points_number.show()
            z_function.show()
            return

        x_section.hide()
        y_section.hide()
        points_number.hide()
        z_function.hide()

    def _set_selected_file_name(self, file_name) -> None:
        self.selected_file_name = file_name

    def _visualize(self) -> None:
        name = self.view.findChild(QtWidgets.QLineEdit, 'name').text().strip()
        if not name:
            DialogBoxComponent('Ошибка', 'Отображаемый график должен иметь название', 'error')()
            return

        width = int(self.view.findChild(QtWidgets.QLineEdit, 'width').text())
        height = int(self.view.findChild(QtWidgets.QLineEdit, 'height').text())

        if self._is_selected_surface_type():
            self._visualize_surface(width, height, name)
            return

        self._visualize_chart(width, height, name)

    def _visualize_chart(self, width: int, height: int, name: str) -> None:
        file_name = self.selected_file_name
        if not file_name:
            DialogBoxComponent('Ошибка', 'Для отображения графика необходимо выбрать файл с данными', 'error')()
            return

        data = FileService.get_data(file_name)

        chart = Chart(self.selected_type, data, [width, height], name)
        try:
            ChartService.visualize_chart(chart)
        except ChartServiceException as e:
            DialogBoxComponent('Ошибка', str(e), 'error')()

    def _visualize_surface(self, width: int, height: int, name: str) -> None:
        x_section = self.view.findChild(QtWidgets.QLineEdit, 'x_section').text().strip()
        y_section = self.view.findChild(QtWidgets.QLineEdit, 'y_section').text().strip()
        points_number = self.view.findChild(QtWidgets.QLineEdit, 'points_number').text().strip()
        z_function = self.view.findChild(QtWidgets.QLineEdit, 'z_function').text().strip()
        if '' in [x_section, y_section, points_number, z_function]:
            DialogBoxComponent('Ошибка',
                               'Для отображения поверхности необходимо указать отрезки x и y, количество точек и функцию z-значений',
                               'error')()
            return

        try:
            x_section = list(map(int, x_section.split(',')))
            y_section = list(map(int, y_section.split(',')))
        except ValueError:
            DialogBoxComponent('Ошибка', 'Некорректное значение отрезка', 'error')()
            return

        surface = Surface(self.selected_type, [width, height], name, x_section, y_section, int(points_number),
                          z_function)
        try:
            SurfaceService.visualize_surface(surface)
        except SurfaceServiceException as e:
            DialogBoxComponent('Ошибка', str(e), 'error')()
