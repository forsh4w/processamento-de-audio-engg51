# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseMusicWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chooseMusicWindow(object):
    def setupUi(self, chooseMusicWindow, files):
        chooseMusicWindow.setObjectName("chooseMusicWindow")
        chooseMusicWindow.resize(423, 47)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("iconMusicAnalyzer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        chooseMusicWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(chooseMusicWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseMusicBox = QtWidgets.QComboBox(self.widget)
        self.chooseMusicBox.setObjectName("chooseMusicBox")

        contador = 1

        for file in files:
            self.chooseMusicBox.addItem(
                str(contador) + "- " + (file.replace(".wav", "")).replace(".mp3", "")
            )
            contador += 1

        self.horizontalLayout_2.addWidget(self.chooseMusicBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.widget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.confirmButton = QtWidgets.QPushButton(self.widget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        chooseMusicWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(chooseMusicWindow)
        QtCore.QMetaObject.connectSlotsByName(chooseMusicWindow)

    def retranslateUi(self, chooseMusicWindow):
        _translate = QtCore.QCoreApplication.translate
        chooseMusicWindow.setWindowTitle(
            _translate("chooseMusicWindow", "Escolher a música")
        )
        self.playButton.setText(_translate("chooseMusicWindow", "Play"))
        self.confirmButton.setText(_translate("chooseMusicWindow", "Confirmar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    chooseMusicWindow = QtWidgets.QMainWindow()
    ui = Ui_chooseMusicWindow()
    ui.setupUi(chooseMusicWindow)
    chooseMusicWindow.show()
    sys.exit(app.exec_())
