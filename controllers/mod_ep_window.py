from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from views.mod_ep_window import epModWindow
from db.ep import buscar_ep_id, actualizar_ep
import shutil

class ModEpWindow(QWidget, epModWindow):
    # Constructor
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.cargar_inputs()

        # Acción de teclear en "Cantidades en Stock"
        self.epModCantLineEdit.textChanged.connect(self.verf_cantidad_stock)

        # Acción de teclear en "Precio Unitario"
        self.epModPrecioLineEdit.textChanged.connect(self.verf_precio_unit)

        # Acción de "Modificar"
        self.epModAceptarButton.clicked.connect(self.mod_ep)

        # Acción de "Cancelar"
        self.epModCancelarButton.clicked.connect(self.close)

    # Función que verifica el tipo de dato ingresado en "Cantidad en Stock"
    def verf_cantidad_stock(self):
        valor = self.epModCantLineEdit.text()
        
        if valor != '':
            if not valor.isnumeric():
                self.epModCantLineEdit.clear()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Solo se aceptan valores númericos enteros en este campo. Favor de verificar')
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

    # Función que verifica el tipo de dato ingresado en "Precio Unit. $"
    def verf_precio_unit(self):
        valor = self.epModPrecioLineEdit.text()
        
        try:
            if valor == '': valor = 0
            valor = float(valor)
        
        except ValueError:
        
            self.epModPrecioLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        
    def cargar_inputs(self):
        data = buscar_ep_id(self._id)
        
        self.idEpModLineEdit.setText(data[1])
        self.epModTituloLineEdit.setText(data[2])
        self.epModCantLineEdit.setText(str(data[3]))
        self.epModPrecioLineEdit.setText(str(data[4]))
        self.epModDescTextEdit.setText(data[5])

    def verf_inputs(self):
        serial = self.idEpModLineEdit.text()
        titulo = self.epModTituloLineEdit.text()
        cantidad = self.epModCantLineEdit.text()
        precio = self.epModPrecioLineEdit.text()
        
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
            msg.setText('El campo Cantidad en Stock en obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if precio == "":
            # print("El campo 'Precio Unit. ($)' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo  Precio Unit. ($) es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if errores == 0:
            return True
    

    def mod_ep(self):
        serial = self.idEpModLineEdit.text()
        titulo = self.epModTituloLineEdit.text()
        cantidad = self.epModCantLineEdit.text()
        precio = self.epModPrecioLineEdit.text()
        descripcion = self.epModDescTextEdit.toPlainText()

        data = [serial, titulo, cantidad, precio.replace(',','.'), descripcion]

        if self.verf_inputs():
            if actualizar_ep(self._id, data):
                self.parent.refresh_ep_from_child()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('El Equipo / Producto ha sido actualizado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.close()


    