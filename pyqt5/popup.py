# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\HMI-Lakban-Qt5\popup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(229, 50)
        Form.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.popup_text = QtWidgets.QLabel(Form)
        self.popup_text.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.popup_text.setStyleSheet("color: rgb(0, 79, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 76, 229);\n"
"font: 75 10pt \"Arial\";")
        self.popup_text.setFrameShape(QtWidgets.QFrame.Box)
        self.popup_text.setLineWidth(2)
        self.popup_text.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_text.setObjectName("popup_text")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(199, 0, 30, 30))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\";\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.popup_text.setText(_translate("Form", "Rework has been submitted."))
        self.pushButton.setText(_translate("Form", "x"))

