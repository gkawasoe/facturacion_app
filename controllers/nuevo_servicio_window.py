from PySide2.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt
from views.pantalla_principal_window import PantallaPrincipalWindow
from views.nuevo_serv_window import servRegWindow
from db.servicios import mostrar_serv
from db.servicios import crear_serv
import shutil

class NuevoServWindow(QWidget, servRegWindow, PantallaPrincipalWindow):
    # Constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        #Esto es para atrapar a la clase padre que fue capturado en "pantalla_principal_window"
        self.parent = parent 
        
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        # Acción de teclear en "Precio Unit. $"
        self.servRegPrecioLineEdit.textChanged.connect(self.verf_precio_unit)

        # Acción de "Aceptar"
        self.servRegAceptarButton.clicked.connect(self.agregar_serv)
        
        # Acción de "Cancelar"
        self.servRegCancelarButton.clicked.connect(self.close)
    
    # Funcion que verifica el input en "Precio Unit. $"
    def verf_precio_unit(self):
        valor = self.servRegPrecioLineEdit.text()
        
        try:
            if valor == '': valor = 0
            
            valor = float(valor)
        
        except ValueError:
        
            self.servRegPrecioLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def verf_inputs(self):
        serial = self.idServRegLineEdit.text()
        titulo = self.servRegTituloLineEdit.text()
        precio = self.servRegPrecioLineEdit.text()
        
        errores = 0

        if serial == "":
            # print("El campo 'Serial' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Serial es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if titulo == "":
            # print("El campo 'Titulo' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Titulo es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()  
            errores += 1

        if precio == "":
            # print("El campo 'Precio Unit. ($)' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Precio Unit. ($) es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if errores == 0:
            return True

    def agregar_serv(self):
        serial = self.idServRegLineEdit.text()
        titulo = self.servRegTituloLineEdit.text()
        precio = self.servRegPrecioLineEdit.text()
        descripcion = self.servRegDescTextEdit.toPlainText()
        
        if self.verf_inputs():
            data = (serial, titulo, precio.replace(',','.'), descripcion)

            if crear_serv(data):
                self.limpiar_inputs()
                self.parent.refresh_serv_from_child()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Servicio creado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_() 
                
    def limpiar_inputs(self):
        self.idServRegLineEdit.clear()
        self.servRegTituloLineEdit.clear()
        self.servRegPrecioLineEdit.clear()
        self.servRegDescTextEdit.clear()

    