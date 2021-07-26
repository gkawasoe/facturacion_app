from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from views.mod_cliente_window import clienteModWindow
from db.clientes import buscar_clientes_id, actualizar_cliente
import shutil

class ModClienteWindow(QWidget, clienteModWindow):
    # Constructor
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.cargar_inputs()

        # Acción de "Modificar"
        self.clienteModAceptarButton.clicked.connect(self.mod_cliente)

        # Acción de "Cancelar"
        self.clienteModCancelarButton.clicked.connect(self.close)

    def cargar_inputs(self):
        data = buscar_clientes_id(self._id)
        
        self.clienteModLineEdit.setText(data[1])
        self.clienteModCedLineEdit.setText(data[2])
        self.clienteModEmailLineEdit.setText(data[3])
        self.clienteModTelfLineEdit.setText(str(data[4]))
        self.clienteModDirTextEdit.setText(data[5])

    def verf_inputs(self):
        nombre = self.clienteModLineEdit.text()
        rif_ced = self.clienteModCedLineEdit.text()
        
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
            msg.setText('El campo Rif / Cédula es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if errores == 0:
            return True
    
    def mod_cliente(self):
        nombre = self.clienteModLineEdit.text()
        rif_ced = self.clienteModCedLineEdit.text()
        email = self.clienteModEmailLineEdit.text()
        telf = self.clienteModTelfLineEdit.text()
        direccion = self.clienteModDirTextEdit.toPlainText()

        data = [nombre, rif_ced, email, telf, direccion]

        if self.verf_inputs():
            if actualizar_cliente(self._id, data):
                self.parent.refresh_clientes_from_child()
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Cliente actualizado satisfactoriamente')
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.close()


    