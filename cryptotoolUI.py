# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cryptotool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CryptoTool(object):
    def setupUi(self, CryptoTool):
        CryptoTool.setObjectName("CryptoTool")
        CryptoTool.resize(264, 463)
        self.centralwidget = QtWidgets.QWidget(CryptoTool)
        self.centralwidget.setObjectName("centralwidget")
        self.Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(10, 20, 241, 161))
        self.Input.setObjectName("Input")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(140, 400, 111, 33))
        self.decodeButton.setObjectName("decodeButton")
        self.Output = QtWidgets.QLineEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(10, 220, 241, 161))
        self.Output.setObjectName("Output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 181, 17))
        self.label_2.setObjectName("label_2")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(10, 400, 101, 33))
        self.encodeButton.setObjectName("encodeButton")
        CryptoTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CryptoTool)
        self.statusbar.setObjectName("statusbar")
        CryptoTool.setStatusBar(self.statusbar)

        self.retranslateUi(CryptoTool)
        QtCore.QMetaObject.connectSlotsByName(CryptoTool)

    def retranslateUi(self, CryptoTool):
        _translate = QtCore.QCoreApplication.translate
        CryptoTool.setWindowTitle(_translate("CryptoTool", "CryptoTool"))
        self.decodeButton.setText(_translate("CryptoTool", "Decode Input"))
        self.label.setText(_translate("CryptoTool", "Input:"))
        self.label_2.setText(_translate("CryptoTool", "Output:"))
        self.encodeButton.setText(_translate("CryptoTool", "Encode Input"))

