# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_serv_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class servModWindow(object):
    def setupUi(self, servModWindow):
        if not servModWindow.objectName():
            servModWindow.setObjectName(u"servModWindow")
        servModWindow.resize(405, 407)
        servModWindow.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(servModWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(servModWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 121, 16))
        self.idServModLineEdit = QLineEdit(servModWindow)
        self.idServModLineEdit.setObjectName(u"idServModLineEdit")
        self.idServModLineEdit.setGeometry(QRect(30, 80, 200, 20))
        self.label_3 = QLabel(servModWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 16))
        self.servModTituloLineEdit = QLineEdit(servModWindow)
        self.servModTituloLineEdit.setObjectName(u"servModTituloLineEdit")
        self.servModTituloLineEdit.setGeometry(QRect(30, 130, 351, 20))
        self.label_6 = QLabel(servModWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 210, 71, 16))
        self.servModDescTextEdit = QTextEdit(servModWindow)
        self.servModDescTextEdit.setObjectName(u"servModDescTextEdit")
        self.servModDescTextEdit.setGeometry(QRect(30, 230, 351, 111))
        self.servModAceptarButton = QPushButton(servModWindow)
        self.servModAceptarButton.setObjectName(u"servModAceptarButton")
        self.servModAceptarButton.setGeometry(QRect(80, 360, 101, 31))
        self.servModAceptarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/botones/modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servModAceptarButton.setIcon(icon)
        self.servModAceptarButton.setFlat(True)
        self.servModCancelarButton = QPushButton(servModWindow)
        self.servModCancelarButton.setObjectName(u"servModCancelarButton")
        self.servModCancelarButton.setGeometry(QRect(220, 360, 101, 31))
        self.servModCancelarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.servModCancelarButton.setStyleSheet(u"QPushButton\n"
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
        self.servModCancelarButton.setIcon(icon1)
        self.servModCancelarButton.setFlat(True)
        self.label_5 = QLabel(servModWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 160, 91, 16))
        self.servModPrecioLineEdit = QLineEdit(servModWindow)
        self.servModPrecioLineEdit.setObjectName(u"servModPrecioLineEdit")
        self.servModPrecioLineEdit.setGeometry(QRect(30, 180, 113, 20))

        self.retranslateUi(servModWindow)

        QMetaObject.connectSlotsByName(servModWindow)
    # setupUi

    def retranslateUi(self, servModWindow):
        servModWindow.setWindowTitle(QCoreApplication.translate("servModWindow", u"Modificar Servicio", None))
        self.label.setText(QCoreApplication.translate("servModWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MODIFICAR SERVICIO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("servModWindow", u"<html><head/><body><p>Id. Servicio</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("servModWindow", u"<html><head/><body><p>Titulo:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("servModWindow", u"<html><head/><body><p>Descripci\u00f3n:</p></body></html>", None))
        self.servModAceptarButton.setText(QCoreApplication.translate("servModWindow", u"Modificar", None))
        self.servModCancelarButton.setText(QCoreApplication.translate("servModWindow", u"  Cancelar", None))
        self.label_5.setText(QCoreApplication.translate("servModWindow", u"<html><head/><body><p>Precio Unit. ($):</p></body></html>", None))
    # retranslateUi

