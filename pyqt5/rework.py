# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\HMI_Lakban\rework.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 376)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 171, 51))
        self.label.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 87 24pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 175, 221, 61))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.line_val = QtWidgets.QLabel(Form)
        self.line_val.setGeometry(QtCore.QRect(340, 100, 161, 41))
        self.line_val.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(236, 236, 236);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.line_val.setAlignment(QtCore.Qt.AlignCenter)
        self.line_val.setObjectName("line_val")
        self.pb_submit = QtWidgets.QPushButton(Form)
        self.pb_submit.setGeometry(QtCore.QRect(0, 280, 611, 101))
        self.pb_submit.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pb_submit.setObjectName("pb_submit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(540, -10, 41, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 48pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.next_btn = QtWidgets.QLabel(Form)
        self.next_btn.setGeometry(QtCore.QRect(476, 180, 94, 49))
        self.next_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.next_btn.setText("")
        self.next_btn.setPixmap(QtGui.QPixmap("right_chevron.png"))
        self.next_btn.setScaledContents(False)
        self.next_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.next_btn.setObjectName("next_btn")
        self.prev_btn = QtWidgets.QLabel(Form)
        self.prev_btn.setGeometry(QtCore.QRect(290, 180, 94, 49))
        self.prev_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.prev_btn.setText("")
        self.prev_btn.setPixmap(QtGui.QPixmap("left_chevron.png"))
        self.prev_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.prev_btn.setObjectName("prev_btn")
        self.rework_val = QtWidgets.QLabel(Form)
        self.rework_val.setGeometry(QtCore.QRect(390, 180, 80, 49))
        self.rework_val.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.rework_val.setAlignment(QtCore.Qt.AlignCenter)
        self.rework_val.setObjectName("rework_val")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "REWORK"))
        self.label_2.setText(_translate("Form", "Line :"))
        self.label_3.setText(_translate("Form", "Jumlah Rework :"))
        self.line_val.setText(_translate("Form", "Line 23"))
        self.pb_submit.setText(_translate("Form", "SUBMIT"))
        self.label_5.setText(_translate("Form", "x"))
        self.rework_val.setText(_translate("Form", "1000"))

