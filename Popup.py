import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


def showDialog(title, msg):
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap("iconMusicAnalyzer"), QtGui.QIcon.Normal, QtGui.QIcon.Off
    )
    msgBox = QMessageBox()
    msgBox.setWindowIcon(icon)
    msgBox.setText(msg)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        msgBox.accept()
