# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LSBcipher.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class LSBMainUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 219)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, -10, 351, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 111, 17))
        self.label_2.setObjectName("label_2")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(10, 60, 181, 131))
        self.decodeButton.setObjectName("decodeButton")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(200, 60, 181, 131))
        self.encodeButton.setObjectName("encodeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LSBcipher"))
        self.label.setText(_translate("MainWindow", "Welcome to the LSBcipher, what do you want to do"))
        self.label_2.setText(_translate("MainWindow", " with LSB message?"))
        self.decodeButton.setText(_translate("MainWindow", "Decode LSB message"))
        self.encodeButton.setText(_translate("MainWindow", "Encode LSB message"))

