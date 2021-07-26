# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_cliente_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class clienteModWindow(object):
    def setupUi(self, clienteModWindow):
        if not clienteModWindow.objectName():
            clienteModWindow.setObjectName(u"clienteModWindow")
        clienteModWindow.resize(405, 472)
        clienteModWindow.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(clienteModWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(clienteModWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.clienteModLineEdit = QLineEdit(clienteModWindow)
        self.clienteModLineEdit.setObjectName(u"clienteModLineEdit")
        self.clienteModLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(clienteModWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.clienteModCedLineEdit = QLineEdit(clienteModWindow)
        self.clienteModCedLineEdit.setObjectName(u"clienteModCedLineEdit")
        self.clienteModCedLineEdit.setGeometry(QRect(30, 130, 113, 20))
        self.label_4 = QLabel(clienteModWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 71, 16))
        self.clienteModEmailLineEdit = QLineEdit(clienteModWindow)
        self.clienteModEmailLineEdit.setObjectName(u"clienteModEmailLineEdit")
        self.clienteModEmailLineEdit.setGeometry(QRect(30, 180, 200, 20))
        self.label_5 = QLabel(clienteModWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 71, 16))
        self.clienteModTelfLineEdit = QLineEdit(clienteModWindow)
        self.clienteModTelfLineEdit.setObjectName(u"clienteModTelfLineEdit")
        self.clienteModTelfLineEdit.setGeometry(QRect(30, 230, 200, 20))
        self.label_6 = QLabel(clienteModWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 47, 13))
        self.clienteModDirTextEdit = QTextEdit(clienteModWindow)
        self.clienteModDirTextEdit.setObjectName(u"clienteModDirTextEdit")
        self.clienteModDirTextEdit.setGeometry(QRect(30, 280, 351, 111))
        self.clienteModAceptarButton = QPushButton(clienteModWindow)
        self.clienteModAceptarButton.setObjectName(u"clienteModAceptarButton")
        self.clienteModAceptarButton.setGeometry(QRect(70, 430, 101, 31))
        self.clienteModAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteModAceptarButton.setIcon(icon)
        self.clienteModAceptarButton.setFlat(True)
        self.clienteModCancelarButton = QPushButton(clienteModWindow)
        self.clienteModCancelarButton.setObjectName(u"clienteModCancelarButton")
        self.clienteModCancelarButton.setGeometry(QRect(210, 430, 101, 31))
        self.clienteModCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clienteModCancelarButton.setStyleSheet(u"QPushButton\n"
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
        self.clienteModCancelarButton.setIcon(icon1)
        self.clienteModCancelarButton.setFlat(True)

        self.retranslateUi(clienteModWindow)

        QMetaObject.connectSlotsByName(clienteModWindow)
    # setupUi

    def retranslateUi(self, clienteModWindow):
        clienteModWindow.setWindowTitle(QCoreApplication.translate("clienteModWindow", u"Modificar Cliente", None))
        self.label.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MODIFICAR CLIENTE</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p>Nombre:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p>RIF / C\u00e9dula:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p>Email:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p>Tel\u00e9fono:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("clienteModWindow", u"<html><head/><body><p>Direcci\u00f3n:</p></body></html>", None))
        self.clienteModAceptarButton.setText(QCoreApplication.translate("clienteModWindow", u"  Registrar", None))
        self.clienteModCancelarButton.setText(QCoreApplication.translate("clienteModWindow", u"  Cancelar", None))
    # retranslateUi

