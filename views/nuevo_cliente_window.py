# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo_cliente_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class clienteRegWindow(object):
    def setupUi(self, clienteRegWindow):
        if not clienteRegWindow.objectName():
            clienteRegWindow.setObjectName(u"clienteRegWindow")
        clienteRegWindow.resize(405, 472)
        clienteRegWindow.setStyleSheet(u"QPushButton\n"
"{\n"
"	height: 2em;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #0069c0;\n"
"	color: white;\n"
"} ")
        self.label = QLabel(clienteRegWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(clienteRegWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.clienteRegLineEdit = QLineEdit(clienteRegWindow)
        self.clienteRegLineEdit.setObjectName(u"clienteRegLineEdit")
        self.clienteRegLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(clienteRegWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.clienteRegCedLineEdit = QLineEdit(clienteRegWindow)
        self.clienteRegCedLineEdit.setObjectName(u"clienteRegCedLineEdit")
        self.clienteRegCedLineEdit.setGeometry(QRect(30, 130, 113, 20))
        self.label_4 = QLabel(clienteRegWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 71, 16))
        self.clienteRegEmailLineEdit = QLineEdit(clienteRegWindow)
        self.clienteRegEmailLineEdit.setObjectName(u"clienteRegEmailLineEdit")
        self.clienteRegEmailLineEdit.setGeometry(QRect(30, 180, 200, 20))
        self.label_5 = QLabel(clienteRegWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 71, 16))
        self.clienteRegTelfLineEdit = QLineEdit(clienteRegWindow)
        self.clienteRegTelfLineEdit.setObjectName(u"clienteRegTelfLineEdit")
        self.clienteRegTelfLineEdit.setGeometry(QRect(30, 230, 200, 20))
        self.label_6 = QLabel(clienteRegWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 47, 13))
        self.clienteRegDirTextEdit = QTextEdit(clienteRegWindow)
        self.clienteRegDirTextEdit.setObjectName(u"clienteRegDirTextEdit")
        self.clienteRegDirTextEdit.setGeometry(QRect(30, 280, 351, 111))
        self.clienteRegAceptarButton = QPushButton(clienteRegWindow)
        self.clienteRegAceptarButton.setObjectName(u"clienteRegAceptarButton")
        self.clienteRegAceptarButton.setGeometry(QRect(70, 430, 101, 31))
        self.clienteRegAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteRegAceptarButton.setIcon(icon)
        self.clienteRegAceptarButton.setFlat(True)
        self.clienteRegCancelarButton = QPushButton(clienteRegWindow)
        self.clienteRegCancelarButton.setObjectName(u"clienteRegCancelarButton")
        self.clienteRegCancelarButton.setGeometry(QRect(210, 430, 101, 31))
        self.clienteRegCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clienteRegCancelarButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	height: 2em;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: grey;\n"
"	color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/botones/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteRegCancelarButton.setIcon(icon1)
        self.clienteRegCancelarButton.setFlat(True)

        self.retranslateUi(clienteRegWindow)

        QMetaObject.connectSlotsByName(clienteRegWindow)
    # setupUi

    def retranslateUi(self, clienteRegWindow):
        clienteRegWindow.setWindowTitle(QCoreApplication.translate("clienteRegWindow", u"Nuevo Cliente", None))
        self.label.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">NUEVO CLIENTE</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p>Nombre:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p>RIF / C\u00e9dula:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p>Email:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p>Tel\u00e9fono:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("clienteRegWindow", u"<html><head/><body><p>Direcci\u00f3n:</p></body></html>", None))
        self.clienteRegAceptarButton.setText(QCoreApplication.translate("clienteRegWindow", u"  Registrar", None))
        self.clienteRegCancelarButton.setText(QCoreApplication.translate("clienteRegWindow", u"  Cancelar", None))
    # retranslateUi

