# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_principal_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PantallaPrincipalWindow(object):
    def setupUi(self, PantallaPrincipalWindow):
        if not PantallaPrincipalWindow.objectName():
            PantallaPrincipalWindow.setObjectName(u"PantallaPrincipalWindow")
        PantallaPrincipalWindow.resize(962, 550)
        icon = QIcon()
        icon.addFile(u"./assets/icons/logo_empresa.jpg", QSize(), QIcon.Normal, QIcon.Off)
        PantallaPrincipalWindow.setWindowIcon(icon)
        self.tabWidget = QTabWidget(PantallaPrincipalWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 941, 531))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.clienteBotonFrame = QFrame(self.tab)
        self.clienteBotonFrame.setObjectName(u"clienteBotonFrame")
        self.clienteBotonFrame.setGeometry(QRect(10, 10, 912, 91))
        self.clienteBotonFrame.setFrameShape(QFrame.StyledPanel)
        self.clienteBotonFrame.setFrameShadow(QFrame.Raised)
        self.clienteRegBoton = QPushButton(self.clienteBotonFrame)
        self.clienteRegBoton.setObjectName(u"clienteRegBoton")
        self.clienteRegBoton.setGeometry(QRect(20, 10, 71, 51))
        self.clienteRegBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clienteRegBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/clientes/nuevo cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteRegBoton.setIcon(icon1)
        self.clienteRegBoton.setIconSize(QSize(50, 50))
        self.clienteRegBoton.setFlat(True)
        self.label = QLabel(self.clienteBotonFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 91, 16))
        self.label_2 = QLabel(self.clienteBotonFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 70, 101, 16))
        self.clienteModBoton = QPushButton(self.clienteBotonFrame)
        self.clienteModBoton.setObjectName(u"clienteModBoton")
        self.clienteModBoton.setGeometry(QRect(150, 10, 71, 51))
        self.clienteModBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clienteModBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/clientes/modificar cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteModBoton.setIcon(icon2)
        self.clienteModBoton.setIconSize(QSize(50, 50))
        self.clienteModBoton.setFlat(True)
        self.label_3 = QLabel(self.clienteBotonFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 70, 91, 16))
        self.clienteElimBoton = QPushButton(self.clienteBotonFrame)
        self.clienteElimBoton.setObjectName(u"clienteElimBoton")
        self.clienteElimBoton.setGeometry(QRect(290, 10, 71, 51))
        self.clienteElimBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clienteElimBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/clientes/eliminar cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteElimBoton.setIcon(icon3)
        self.clienteElimBoton.setIconSize(QSize(50, 50))
        self.clienteElimBoton.setFlat(True)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 911, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 61, 16))
        self.clienteBusComboBox = QComboBox(self.frame)
        self.clienteBusComboBox.setObjectName(u"clienteBusComboBox")
        self.clienteBusComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.clienteBusLineEdit = QLineEdit(self.frame)
        self.clienteBusLineEdit.setObjectName(u"clienteBusLineEdit")
        self.clienteBusLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.clienteBusBoton = QPushButton(self.frame)
        self.clienteBusBoton.setObjectName(u"clienteBusBoton")
        self.clienteBusBoton.setGeometry(QRect(660, 10, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/botones/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clienteBusBoton.setIcon(icon4)
        self.clienteBusBoton.setIconSize(QSize(30, 30))
        self.clienteTabla = QTableWidget(self.tab)
        self.clienteTabla.setObjectName(u"clienteTabla")
        self.clienteTabla.setGeometry(QRect(10, 160, 911, 311))
        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 480, 611, 21))
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.clienteBotonFrame_2 = QFrame(self.tab_3)
        self.clienteBotonFrame_2.setObjectName(u"clienteBotonFrame_2")
        self.clienteBotonFrame_2.setGeometry(QRect(10, 10, 912, 91))
        self.clienteBotonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.clienteBotonFrame_2.setFrameShadow(QFrame.Raised)
        self.equipoRegBoton = QPushButton(self.clienteBotonFrame_2)
        self.equipoRegBoton.setObjectName(u"equipoRegBoton")
        self.equipoRegBoton.setGeometry(QRect(20, 10, 71, 51))
        self.equipoRegBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.equipoRegBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/equipos_productos/nuevo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.equipoRegBoton.setIcon(icon5)
        self.equipoRegBoton.setIconSize(QSize(50, 50))
        self.equipoRegBoton.setFlat(True)
        self.label_5 = QLabel(self.clienteBotonFrame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 101, 16))
        self.label_6 = QLabel(self.clienteBotonFrame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(135, 70, 111, 16))
        self.equipoModBoton = QPushButton(self.clienteBotonFrame_2)
        self.equipoModBoton.setObjectName(u"equipoModBoton")
        self.equipoModBoton.setGeometry(QRect(150, 10, 71, 51))
        self.equipoModBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.equipoModBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/equipos_productos/modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.equipoModBoton.setIcon(icon6)
        self.equipoModBoton.setIconSize(QSize(50, 50))
        self.equipoModBoton.setFlat(True)
        self.label_7 = QLabel(self.clienteBotonFrame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 70, 101, 16))
        self.equipoElimBoton = QPushButton(self.clienteBotonFrame_2)
        self.equipoElimBoton.setObjectName(u"equipoElimBoton")
        self.equipoElimBoton.setGeometry(QRect(290, 10, 71, 51))
        self.equipoElimBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.equipoElimBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/equipos_productos/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.equipoElimBoton.setIcon(icon7)
        self.equipoElimBoton.setIconSize(QSize(50, 50))
        self.equipoElimBoton.setFlat(True)
        self.equipoTabla = QTableWidget(self.tab_3)
        self.equipoTabla.setObjectName(u"equipoTabla")
        self.equipoTabla.setGeometry(QRect(10, 160, 911, 311))
        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 110, 911, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 61, 16))
        self.equipoBusComboBox = QComboBox(self.frame_2)
        self.equipoBusComboBox.setObjectName(u"equipoBusComboBox")
        self.equipoBusComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.equipoBusLineEdit = QLineEdit(self.frame_2)
        self.equipoBusLineEdit.setObjectName(u"equipoBusLineEdit")
        self.equipoBusLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.equipoBusBoton = QPushButton(self.frame_2)
        self.equipoBusBoton.setObjectName(u"equipoBusBoton")
        self.equipoBusBoton.setGeometry(QRect(660, 10, 131, 25))
        self.equipoBusBoton.setIcon(icon4)
        self.equipoBusBoton.setIconSize(QSize(30, 30))
        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 480, 611, 21))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.clienteBotonFrame_3 = QFrame(self.tab_2)
        self.clienteBotonFrame_3.setObjectName(u"clienteBotonFrame_3")
        self.clienteBotonFrame_3.setGeometry(QRect(10, 10, 912, 91))
        self.clienteBotonFrame_3.setFrameShape(QFrame.StyledPanel)
        self.clienteBotonFrame_3.setFrameShadow(QFrame.Raised)
        self.servicioRegBoton = QPushButton(self.clienteBotonFrame_3)
        self.servicioRegBoton.setObjectName(u"servicioRegBoton")
        self.servicioRegBoton.setGeometry(QRect(20, 10, 71, 51))
        self.servicioRegBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.servicioRegBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"./assets/icons/servicios/nuevo servicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servicioRegBoton.setIcon(icon8)
        self.servicioRegBoton.setIconSize(QSize(50, 50))
        self.servicioRegBoton.setFlat(True)
        self.label_9 = QLabel(self.clienteBotonFrame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 70, 91, 16))
        self.label_10 = QLabel(self.clienteBotonFrame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 70, 101, 16))
        self.servicioModBoton = QPushButton(self.clienteBotonFrame_3)
        self.servicioModBoton.setObjectName(u"servicioModBoton")
        self.servicioModBoton.setGeometry(QRect(150, 10, 71, 51))
        self.servicioModBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.servicioModBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"./assets/icons/servicios/modificar servicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servicioModBoton.setIcon(icon9)
        self.servicioModBoton.setIconSize(QSize(50, 50))
        self.servicioModBoton.setFlat(True)
        self.label_11 = QLabel(self.clienteBotonFrame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 70, 101, 16))
        self.servicioElimBoton = QPushButton(self.clienteBotonFrame_3)
        self.servicioElimBoton.setObjectName(u"servicioElimBoton")
        self.servicioElimBoton.setGeometry(QRect(290, 10, 71, 51))
        self.servicioElimBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.servicioElimBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"./assets/icons/servicios/cancelar servicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servicioElimBoton.setIcon(icon10)
        self.servicioElimBoton.setIconSize(QSize(50, 50))
        self.servicioElimBoton.setFlat(True)
        self.servicioTabla = QTableWidget(self.tab_2)
        self.servicioTabla.setObjectName(u"servicioTabla")
        self.servicioTabla.setGeometry(QRect(10, 160, 911, 311))
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 110, 911, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 61, 16))
        self.servicioBusComboBox = QComboBox(self.frame_3)
        self.servicioBusComboBox.setObjectName(u"servicioBusComboBox")
        self.servicioBusComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.servicioBusLineEdit = QLineEdit(self.frame_3)
        self.servicioBusLineEdit.setObjectName(u"servicioBusLineEdit")
        self.servicioBusLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.servicioBusBoton = QPushButton(self.frame_3)
        self.servicioBusBoton.setObjectName(u"servicioBusBoton")
        self.servicioBusBoton.setGeometry(QRect(660, 10, 131, 25))
        self.servicioBusBoton.setIcon(icon4)
        self.servicioBusBoton.setIconSize(QSize(30, 30))
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(170, 480, 611, 21))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.clienteBotonFrame_4 = QFrame(self.tab_4)
        self.clienteBotonFrame_4.setObjectName(u"clienteBotonFrame_4")
        self.clienteBotonFrame_4.setGeometry(QRect(10, 10, 912, 91))
        self.clienteBotonFrame_4.setFrameShape(QFrame.StyledPanel)
        self.clienteBotonFrame_4.setFrameShadow(QFrame.Raised)
        self.presupuestoRegBoton = QPushButton(self.clienteBotonFrame_4)
        self.presupuestoRegBoton.setObjectName(u"presupuestoRegBoton")
        self.presupuestoRegBoton.setGeometry(QRect(20, 10, 71, 51))
        self.presupuestoRegBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.presupuestoRegBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"./assets/icons/presupuestos/nuevo presupuesto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.presupuestoRegBoton.setIcon(icon11)
        self.presupuestoRegBoton.setIconSize(QSize(50, 50))
        self.presupuestoRegBoton.setFlat(True)
        self.label_13 = QLabel(self.clienteBotonFrame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 70, 121, 16))
        self.label_14 = QLabel(self.clienteBotonFrame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 70, 131, 16))
        self.presupuestoModBoton = QPushButton(self.clienteBotonFrame_4)
        self.presupuestoModBoton.setObjectName(u"presupuestoModBoton")
        self.presupuestoModBoton.setGeometry(QRect(150, 10, 71, 51))
        self.presupuestoModBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.presupuestoModBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"./assets/icons/presupuestos/modificar presupuesto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.presupuestoModBoton.setIcon(icon12)
        self.presupuestoModBoton.setIconSize(QSize(50, 50))
        self.presupuestoModBoton.setFlat(True)
        self.label_15 = QLabel(self.clienteBotonFrame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 70, 131, 16))
        self.presupuestoElimBoton = QPushButton(self.clienteBotonFrame_4)
        self.presupuestoElimBoton.setObjectName(u"presupuestoElimBoton")
        self.presupuestoElimBoton.setGeometry(QRect(290, 10, 71, 51))
        self.presupuestoElimBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.presupuestoElimBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"./assets/icons/presupuestos/eliminar presupuesto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.presupuestoElimBoton.setIcon(icon13)
        self.presupuestoElimBoton.setIconSize(QSize(50, 50))
        self.presupuestoElimBoton.setFlat(True)
        self.presupuestoImpBoton = QPushButton(self.clienteBotonFrame_4)
        self.presupuestoImpBoton.setObjectName(u"presupuestoImpBoton")
        self.presupuestoImpBoton.setGeometry(QRect(430, 10, 71, 51))
        self.presupuestoImpBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.presupuestoImpBoton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"./assets/icons/presupuestos/imprimir presupuesto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.presupuestoImpBoton.setIcon(icon14)
        self.presupuestoImpBoton.setIconSize(QSize(50, 50))
        self.presupuestoImpBoton.setFlat(True)
        self.label_17 = QLabel(self.clienteBotonFrame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(410, 70, 131, 16))
        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 110, 911, 41))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 61, 16))
        self.presupuestoBusComboBox = QComboBox(self.frame_4)
        self.presupuestoBusComboBox.setObjectName(u"presupuestoBusComboBox")
        self.presupuestoBusComboBox.setGeometry(QRect(70, 10, 161, 22))
        self.presupuestoBusLineEdit = QLineEdit(self.frame_4)
        self.presupuestoBusLineEdit.setObjectName(u"presupuestoBusLineEdit")
        self.presupuestoBusLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.presupuestoBusBoton = QPushButton(self.frame_4)
        self.presupuestoBusBoton.setObjectName(u"presupuestoBusBoton")
        self.presupuestoBusBoton.setGeometry(QRect(660, 10, 131, 25))
        self.presupuestoBusBoton.setIcon(icon4)
        self.presupuestoBusBoton.setIconSize(QSize(30, 30))
        self.presupuestoTabla = QTableWidget(self.tab_4)
        self.presupuestoTabla.setObjectName(u"presupuestoTabla")
        self.presupuestoTabla.setGeometry(QRect(10, 160, 911, 311))
        self.label_18 = QLabel(self.tab_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 480, 611, 21))
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(PantallaPrincipalWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PantallaPrincipalWindow)
    # setupUi

    def retranslateUi(self, PantallaPrincipalWindow):
        PantallaPrincipalWindow.setWindowTitle(QCoreApplication.translate("PantallaPrincipalWindow", u"Sistema de Facturaci\u00f3n - Tecno Servicios A.J. Rojas", None))
        self.clienteRegBoton.setText("")
        self.label.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Cliente</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modificar Cliente</span></p></body></html>", None))
        self.clienteModBoton.setText("")
        self.label_3.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Cliente</span></p></body></html>", None))
        self.clienteElimBoton.setText("")
        self.label_4.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p>Buscar por:</p></body></html>", None))
        self.clienteBusBoton.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"BUSCAR", None))
        self.label_19.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aplicaci\u00f3n Dise\u00f1ada y Elaborada por:</span><span style=\" font-size:10pt;\"> Goichi Kawasoe Hern\u00e1ndez / </span><span style=\" font-size:10pt; font-weight:600;\">Email: </span><span style=\" font-size:10pt;\">gkawasoe@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PantallaPrincipalWindow", u"Clientes", None))
        self.equipoRegBoton.setText("")
        self.label_5.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Producto</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modificar Producto</span></p></body></html>", None))
        self.equipoModBoton.setText("")
        self.label_7.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Producto</span></p></body></html>", None))
        self.equipoElimBoton.setText("")
        self.label_8.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p>Buscar por:</p></body></html>", None))
        self.equipoBusBoton.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"BUSCAR", None))
        self.label_20.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aplicaci\u00f3n Dise\u00f1ada y Elaborada por:</span><span style=\" font-size:10pt;\"> Goichi Kawasoe Hern\u00e1ndez / </span><span style=\" font-size:10pt; font-weight:600;\">Email: </span><span style=\" font-size:10pt;\">gkawasoe@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("PantallaPrincipalWindow", u"Equipos / Productos", None))
        self.servicioRegBoton.setText("")
        self.label_9.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Servicio</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modificar Servicio</span></p></body></html>", None))
        self.servicioModBoton.setText("")
        self.label_11.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Servicio</span></p></body></html>", None))
        self.servicioElimBoton.setText("")
        self.label_12.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p>Buscar por:</p></body></html>", None))
        self.servicioBusBoton.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"BUSCAR", None))
        self.label_21.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aplicaci\u00f3n Dise\u00f1ada y Elaborada por:</span><span style=\" font-size:10pt;\"> Goichi Kawasoe Hern\u00e1ndez / </span><span style=\" font-size:10pt; font-weight:600;\">Email: </span><span style=\" font-size:10pt;\">gkawasoe@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PantallaPrincipalWindow", u"Servicios", None))
        self.presupuestoRegBoton.setText("")
        self.label_13.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Presupuesto</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modificar Presupuesto</span></p></body></html>", None))
        self.presupuestoModBoton.setText("")
        self.label_15.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Presupuesto</span></p></body></html>", None))
        self.presupuestoElimBoton.setText("")
        self.presupuestoImpBoton.setText("")
        self.label_17.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Imprimir Presupuesto</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p>Buscar por:</p></body></html>", None))
        self.presupuestoBusBoton.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"BUSCAR", None))
        self.label_18.setText(QCoreApplication.translate("PantallaPrincipalWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aplicaci\u00f3n Dise\u00f1ada y Elaborada por:</span><span style=\" font-size:10pt;\"> Goichi Kawasoe Hern\u00e1ndez / </span><span style=\" font-size:10pt; font-weight:600;\">Email: </span><span style=\" font-size:10pt;\">gkawasoe@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("PantallaPrincipalWindow", u"Presupuestos", None))
    # retranslateUi

