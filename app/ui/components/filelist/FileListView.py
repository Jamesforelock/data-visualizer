# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QCursor


class FileListView(QtWidgets.QWidget):
    selected_file_name_changed = pyqtSignal(str)

    def __init__(self, object_name: str) -> None:
        super(FileListView, self).__init__()
        self.setObjectName(object_name)
        self._init_content()

    def _init_content(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(FileListView._get_file_list_widget())
        layout.addWidget(FileListView._get_buttons())

    @staticmethod
    def _get_file_list_widget() -> QtWidgets.QListWidget:
        file_list = QtWidgets.QListWidget()
        file_list.setObjectName('list')
        file_list.setFixedSize(300, 150)

        return file_list

    @staticmethod
    def _get_buttons() -> QtWidgets.QWidget:
        buttons = QtWidgets.QWidget()

        buttons_layout = QtWidgets.QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignTop)

        add_button = QtWidgets.QPushButton('Добавить файл')
        add_button.setObjectName('add_button')
        add_button.setFont(QFont('Arial'))
        add_button.setCursor(QCursor(Qt.PointingHandCursor))
        buttons_layout.addWidget(add_button)

        remove_button = QtWidgets.QPushButton('Удалить файл')
        remove_button.setObjectName('remove_button')
        remove_button.setFont(QFont('Arial'))
        remove_button.setCursor(QCursor(Qt.PointingHandCursor))
        buttons_layout.addWidget(remove_button)

        buttons.setLayout(buttons_layout)

        return buttons
