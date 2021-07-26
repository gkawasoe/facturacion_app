# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo_ep_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class epRegWindow(object):
    def setupUi(self, epRegWindow):
        if not epRegWindow.objectName():
            epRegWindow.setObjectName(u"epRegWindow")
        epRegWindow.resize(405, 483)
        epRegWindow.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(epRegWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(epRegWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 121, 16))
        self.idEpRegLineEdit = QLineEdit(epRegWindow)
        self.idEpRegLineEdit.setObjectName(u"idEpRegLineEdit")
        self.idEpRegLineEdit.setGeometry(QRect(30, 80, 200, 20))
        self.label_3 = QLabel(epRegWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.epRegTituloLineEdit = QLineEdit(epRegWindow)
        self.epRegTituloLineEdit.setObjectName(u"epRegTituloLineEdit")
        self.epRegTituloLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_4 = QLabel(epRegWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 101, 16))
        self.epRegCantLineEdit = QLineEdit(epRegWindow)
        self.epRegCantLineEdit.setObjectName(u"epRegCantLineEdit")
        self.epRegCantLineEdit.setGeometry(QRect(30, 180, 200, 20))
        self.label_6 = QLabel(epRegWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 270, 71, 16))
        self.epRegDescTextEdit = QTextEdit(epRegWindow)
        self.epRegDescTextEdit.setObjectName(u"epRegDescTextEdit")
        self.epRegDescTextEdit.setGeometry(QRect(30, 290, 351, 111))
        self.epRegAceptarButton = QPushButton(epRegWindow)
        self.epRegAceptarButton.setObjectName(u"epRegAceptarButton")
        self.epRegAceptarButton.setGeometry(QRect(80, 430, 101, 31))
        self.epRegAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.epRegAceptarButton.setIcon(icon)
        self.epRegAceptarButton.setFlat(True)
        self.epRegCancelarButton = QPushButton(epRegWindow)
        self.epRegCancelarButton.setObjectName(u"epRegCancelarButton")
        self.epRegCancelarButton.setGeometry(QRect(220, 430, 101, 31))
        self.epRegCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.epRegCancelarButton.setStyleSheet(u"QPushButton\n"
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
        self.epRegCancelarButton.setIcon(icon1)
        self.epRegCancelarButton.setFlat(True)
        self.label_5 = QLabel(epRegWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 91, 16))
        self.epRegPrecioLineEdit = QLineEdit(epRegWindow)
        self.epRegPrecioLineEdit.setObjectName(u"epRegPrecioLineEdit")
        self.epRegPrecioLineEdit.setGeometry(QRect(30, 240, 113, 20))

        self.retranslateUi(epRegWindow)

        QMetaObject.connectSlotsByName(epRegWindow)
    # setupUi

    def retranslateUi(self, epRegWindow):
        epRegWindow.setWindowTitle(QCoreApplication.translate("epRegWindow", u"Nuevo Equipo / Producto", None))
        self.label.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">NUEVO EQUIPO / PRODUCTO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p>Id. Equipo / Producto:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p>Titulo:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p>Cantidad en Stock:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.epRegAceptarButton.setText(QCoreApplication.translate("epRegWindow", u"  Registrar", None))
        self.epRegCancelarButton.setText(QCoreApplication.translate("epRegWindow", u"  Cancelar", None))
        self.label_5.setText(QCoreApplication.translate("epRegWindow", u"<html><head/><body><p>Precio Unit. ($):</p></body></html>", None))
    # retranslateUi

