# @author Denis Chuprynin <denischuprynin@gmail.com>


from PyQt5 import QtWidgets


class DialogBoxComponent:
    def __init__(self, title: str, message: str, message_type=''):
        self.view = QtWidgets.QMessageBox()
        if message_type == 'error':
            self.view.setIcon(QtWidgets.QMessageBox.Critical)
        else:
            self.view.setIcon(QtWidgets.QMessageBox.Information)
        self.view.setWindowTitle(title)
        self.view.setText(message)
        self.view.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def __call__(self):
        self.view.exec()
