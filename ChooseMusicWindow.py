# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseMusicWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MusicAnalyzer import MusicAnalyzer
from Popup import showDialog
import pygame
import matplotlib.pyplot as plt

# John
class Ui_chooseMusicWindow(object):
    def setupUi(self, Dialog, files, directories):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 45)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("iconMusicAnalyzer"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 10, 391, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseMuiscBox = QtWidgets.QComboBox(self.layoutWidget)
        self.chooseMuiscBox.setAccessibleName("")
        self.chooseMuiscBox.setAutoFillBackground(False)
        self.chooseMuiscBox.setObjectName("chooseMuiscBox")

        contador = 1

        for file in files:
            self.chooseMuiscBox.addItem(
                str(contador) + "- " + (file.replace(".wav", "")).replace(".mp3", "")
            )
            contador += 1

        self.horizontalLayout_2.addWidget(self.chooseMuiscBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.layoutWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.confirmButton = QtWidgets.QPushButton(self.layoutWidget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.confirmButton.clicked.connect(
            lambda: self.get_audio_details(files, directories)
        )
        self.playButton.clicked.connect(lambda: self.play_music(files, directories))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # John
    def get_audio_details(self, files, directories):
        position = self.chooseMuiscBox.currentIndex()
        file = str(position + 1) + ".wav"
        musicAnalyzer = MusicAnalyzer()
        details = musicAnalyzer.audio_details(file, directories)

        msg = (
            "Número de canais de som: "
            + str(details[0])
            + "          "
            + "\n"
            + "\n"
            + "Largura do sample: "
            + str(details[1])
            + "          "
            + "\n"
            + "\n"
            + "Frame rate: "
            + str(details[2])
            + "          "
            + "\n"
            + "\n"
            + "Número de frames: "
            + str(details[3])
            + "          "
        )

        showDialog("Detalhes do áudio", msg)

        musicAnalyzer.plot_graph(files, file, directories, position)
        # musicAnalyzer.show_spectrogram(files, file, directories, position)
        # musicAnalyzer.show_center_of_mass(files, file, directories, position)
        # musicAnalyzer.show_notes(files, file, directories, position)
        plt.show()

    # Sailon
    def play_music(self, files, directories):
        # workspace = directories[1]
        directory = directories[0]
        pygame.init()
        pygame.mixer.music.load(
            directory + "/" + files[self.chooseMuiscBox.currentIndex()]
        )
        # pygame.mixer.music.load(workspace + "/" + str(self.chooseMuiscBox.currentIndex() + 1) + ".wav")
        pygame.mixer.music.play()
        pygame.event.wait()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Escolher a música"))
        # self.chooseMuiscBox.setItemText(0, _translate("Dialog", "New Item"))
        self.playButton.setText(_translate("Dialog", "Play"))
        self.confirmButton.setText(_translate("Dialog", "Confirmar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_chooseMusicWindow()
    ui.setupUi(Dialog, [], [])
    Dialog.show()
    sys.exit(app.exec_())
