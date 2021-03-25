# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseDirectoryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MusicAnalyzer import MusicAnalyzer
from Application import prepare_files, analyze_files
from tkinter.filedialog import askdirectory
from ChooseMusicWindow import *


class Ui_chooseDirectoryWindow(object):
    def setupUi(self, chooseDirectoryWindow):
        chooseDirectoryWindow.setObjectName("chooseDirectoryWindow")
        chooseDirectoryWindow.resize(456, 82)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("iconMusicAnalyzer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        chooseDirectoryWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(chooseDirectoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(22, 10, 411, 58))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditDirectory = QtWidgets.QLineEdit(self.widget)
        self.lineEditDirectory.setObjectName("lineEditDirectory")
        self.horizontalLayout.addWidget(self.lineEditDirectory)
        self.chargeButton = QtWidgets.QPushButton(self.widget)
        self.chargeButton.setObjectName("chargeButton")
        self.horizontalLayout.addWidget(self.chargeButton)
        self.cleanButton = QtWidgets.QPushButton(self.widget)
        self.cleanButton.setObjectName("cleanButton")
        self.horizontalLayout.addWidget(self.cleanButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirmButton = QtWidgets.QPushButton(self.widget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_2.addWidget(self.confirmButton)
        self.crossfadeButton = QtWidgets.QPushButton(self.widget)
        self.crossfadeButton.setObjectName("crossfadeButton")
        self.horizontalLayout_2.addWidget(self.crossfadeButton)
        self.thanksButton = QtWidgets.QPushButton(self.widget)
        self.thanksButton.setObjectName("thanksButton")
        self.horizontalLayout_2.addWidget(self.thanksButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        chooseDirectoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(chooseDirectoryWindow)
        QtCore.QMetaObject.connectSlotsByName(chooseDirectoryWindow)

        self.directories = [""]

    def retranslateUi(self, chooseDirectoryWindow):
        _translate = QtCore.QCoreApplication.translate
        chooseDirectoryWindow.setWindowTitle(
            _translate("chooseDirectoryWindow", "Music Analyzer")
        )
        self.lineEditDirectory.setPlaceholderText(
            _translate(
                "chooseDirectoryWindow", "Escolher diretório com arquivos .mp3/.wav"
            )
        )
        self.chargeButton.setText(_translate("chooseDirectoryWindow", "Carregar"))
        self.cleanButton.setText(_translate("chooseDirectoryWindow", "Limpar"))
        self.confirmButton.setText(_translate("chooseDirectoryWindow", "Confirmar"))
        self.crossfadeButton.setText(_translate("chooseDirectoryWindow", "Crossfade"))
        self.thanksButton.setText(_translate("chooseDirectoryWindow", "Agradecimentos"))

    def openChooseMusicWindow(self):
        self.windows = QtWidgets.QMainWindow()
        self.ui = Ui_chooseMusicWindow()
        self.ui.setupUi(self.windows)
        self.windows.show()

    def get_directory(self):
        _translate = QtCore.QCoreApplication.translate
        directory = askdirectory()
        self.lineEditDirectory.setText(_translate("chooseDirectoryWindow", directory))
        workspace = directory + "/" + "Workspace"
        self.directories = [directory, workspace]

    def goToMusicChoiceStep(self, directories):
        if directories[0] != "":
            prepare_files(directories)
            self.openChooseMusicWindow()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    chooseDirectoryWindow = QtWidgets.QMainWindow()
    ui = Ui_chooseDirectoryWindow()
    ui.setupUi(chooseDirectoryWindow)
    chooseDirectoryWindow.show()
    sys.exit(app.exec_())
