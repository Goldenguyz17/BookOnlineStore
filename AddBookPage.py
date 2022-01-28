# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddBookPage.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import test_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(472, 607)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 471, 121))
        self.label.setStyleSheet(u"border-image: url(:/blue/library_bluejpg.jpg) 0 0 0 0 \n"
"stretch stretch;\n"
"border-radius:5px")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 120, 471, 491))
        self.label_2.setStyleSheet(u"border-image: url(:/blue/bg.jpg) 0 0 0 0 \n"
"stretch stretch;\n"
"border-radius:5px")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 161, 101, 20))
        self.label_4.setStyleSheet(u"background-color: rgb(158, 212, 249);\n"
"border-radius:5px")
        self.name_edit = QLineEdit(Form)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(110, 160, 141, 20))
        self.book_name_edit = QLineEdit(Form)
        self.book_name_edit.setObjectName(u"book_name_edit")
        self.book_name_edit.setGeometry(QRect(110, 200, 141, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 101, 21))
        self.label_5.setStyleSheet(u"background-color: rgb(158, 212, 249);\n"
"border-radius:5px")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 240, 141, 20))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 101, 21))
        self.label_6.setStyleSheet(u"background-color: rgb(158, 212, 249);\n"
"border-radius:5px")
        self.book_picture_edit = QLabel(Form)
        self.book_picture_edit.setObjectName(u"book_picture_edit")
        self.book_picture_edit.setGeometry(QRect(270, 150, 151, 181))
        self.book_picture_edit.setStyleSheet(u"border-style: solid;border-width: 1px;border-color: black;\n"
"background-color: rgb(255, 255, 255);")
        self.add_button = QPushButton(Form)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(160, 490, 131, 41))
        self.add_button.setStyleSheet(u"background-color: rgb(158, 212, 249);\n"
"border-radius:5px")
        self.add_book_picture = QPushButton(Form)
        self.add_book_picture.setObjectName(u"add_book_picture")
        self.add_book_picture.setGeometry(QRect(290, 370, 111, 21))
        self.add_book_picture.setStyleSheet(u"background-color: rgb(158, 212, 249);\n"
"border-radius:5px")
        self.labelicon = QLabel(Form)
        self.labelicon.setObjectName(u"labelicon")
        self.labelicon.setGeometry(QRect(0, 10, 141, 81))
        font = QFont()
        font.setFamily(u"Script MT Bold")
        font.setPointSize(30)
        self.labelicon.setFont(font)
        self.labelicon.setScaledContents(True)
        self.labelicon.setAlignment(Qt.AlignCenter)
        self.label_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.name_edit.raise_()
        self.book_name_edit.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.label_6.raise_()
        self.add_button.raise_()
        self.add_book_picture.raise_()
        self.labelicon.raise_()
        self.book_picture_edit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Book Author:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Book Name: </span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Price:</span></p></body></html>", None))
        self.book_picture_edit.setText("")
        self.add_button.setText(QCoreApplication.translate("Form", u"Add the Book", None))
        self.add_book_picture.setText(QCoreApplication.translate("Form", u"Add File Picture", None))
        self.labelicon.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">BOS</span></p></body></html>", None))
    # retranslateUi

