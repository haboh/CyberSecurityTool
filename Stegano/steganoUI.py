# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stegano.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stegano(object):
    def setupUi(self, Stegano):
        Stegano.setObjectName("Stegano")
        Stegano.resize(1134, 593)
        self.centralwidget = QtWidgets.QWidget(Stegano)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(870, 120, 261, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DefaultButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.DefaultButton.setObjectName("DefaultButton")
        self.verticalLayout.addWidget(self.DefaultButton)
        self.XORButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.XORButton.setObjectName("XORButton")
        self.verticalLayout.addWidget(self.XORButton)
        self.RedPlaneButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.RedPlaneButton.setObjectName("RedPlaneButton")
        self.verticalLayout.addWidget(self.RedPlaneButton)
        self.GreenPlaneButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.GreenPlaneButton.setObjectName("GreenPlaneButton")
        self.verticalLayout.addWidget(self.GreenPlaneButton)
        self.BluePlaneButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.BluePlaneButton.setObjectName("BluePlaneButton")
        self.verticalLayout.addWidget(self.BluePlaneButton)
        self.FullRedButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.FullRedButton.setObjectName("FullRedButton")
        self.verticalLayout.addWidget(self.FullRedButton)
        self.FullGreenButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.FullGreenButton.setObjectName("FullGreenButton")
        self.verticalLayout.addWidget(self.FullGreenButton)
        self.FullBlueButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.FullBlueButton.setObjectName("FullBlueButton")
        self.verticalLayout.addWidget(self.FullBlueButton)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Stegano.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Stegano)
        self.statusbar.setObjectName("statusbar")
        Stegano.setStatusBar(self.statusbar)

        self.retranslateUi(Stegano)
        QtCore.QMetaObject.connectSlotsByName(Stegano)

    def retranslateUi(self, Stegano):
        _translate = QtCore.QCoreApplication.translate
        Stegano.setWindowTitle(_translate("Stegano", "MainWindow"))
        self.label.setText(_translate("Stegano", "Stegano"))
        self.DefaultButton.setText(_translate("Stegano", "Default"))
        self.XORButton.setText(_translate("Stegano", "XOR (Negative)"))
        self.RedPlaneButton.setText(_translate("Stegano", "Red Plane"))
        self.GreenPlaneButton.setText(_translate("Stegano", "Green Plane"))
        self.BluePlaneButton.setText(_translate("Stegano", "Blue Plane"))
        self.FullRedButton.setText(_translate("Stegano", "Full Red"))
        self.FullGreenButton.setText(_translate("Stegano", "Full Green"))
        self.FullBlueButton.setText(_translate("Stegano", "Full Blue"))
        self.pushButton.setText(_translate("Stegano", "Select file"))
