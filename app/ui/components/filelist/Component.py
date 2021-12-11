# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from app.lib.file.Service import Service as FileService
from app.lib.file.ServiceException import ServiceException as FileServiceException
from app.ui.components.filelist.View import View


class Component:
    def __init__(self, object_name: str) -> None:
        self.view = View(object_name)
        self.file_list = self.view.findChild(QtWidgets.QListWidget, 'list')
        self._register_event_handlers()
        self._update_list()

    def __call__(self) -> QtWidgets.QWidget:
        return self.view

    def _register_event_handlers(self) -> None:
        add_button = self.view.findChild(QtWidgets.QPushButton, 'add_button')
        add_button.clicked.connect(lambda: self._add_file(self._choose_file_to_add()))

        remove_button = self.view.findChild(QtWidgets.QPushButton, 'remove_button')
        remove_button.clicked.connect(lambda: self._remove_selected_file())

    def _update_list(self) -> None:
        self.file_list.clear()
        self.file_list.addItems(FileService.get_file_list())

    @staticmethod
    def _choose_file_to_add() -> str:
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dlg.setNameFilter('CSV (*.csv)')
        dlg.exec()
        if not dlg.selectedFiles():
            return ''

        return dlg.selectedFiles()[0]

    def _add_file(self, src_path: str) -> None:
        if not src_path:
            return
        try:
            FileService.copy_file_to_data_dir(src_path)
            self._update_list()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle('Успех')
            msg.setText('Файл успешно добавлен')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
        except FileServiceException as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle('Ошибка')
            msg.setText(str(e))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()

    def _remove_selected_file(self) -> None:
        if self.file_list.currentItem() is None:
            return
        try:
            file_name = self.file_list.currentItem().text()
            FileService.remove_file(file_name)
            self._update_list()
            if len(self.file_list) == 0:
                self.selected_file_name = ''
                return
        except FileServiceException as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle('Ошибка')
            msg.setText(str(e))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
