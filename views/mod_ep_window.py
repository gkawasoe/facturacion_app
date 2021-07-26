# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_ep_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class epModWindow(object):
    def setupUi(self, epModWindow):
        if not epModWindow.objectName():
            epModWindow.setObjectName(u"epModWindow")
        epModWindow.resize(405, 483)
        epModWindow.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(epModWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(epModWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 121, 16))
        self.idEpModLineEdit = QLineEdit(epModWindow)
        self.idEpModLineEdit.setObjectName(u"idEpModLineEdit")
        self.idEpModLineEdit.setGeometry(QRect(30, 80, 200, 20))
        self.label_3 = QLabel(epModWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.epModTituloLineEdit = QLineEdit(epModWindow)
        self.epModTituloLineEdit.setObjectName(u"epModTituloLineEdit")
        self.epModTituloLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_4 = QLabel(epModWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 101, 16))
        self.epModCantLineEdit = QLineEdit(epModWindow)
        self.epModCantLineEdit.setObjectName(u"epModCantLineEdit")
        self.epModCantLineEdit.setGeometry(QRect(30, 180, 200, 20))
        self.label_6 = QLabel(epModWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 270, 71, 16))
        self.epModDescTextEdit = QTextEdit(epModWindow)
        self.epModDescTextEdit.setObjectName(u"epModDescTextEdit")
        self.epModDescTextEdit.setGeometry(QRect(30, 290, 351, 111))
        self.epModAceptarButton = QPushButton(epModWindow)
        self.epModAceptarButton.setObjectName(u"epModAceptarButton")
        self.epModAceptarButton.setGeometry(QRect(80, 430, 101, 31))
        self.epModAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.epModAceptarButton.setIcon(icon)
        self.epModAceptarButton.setFlat(True)
        self.epModCancelarButton = QPushButton(epModWindow)
        self.epModCancelarButton.setObjectName(u"epModCancelarButton")
        self.epModCancelarButton.setGeometry(QRect(220, 430, 101, 31))
        self.epModCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.epModCancelarButton.setStyleSheet(u"QPushButton\n"
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
        self.epModCancelarButton.setIcon(icon1)
        self.epModCancelarButton.setFlat(True)
        self.label_5 = QLabel(epModWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 91, 16))
        self.epModPrecioLineEdit = QLineEdit(epModWindow)
        self.epModPrecioLineEdit.setObjectName(u"epModPrecioLineEdit")
        self.epModPrecioLineEdit.setGeometry(QRect(30, 240, 113, 20))

        self.retranslateUi(epModWindow)

        QMetaObject.connectSlotsByName(epModWindow)
    # setupUi

    def retranslateUi(self, epModWindow):
        epModWindow.setWindowTitle(QCoreApplication.translate("epModWindow", u"Modificar Equipo / Producto", None))
        self.label.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MODIFICAR EQUIPO / PRODUCTO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p>Id. Equipo / Producto:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p>Titulo:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p>Cantidad en Stock:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.epModAceptarButton.setText(QCoreApplication.translate("epModWindow", u"Modificar", None))
        self.epModCancelarButton.setText(QCoreApplication.translate("epModWindow", u"  Cancelar", None))
        self.label_5.setText(QCoreApplication.translate("epModWindow", u"<html><head/><body><p>Precio Unit. ($):</p></body></html>", None))
    # retranslateUi

