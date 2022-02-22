# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIntValidator, QFont
from app.lib.chart.ChartService import ChartService


class ChartGeneratorView(QtWidgets.QWidget):
    selected_file_name_changed = pyqtSignal(str)

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
        column_layout.setAlignment(Qt.AlignVCenter)
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

        label = QtWidgets.QLabel('Тип графика')
        layout.addWidget(label)

        radiobuttons = {
            ChartService.DOT_CHART_TYPE: 'Точечный график',
            ChartService.LINE_CHART_TYPE: 'Линейный график',
            ChartService.BAR_CHART_TYPE: 'Столбчатая диаграмма',
            ChartService.PIE_CHART_TYPE: 'Круговая диаграмма',
            ChartService.DOT_CHART_3D_TYPE: 'Точечный 3D-график',
            ChartService.LINE_CHART_3D_TYPE: 'Линейный 3D-график',
            ChartService.WIREFRAME_CHART_TYPE: 'Каркасная поверхность',
            ChartService.SURFACE_CHART_3D_TYPE: 'Поверхность',
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

        chart_name = QtWidgets.QLineEdit()
        chart_name.setObjectName('name')
        chart_name.setFixedHeight(30)
        chart_name.setPlaceholderText('Название графика')
        chart_setttings_layout.addWidget(chart_name)

        z_function = QtWidgets.QLineEdit()
        z_function.setObjectName('z_function')
        z_function.setFixedHeight(30)
        z_function.setPlaceholderText('Функция z-значений')
        z_function.hide()
        chart_setttings_layout.addWidget(z_function)

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
