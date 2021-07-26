from PySide2.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt
from views.pantalla_principal_window import PantallaPrincipalWindow
from views.nuevo_ep_window import epRegWindow
from db.ep import mostrar_ep
from db.ep import crear_ep
import shutil

class NuevoEpWindow(QWidget, epRegWindow, PantallaPrincipalWindow):
    # Constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        #Esto es para atrapar a la clase padre que fue capturado en "pantalla_principal_window"
        self.parent = parent 
        
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        # Acción de teclear en "Cantidades en Stock"
        self.epRegCantLineEdit.textChanged.connect(self.verf_cantidad_stock)
        
        # Acción de teclear en "Precio Unitario"
        self.epRegPrecioLineEdit.textChanged.connect(self.verf_precio_unit)

        # Acción de "Aceptar"
        self.epRegAceptarButton.clicked.connect(self.agregar_ep)

        # Acción de "Cancelar"
        self.epRegCancelarButton.clicked.connect(self.close)
    
    # Función que verifica el tipo de dato ingresado en "Precio Unit. $"
    def verf_precio_unit(self):
        valor = self.epRegPrecioLineEdit.text()
        
        try:
            if valor == '': valor = 0

            valor = float(valor)
        
        except ValueError:
        
            self.epRegPrecioLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    # Función que verifica el tipo de dato ingresado en "Cantidad en Stock"
    def verf_cantidad_stock(self):
        valor = self.epRegCantLineEdit.text()
        
        if valor != '':
            if not valor.isnumeric():
                self.epRegCantLineEdit.clear()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Solo se aceptan valores númericos enteros en este campo. Favor de verificar')
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

    def verf_inputs(self):
        serial = self.idEpRegLineEdit.text()
        titulo = self.epRegTituloLineEdit.text()
        cantidad = self.epRegCantLineEdit.text()
        precio = self.epRegPrecioLineEdit.text()
        
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

        if cantidad == "":
            # print("El campo 'Cantidad en Stock' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Cantidad en Stock es obligatorio')
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

    def agregar_ep(self):
        serial = self.idEpRegLineEdit.text()
        titulo = self.epRegTituloLineEdit.text()
        cantidad = self.epRegCantLineEdit.text()
        precio = self.epRegPrecioLineEdit.text()
        descripcion = self.epRegDescTextEdit.toPlainText()
        
        if self.verf_inputs():
            data = (serial, titulo, cantidad, precio.replace(',','.'), descripcion)

            if crear_ep(data):
                self.limpiar_inputs()
                self.parent.refresh_ep_from_child() 
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Equipo / Producto creado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
    
    def limpiar_inputs(self):
        self.idEpRegLineEdit.clear()
        self.epRegTituloLineEdit.clear()
        self.epRegCantLineEdit.clear()
        self.epRegPrecioLineEdit.clear()
        self.epRegDescTextEdit.clear()