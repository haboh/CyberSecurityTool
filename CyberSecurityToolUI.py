# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CyberSecurityTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CyberSecurityTool(object):
    def setupUi(self, CyberSecurityTool):
        CyberSecurityTool.setObjectName("CyberSecurityTool")
        CyberSecurityTool.setWindowModality(QtCore.Qt.ApplicationModal)
        CyberSecurityTool.resize(916, 595)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        CyberSecurityTool.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CyberSecurityTool)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 572))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FrequencyTextAnalysisButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.FrequencyTextAnalysisButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.FrequencyTextAnalysisButton.setFont(font)
        self.FrequencyTextAnalysisButton.setObjectName("FrequencyTextAnalysisButton")
        self.verticalLayout_2.addWidget(self.FrequencyTextAnalysisButton)
        self.LSBcipherButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LSBcipherButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LSBcipherButton.setFont(font)
        self.LSBcipherButton.setToolTipDuration(-1)
        self.LSBcipherButton.setObjectName("LSBcipherButton")
        self.verticalLayout_2.addWidget(self.LSBcipherButton)
        self.CryptoToolButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CryptoToolButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CryptoToolButton.setFont(font)
        self.CryptoToolButton.setObjectName("CryptoToolButton")
        self.verticalLayout_2.addWidget(self.CryptoToolButton)
        self.SteganoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SteganoButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SteganoButton.setFont(font)
        self.SteganoButton.setObjectName("SteganoButton")
        self.verticalLayout_2.addWidget(self.SteganoButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.PixMap = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.PixMap.setMinimumSize(QtCore.QSize(570, 570))
        self.PixMap.setMaximumSize(QtCore.QSize(570, 570))
        self.PixMap.setText("")
        self.PixMap.setObjectName("PixMap")
        self.horizontalLayout.addWidget(self.PixMap)
        CyberSecurityTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CyberSecurityTool)
        self.statusbar.setObjectName("statusbar")
        CyberSecurityTool.setStatusBar(self.statusbar)

        self.retranslateUi(CyberSecurityTool)
        QtCore.QMetaObject.connectSlotsByName(CyberSecurityTool)

    def retranslateUi(self, CyberSecurityTool):
        _translate = QtCore.QCoreApplication.translate
        CyberSecurityTool.setWindowTitle(_translate("CyberSecurityTool", "MainWindow"))
        self.FrequencyTextAnalysisButton.setText(_translate("CyberSecurityTool", "Frequency Text Analysis"))
        self.LSBcipherButton.setText(_translate("CyberSecurityTool", "LSBcipher"))
        self.CryptoToolButton.setText(_translate("CyberSecurityTool", "CryptoTool"))
        self.SteganoButton.setText(_translate("CyberSecurityTool", "Stegano"))

