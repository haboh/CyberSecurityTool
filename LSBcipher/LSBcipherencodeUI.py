# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LSBcipherencode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class LSBEncodeUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previewButton = QtWidgets.QPushButton(self.centralwidget)
        self.previewButton.setGeometry(QtCore.QRect(260, 50, 91, 33))
        self.previewButton.setObjectName("previewButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 211, 21))
        self.label.setObjectName("label")
        self.pathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathEdit.setGeometry(QtCore.QRect(40, 50, 171, 31))
        self.pathEdit.setObjectName("pathEdit")
        self.previewLabel = QtWidgets.QLabel(self.centralwidget)
        self.previewLabel.setGeometry(QtCore.QRect(50, 120, 101, 91))
        self.previewLabel.setObjectName("previewLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 101, 17))
        self.label_2.setObjectName("label_2")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(190, 160, 141, 41))
        self.encodeButton.setObjectName("encodeButton")
        self.fileExplorerButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileExplorerButton.setGeometry(QtCore.QRect(220, 50, 31, 33))
        self.fileExplorerButton.setObjectName("fileExplorerButton")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(60, 80, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.msgEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.msgEdit.setGeometry(QtCore.QRect(20, 250, 341, 31))
        self.msgEdit.setObjectName("msgEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 331, 21))
        self.label_3.setObjectName("label_3")
        self.saveFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveFileButton.setGeometry(QtCore.QRect(270, 290, 93, 28))
        self.saveFileButton.setObjectName("saveFileButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LSBcipher decode mode"))
        self.previewButton.setText(_translate("MainWindow", "Preview"))
        self.label.setText(_translate("MainWindow", "Print full path to your image here:"))
        self.previewLabel.setText(_translate("MainWindow", "Preview"))
        self.label_2.setText(_translate("MainWindow", "Image preview:"))
        self.encodeButton.setText(_translate("MainWindow", "Encode LSB message"))
        self.fileExplorerButton.setText(_translate("MainWindow", "F"))
        self.label_1.setText(_translate("MainWindow", "*working only with png/bmp/jpg etc"))
        self.label_3.setText(_translate("MainWindow", "Print your binary message you want to encode here:"))
        self.saveFileButton.setText(_translate("MainWindow", "Save"))

