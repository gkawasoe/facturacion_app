# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo_serv_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class servRegWindow(object):
    def setupUi(self, servRegWindow):
        if not servRegWindow.objectName():
            servRegWindow.setObjectName(u"servRegWindow")
        servRegWindow.resize(405, 407)
        servRegWindow.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(servRegWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(servRegWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 121, 16))
        self.idServRegLineEdit = QLineEdit(servRegWindow)
        self.idServRegLineEdit.setObjectName(u"idServRegLineEdit")
        self.idServRegLineEdit.setGeometry(QRect(30, 80, 200, 20))
        self.label_3 = QLabel(servRegWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.servRegTituloLineEdit = QLineEdit(servRegWindow)
        self.servRegTituloLineEdit.setObjectName(u"servRegTituloLineEdit")
        self.servRegTituloLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_6 = QLabel(servRegWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 210, 71, 16))
        self.servRegDescTextEdit = QTextEdit(servRegWindow)
        self.servRegDescTextEdit.setObjectName(u"servRegDescTextEdit")
        self.servRegDescTextEdit.setGeometry(QRect(30, 230, 351, 111))
        self.servRegAceptarButton = QPushButton(servRegWindow)
        self.servRegAceptarButton.setObjectName(u"servRegAceptarButton")
        self.servRegAceptarButton.setGeometry(QRect(80, 360, 101, 31))
        self.servRegAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servRegAceptarButton.setIcon(icon)
        self.servRegAceptarButton.setFlat(True)
        self.servRegCancelarButton = QPushButton(servRegWindow)
        self.servRegCancelarButton.setObjectName(u"servRegCancelarButton")
        self.servRegCancelarButton.setGeometry(QRect(220, 360, 101, 31))
        self.servRegCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.servRegCancelarButton.setStyleSheet(u"QPushButton\n"
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
        self.servRegCancelarButton.setIcon(icon1)
        self.servRegCancelarButton.setFlat(True)
        self.label_5 = QLabel(servRegWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 160, 91, 16))
        self.servRegPrecioLineEdit = QLineEdit(servRegWindow)
        self.servRegPrecioLineEdit.setObjectName(u"servRegPrecioLineEdit")
        self.servRegPrecioLineEdit.setGeometry(QRect(30, 180, 113, 20))

        self.retranslateUi(servRegWindow)

        QMetaObject.connectSlotsByName(servRegWindow)
    # setupUi

    def retranslateUi(self, servRegWindow):
        servRegWindow.setWindowTitle(QCoreApplication.translate("servRegWindow", u"Nuevo Servicio", None))
        self.label.setText(QCoreApplication.translate("servRegWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">NUEVO SERVICIO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("servRegWindow", u"<html><head/><body><p>Id. Servicio</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("servRegWindow", u"<html><head/><body><p>Titulo:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("servRegWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.servRegAceptarButton.setText(QCoreApplication.translate("servRegWindow", u"  Registrar", None))
        self.servRegCancelarButton.setText(QCoreApplication.translate("servRegWindow", u"  Cancelar", None))
        self.label_5.setText(QCoreApplication.translate("servRegWindow", u"<html><head/><body><p>Precio Unit. ($):</p></body></html>", None))
    # retranslateUi

