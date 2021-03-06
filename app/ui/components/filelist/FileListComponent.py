# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets
from app.lib.file.FileService import FileService
from app.lib.file.FileServiceException import FileServiceException
from app.lib.mysql.MysqlConnectionCreator import MysqlConnectionCreator
from app.lib.mysql.MysqlService import MysqlService
from app.ui.components.filelist.FileListView import FileListView
from app.ui.components.dialogbox.DialogBoxComponent import DialogBoxComponent


class FileListComponent:
    def __init__(self, object_name: str) -> None:
        self.view = FileListView(object_name)
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

        mysql_export_button = self.view.findChild(QtWidgets.QPushButton, 'mysql_export_button')
        mysql_export_button.clicked.connect(lambda: self._create_csv_from_mysql_table())

        self.file_list.currentItemChanged.connect(
            lambda: self.view.selected_file_name_changed.emit(
                self.file_list.currentItem().text() if self.file_list.currentItem() is not None else '')
        )

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

    def _create_csv_from_mysql_table(self) -> None:
        table_name = self._input_table_name()
        if table_name == '':
            return

        create_header = self.view.findChild(QtWidgets.QCheckBox, 'create_header_checkbox').isChecked()
        try:
            connection = MysqlConnectionCreator().get_connection()
            mysql_service = MysqlService(connection)
            mysql_service.create_csv_from_table(table_name, create_header)
            self._update_list()
        except Exception as e:
            DialogBoxComponent('????????????', str(e), 'error')()

    def _input_table_name(self) -> str:
        dlg = QtWidgets.QInputDialog()
        table_name, ok = dlg.getText(self.view, '?????????????????? ???????????? ???? ?????????????? MySQL', '?????????????? ???????????????? ??????????????')
        if not ok:
            return ''
        return table_name.strip()

    def _add_file(self, src_path: str) -> None:
        if not src_path:
            return
        try:
            FileService.copy_file_to_data_dir(src_path)
            self._update_list()
            DialogBoxComponent('??????????', '???????? ?????????????? ????????????????')()
        except FileServiceException as e:
            DialogBoxComponent('????????????', str(e), 'error')()

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
            DialogBoxComponent('????????????', str(e), 'error')()
