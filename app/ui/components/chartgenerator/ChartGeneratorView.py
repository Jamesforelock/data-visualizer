# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIntValidator


class ChartGeneratorView(QtWidgets.QWidget):
    selected_file_name_changed = pyqtSignal(str)

    def __init__(self, object_name: str) -> None:
        super(ChartGeneratorView, self).__init__()
        self.setObjectName(object_name)
        self._init_content()

    def _init_content(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self._get_chart_type_widget())
        column = QtWidgets.QWidget()
        column_layout = QtWidgets.QVBoxLayout()
        column_layout.addWidget(self._get_chart_settings_widget())
        visualize_button = QtWidgets.QPushButton('Визуализировать')
        visualize_button.setObjectName('visualize_button')
        column_layout.addWidget(visualize_button)
        column.setLayout(column_layout)
        layout.addWidget(column)

    @staticmethod
    def _get_chart_type_widget() -> QtWidgets.QWidget:
        chart_type = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel('Тип графика')
        layout.addWidget(label)

        radiobutton = QtWidgets.QRadioButton('Круговая диаграмма')
        radiobutton.setChecked(True)
        radiobutton.type = 'P'
        layout.addWidget(radiobutton)

        radiobutton = QtWidgets.QRadioButton('Столбчатая диаграмма')
        radiobutton.type = 'B'
        layout.addWidget(radiobutton)

        radiobutton = QtWidgets.QRadioButton('Линейный график')
        radiobutton.type = 'L'
        layout.addWidget(radiobutton)

        chart_type.setLayout(layout)

        return chart_type

    @staticmethod
    def _get_chart_settings_widget() -> QtWidgets.QWidget:
        chart_setttings = QtWidgets.QWidget()
        chart_setttings_layout = QtWidgets.QVBoxLayout()

        chart_name = QtWidgets.QLineEdit()
        chart_name.setObjectName('name')
        chart_name.setFixedHeight(30)
        chart_name.setPlaceholderText('Название графика')
        chart_setttings_layout.addWidget(chart_name)

        size = QtWidgets.QWidget()
        size_layout = QtWidgets.QHBoxLayout()

        size_validator = QIntValidator()

        width_label = QtWidgets.QLabel('Ширина:')
        width = QtWidgets.QLineEdit('500')
        width.setObjectName('width')
        width.setValidator(size_validator)
        size_layout.addWidget(width_label)
        size_layout.addWidget(width)

        height_label = QtWidgets.QLabel('Высота:')
        height = QtWidgets.QLineEdit('400')
        height.setObjectName('height')
        height.setValidator(size_validator)
        size_layout.addWidget(height_label)
        size_layout.addWidget(height)

        size.setLayout(size_layout)

        chart_setttings_layout.addWidget(size)
        chart_setttings.setLayout(chart_setttings_layout)

        return chart_setttings
