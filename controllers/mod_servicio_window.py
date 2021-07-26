from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from views.mod_serv_window import servModWindow
from db.servicios import buscar_serv_id, actualizar_serv
import shutil

class ModServWindow(QWidget, servModWindow):
    # Constructor
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.cargar_inputs()

        # Acción de teclear en "Precio Unit. $"
        self.servModPrecioLineEdit.textChanged.connect(self.verf_precio_unit)

        # Acción de "Modificar"
        self.servModAceptarButton.clicked.connect(self.mod_serv)
        
        # Acción de "Cancelar"
        self.servModCancelarButton.clicked.connect(self.close)

    # Funcion que verifica el input en "Precio Unit. $"
    def verf_precio_unit(self):
        valor = self.servModPrecioLineEdit.text()
        
        try:
            if valor == '': valor = 0

            valor = float(valor)
        
        except ValueError:
        
            self.servModPrecioLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def cargar_inputs(self):
        data = buscar_serv_id(self._id)
        
        self.idServModLineEdit.setText(data[1])
        self.servModTituloLineEdit.setText(data[2])
        self.servModPrecioLineEdit.setText(str(data[3]))
        self.servModDescTextEdit.setText(data[4])
        
    def verf_inputs(self):
        serial = self.idServModLineEdit.text()
        titulo = self.servModTituloLineEdit.text()
        precio = self.servModPrecioLineEdit.text()
        
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
    
    def mod_serv(self):
        serial = self.idServModLineEdit.text()
        titulo = self.servModTituloLineEdit.text()
        precio = self.servModPrecioLineEdit.text()
        descripcion = self.servModDescTextEdit.toPlainText()

        data = [serial, titulo, precio.replace(',','.'), descripcion]

        if self.verf_inputs():
            if actualizar_serv(self._id, data):
                self.parent.refresh_serv_from_child()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Servicio actualizado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.close()


    