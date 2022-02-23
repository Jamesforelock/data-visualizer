# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIntValidator, QFont
from app.lib.chart.ChartService import ChartService
from app.lib.chart.SurfaceService import SurfaceService


class ChartGeneratorView(QtWidgets.QWidget):
    selected_file_name_changed = pyqtSignal(str)
    is_selected_surface_type = pyqtSignal(bool)

    def __init__(self, object_name: str) -> None:
        super(ChartGeneratorView, self).__init__()
        self.setObjectName(object_name)
        self._init_content()

    def _init_content(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self._get_chart_type_widget())
        layout.setAlignment(Qt.AlignTop)
        column = QtWidgets.QWidget()
        column_layout = QtWidgets.QVBoxLayout()
        column_layout.setAlignment(Qt.AlignTop)
        column_layout.addWidget(self._get_chart_settings_widget())
        visualize_button = QtWidgets.QPushButton('Визуализировать')
        visualize_button.setObjectName('visualize_button')
        visualize_button.setMinimumHeight(35)
        column_layout.addWidget(visualize_button)
        column.setLayout(column_layout)
        layout.addWidget(column)

    @staticmethod
    def _get_chart_type_widget() -> QtWidgets.QWidget:
        chart_type = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        label = QtWidgets.QLabel('Тип графика')
        layout.addWidget(label)

        radiobuttons = {
            ChartService.DOT_CHART_TYPE: 'Точечный график',
            ChartService.LINE_CHART_TYPE: 'Линейный график',
            ChartService.BAR_CHART_TYPE: 'Столбчатая диаграмма',
            ChartService.PIE_CHART_TYPE: 'Круговая диаграмма',
            ChartService.DOT_CHART_3D_TYPE: 'Точечный 3D-график',
            ChartService.LINE_CHART_3D_TYPE: 'Линейный 3D-график',
            SurfaceService.WIREFRAME_TYPE: 'Каркасная поверхность',
            SurfaceService.SURFACE_TYPE: 'Поверхность',
        }

        for radiobutton_type, name in radiobuttons.items():
            radiobutton = QtWidgets.QRadioButton(name)
            radiobutton.type = radiobutton_type
            radiobutton.setFont(QFont('Arial', 11))
            if radiobutton.type == ChartService.DOT_CHART_TYPE:
                radiobutton.setChecked(True)
            layout.addWidget(radiobutton)

        chart_type.setLayout(layout)

        return chart_type

    @staticmethod
    def _get_chart_settings_widget() -> QtWidgets.QWidget:
        chart_setttings = QtWidgets.QWidget()
        chart_setttings_layout = QtWidgets.QVBoxLayout()
        chart_setttings_layout.setContentsMargins(0, 0, 0, 0)

        x_section = QtWidgets.QLineEdit()
        x_section.setObjectName('x_section')
        x_section.setFixedHeight(30)
        x_section.setPlaceholderText('Отрезок x (указывать через запятую)')
        x_section.hide()
        chart_setttings_layout.addWidget(x_section)

        y_section = QtWidgets.QLineEdit()
        y_section.setObjectName('y_section')
        y_section.setFixedHeight(30)
        y_section.setPlaceholderText('Отрезок y (указывать через запятую)')
        y_section.hide()
        chart_setttings_layout.addWidget(y_section)

        points_number = QtWidgets.QLineEdit()
        points_number.setObjectName('points_number')
        points_number.setFixedHeight(30)
        points_number.setPlaceholderText('Количество точек')
        points_number.hide()
        chart_setttings_layout.addWidget(points_number)

        z_function = QtWidgets.QLineEdit()
        z_function.setObjectName('z_function')
        z_function.setFixedHeight(30)
        z_function.setPlaceholderText('Функция z-значений')
        z_function.hide()
        chart_setttings_layout.addWidget(z_function)

        width_label = QtWidgets.QLabel('Название графика:')
        chart_setttings_layout.addWidget(width_label)

        chart_name = QtWidgets.QLineEdit()
        chart_name.setObjectName('name')
        chart_name.setFixedHeight(30)
        chart_setttings_layout.addWidget(chart_name)

        size = QtWidgets.QWidget()
        size_layout = QtWidgets.QVBoxLayout()
        size_layout.setContentsMargins(0, 0, 0, 0)

        size_validator = QIntValidator()

        width_label = QtWidgets.QLabel('Ширина:')
        width = QtWidgets.QLineEdit('500')
        width.setFixedHeight(30)
        width.setObjectName('width')
        width.setValidator(size_validator)
        size_layout.addWidget(width_label)
        size_layout.addWidget(width)

        height_label = QtWidgets.QLabel('Высота:')
        height = QtWidgets.QLineEdit('400')
        height.setFixedHeight(30)
        height.setObjectName('height')
        height.setValidator(size_validator)
        size_layout.addWidget(height_label)
        size_layout.addWidget(height)

        size.setLayout(size_layout)

        chart_setttings_layout.addWidget(size)
        chart_setttings.setLayout(chart_setttings_layout)

        return chart_setttings
