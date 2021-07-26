from PySide2.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt
from views.pantalla_principal_window import PantallaPrincipalWindow
from views.nuevo_cliente_window import clienteRegWindow
from db.clientes import mostrar_clientes
from db.clientes import crear_cliente
import shutil

class NuevoClienteWindow(QWidget, clienteRegWindow, PantallaPrincipalWindow):
    # Constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        #Esto es para atrapar a la clase padre que fue capturado en "pantalla_principal_window"
        self.parent = parent 
        
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        # Acción de "Aceptar"
        self.clienteRegAceptarButton.clicked.connect(self.agregar_cliente)
        # Acción de "Cancelar"
        self.clienteRegCancelarButton.clicked.connect(self.close)
    
    def verf_inputs(self):
        nombre = self.clienteRegLineEdit.text()
        rif_ced = self.clienteRegCedLineEdit.text()
        
        errores = 0

        if nombre == "":
            # print("El campo 'Nombre' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Nombre es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if rif_ced == "":
            # print("El campo 'RIF / Cédula' es obligatorio") 
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo RIF / Cédula es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if errores == 0:
            return True

    def agregar_cliente(self):
        nombre = self.clienteRegLineEdit.text()
        rif_ced = self.clienteRegCedLineEdit.text()
        email = self.clienteRegEmailLineEdit.text()
        telf = self.clienteRegTelfLineEdit.text()
        direccion = self.clienteRegDirTextEdit.toPlainText()

        if self.verf_inputs():
            data = (nombre, rif_ced, email, telf, direccion)

            if crear_cliente(data):
                self.limpiar_inputs()
                self.parent.refresh_clientes_from_child()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Cliente creado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_() 
                
    def limpiar_inputs(self):
        self.clienteRegLineEdit.clear()
        self.clienteRegCedLineEdit.clear()
        self.clienteRegEmailLineEdit.clear()
        self.clienteRegTelfLineEdit.clear()
        self.clienteRegDirTextEdit.clear()
    