from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QLineEdit, QComboBox
from PySide2.QtCore import Qt
from views.mod_presupuesto_window import modPresupuestoWindow
from views.pantalla_principal_window import PantallaPrincipalWindow
from db.presupuesto import mostrar_presupuesto
from db.presupuesto import actualizar_presupuesto, eliminar_presupuesto_detalle, crear_presupuesto_detalle
from db.presupuesto import buscar_presupuesto_id, cargar_renglon, cargar_equipos_combobox, cargar_servicios_combobox, cargar_clientes_combobox
from os import remove
import datetime
import numpy as np
import sys
import shutil
import json
import os

class ModPresupuestoWindow(QWidget, modPresupuestoWindow):
    # Constructor
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)
        self.parent = parent
                
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        vacio = []

        # Crear Archivo .json
        with open(u'./controllers/mod_presupuesto.json','w') as archivo:
            json.dump(vacio, archivo)
        
        self.cargar_inputs()
        
        arreglo = cargar_equipos_combobox(self)
        arreglo2 = ("Productos","Servicios")
        arreglo3 = cargar_clientes_combobox(self)

        self.presupuestoTipoModComboBox.addItem(arreglo2[0])
        self.presupuestoTipoModComboBox.addItem(arreglo2[1])

        i = 0 
        j = 0
        
        # Cargar listdo de "Productos" en el combobox correspondiente
        while i < len(arreglo):
            self.presupuestoProdServModComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][4]))
            i = i + 1
            self.presupuestoProdServModComboBox.setCurrentIndex(0)

        # Cargar listado de "Clientes" en el combobox correspondiente
        while j < len(arreglo3):
            self.presupuestoClienteModComboBox.addItem("Id: " + str(arreglo3[j][0]) + " | RIF / Cédula: " + arreglo3[j][2] + " | Nombre: " + arreglo3[j][1])
            j = j + 1
            self.presupuestoClienteModComboBox.setCurrentIndex(0)

        # Acción de teclear en "Tasa"
        self.presupuestoTasaModLineEdit.textChanged.connect(self.calcular_total)
        
        # Acción de cambiar "Producto / Servicio"
        self.presupuestoTipoModComboBox.activated.connect(self.cambiar_prod_serv)
        
        # Acción de "Agregar"
        self.presupuestoModAddPushButton.clicked.connect(self.cargar_datos_tabla)

        # Acción de "Eliminar"
        self.presupuestoModElimPushButton.clicked.connect(self.eliminar_datos_tabla)

        # Acción de "Modificar"
        self.presupuestoAceptarModPushButton.clicked.connect(self.modificar_presupuesto)
        
        # Acción de "Cancelar"
        self.presupuestoCancelarModPushButton.clicked.connect(self.close)
    
    # Función que carga los datos del "presupuesto" a ser modificado
    def cargar_inputs(self):
        data = buscar_presupuesto_id(self._id)
        data2 = cargar_renglon(self._id)
        monto_bs_total = round(float(data[3]) * float(data[7]),2)
        formato_fecha = "%d/%m/%Y"
        fecha_reg = str(data[4])
        fecha_fin = str(data[5])

        with open(u'./controllers/mod_presupuesto.json','r') as archivo:
            bd = json.load(archivo)

        for record in data2:
            js = {}
            js["id"] = record[2]
            js["tipo"] = record[3]
            js["serial"] = record[4]
            js["titulo"] = record[5]
            js["cantidad"] = record[6]
            js["precio"] = record[7]
            js["monto"] = record[8]

            bd.append(js)
        
        print(fecha_reg)
        
        fecha_reg = datetime.datetime.strptime(fecha_reg, formato_fecha)
        fecha_fin = datetime.datetime.strptime(fecha_fin, formato_fecha)

        self.presupuestoNroModlineEdit.setText(data[1])
        self.presupuestoClienteModComboBox.setCurrentIndex(data[2])
        self.presupuestoTasaModLineEdit.setText(str(data[3]))
        self.presupuestoEmiModDateEdit.setDate(fecha_reg)
        self.presupuestoVencModDateEdit.setDate(fecha_fin)
        self.presupuestoTotDolarModLineEdit.setText(str(data[7]))
        self.presupuestoTotBsModLineEdit.setText(str(monto_bs_total))

        #Rellenar la tabla interna de la vista "Modificar Presupuesto"
        data3 = []
        
        for vector in bd:
            data4 = (vector['id'], vector['tipo'], vector['serial'], vector['titulo'], vector['cantidad'], vector['precio'], vector['monto'])
            data3.append(data4)
        
        #Registrar los datos en el archivo JSON "mod_presupuesto.json"
        with open(u'./controllers/mod_presupuesto.json','w') as archivo:
            json.dump(bd, archivo)

        self.table_config_mod_presupuesto()
        
        self.presupuestoModTableWidget.setRowCount(len(data3))

        for (index_row, row) in enumerate(data3):
            for (index_cell, cell) in enumerate(row):
                self.presupuestoModTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        
    
    # Función que modifica el ComboBox de "Producto / Servicio"
    def cambiar_prod_serv(self):
        opc_capt = self.presupuestoTipoModComboBox.currentText()
        
        if opc_capt == 'Productos':
            arreglo = cargar_equipos_combobox(self)
            i = 0

            # Limpiar el Combobox de "Producto / Servicio"
            self.presupuestoProdServModComboBox.clear()

            # Cargar listdo de "Productos" en el combobox correspondiente
            while i < len(arreglo):
                self.presupuestoProdServModComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][4]))
                i = i + 1
                self.presupuestoProdServModComboBox.setCurrentIndex(0)
        
        if opc_capt == 'Servicios':
            arreglo = cargar_servicios_combobox(self)
            i = 0

            # Limpiar el Combobox de "Producto / Servicio"
            self.presupuestoProdServModComboBox.clear()

            # Cargar listdo de "Servicios" en el combobox correspondiente
            while i < len(arreglo):
                self.presupuestoProdServModComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][3]))
                i = i + 1
                self.presupuestoProdServModComboBox.setCurrentIndex(0)

    # Función que verifica el input de "Tasa"
    def verf_tasa(self):
        valor = self.presupuestoTasaModLineEdit.text()
        bandera = False
        try:
            if valor == '': valor = 0

            valor = float(valor)
            
            bandera = True

        except ValueError:
        
            self.presupuestoTasaModLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        finally:

            return bandera
    
    # Función que calcula el total en Bolívares
    def calcular_total(self):
        tasa_capt = self.presupuestoTasaModLineEdit.text()
        total_dol_capt = self.presupuestoTotDolarModLineEdit.text()

        if self.verf_tasa():
            if total_dol_capt != '' and tasa_capt != '':
                total_bs = float(tasa_capt) * float(total_dol_capt)
                self.presupuestoTotBsModLineEdit.setText(str(round(total_bs,2)))

    # Función que verifica los campos en esta vista
    def verf_inputs(self):
        nro_presupuesto = self.presupuestoNroModlineEdit.text()
        tasa = self.presupuestoTasaModLineEdit.text()
        
        with open(u'./controllers/mod_presupuesto.json','r') as archivo:
            bd = json.load(archivo)
        
        renglones = bd
        
        errores = 0

        if nro_presupuesto == "":
            # print("El campo 'Serial' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Nro. Presupuesto es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if tasa == "":
            # print("El campo 'Titulo' es obligatorio")
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('El campo Tasa es obligatorio')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if not renglones:
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('Debe agregar mínimo 1 Item de Productos / Servicios')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            errores += 1

        if errores == 0:
            return True

    def modificar_presupuesto(self):
        nro_presupuesto = self.presupuestoNroModlineEdit.text()
        tasa = self.presupuestoTasaModLineEdit.text()
        fecha_inicio = self.presupuestoEmiModDateEdit.text()
        fecha_fin = self.presupuestoVencModDateEdit.text()
        cliente = self.presupuestoClienteModComboBox.currentText()
        sub_cad = ' |'
        
        # Proceso que encuentra una sub-cadena
        pos_index = 0
        pos = 0

        while pos != -1:
            pos = cliente.find(sub_cad, pos)
            if pos != -1:
                pos_index = pos
                pos = -1

        # Fin del proceso

        id_cliente = cliente[4:pos_index]

        with open(u'./controllers/mod_presupuesto.json','r') as archivo:
            bd = json.load(archivo)
        
        renglones = bd
        monto_total = self.presupuestoTotDolarModLineEdit.text()
        
        if self.verf_inputs():
            data = (nro_presupuesto, int(id_cliente), round(float(tasa),2), str(fecha_inicio), str(fecha_fin), str(renglones), monto_total)

            if actualizar_presupuesto(self._id,data):
                if eliminar_presupuesto_detalle(self._id):

                    for vector in bd:
                        data2 = (self._id, int(str(vector['id'])), str(vector['tipo']), str(vector['serial']), str(vector['titulo']), int(str(vector['cantidad'])), float(str(vector['precio'])), float(str(vector['monto'])))
                        crear_presupuesto_detalle(data2)

                    self.limpiar_inputs()
                    self.parent.refresh_prespuesto_from_child() 

                    # Crear Archivo .json
                    vacio = []
                    with open(u'./controllers/mod_presupuesto.json','w') as archivo:
                        json.dump(vacio, archivo)

                    msg = QMessageBox()
                    msg.setWindowTitle('SISTEMA')
                    msg.setText('Presupuesto modificado satisfactoriamente')
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
    # Limpiar Inputs o Campos de esta vista                
    def limpiar_inputs(self):
        self.presupuestoNroModlineEdit.clear()
        self.presupuestoTasaModLineEdit.clear()
        self.presupuestoClienteModComboBox.clearFocus()
        self.presupuestoTotDolarModLineEdit.clear()
        self.presupuestoTotBsModLineEdit.clear()
        self.presupuestoCantModLineEdit.clear()
        
        # Eliminar Datos de la tabla interna de la vista "Nuevo Presupuesto"
        while(self.presupuestoModTableWidget.rowCount() > 0):
            self.presupuestoModTableWidget.removeRow(0)
        
        self.presupuestoModTableWidget.reset()

        #Eliminar el archivo "mod_presupuesto.json"
        remove("./controllers/mod_presupuesto.json")
    
    # Configurar tabla de "Nuevo Presupuesto"
    def table_config_mod_presupuesto(self):
        column_headers = ("Id","Tipo","Serial","Titulo", "Cantidad", "Precio Unit. ($)","Monto ($)")
        self.presupuestoModTableWidget.setColumnCount(len(column_headers))     
        self.presupuestoModTableWidget.setHorizontalHeaderLabels(column_headers)

        self.presupuestoModTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # Función que recarga la tabla interna de la vista de "Nuevo Presupuesto"
    def refresh_mod_presupuesto_table(self):
        data3 = []
        cont = 0
        total_dol = 0
        tasa = self.presupuestoTasaModLineEdit.text()
        
        with open(u'./controllers/mod_presupuesto.json','r') as archivo:
            bd = json.load(archivo)
        
        for vector in bd:
            data2 = (vector['id'], vector['tipo'], vector['serial'], vector['titulo'], vector['cantidad'], vector['precio'], vector['monto'])
            total_dol = total_dol + (float(vector['monto']))
            data3.append(data2)
        
        self.table_config_mod_presupuesto()
        
        
        self.presupuestoModTableWidget.setRowCount(len(data3))
        
        for (index_row, row) in enumerate(data3):
            for (index_cell, cell) in enumerate(row):
                self.presupuestoModTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        # Colocar el monto en dolares en dicho Line Edit
        self.presupuestoTotDolarModLineEdit.setText(str(total_dol))

        # Colocar el monto en Bolívares en dicho Line Edit
        if tasa != '':
            calculo = float(tasa) * total_dol
            self.presupuestoTotBsModLineEdit.setText(str(calculo))
    
    # Función que ingresa un "Producto / Servicio" en la tabla de "Presupuestos"
    def cargar_datos_tabla(self):
        indice = self.presupuestoProdServModComboBox.currentIndex()
        valor = self.presupuestoProdServModComboBox.itemText(indice)
        cantidad = self.presupuestoCantModLineEdit.text()
        tasa = self.presupuestoTasaModLineEdit.text()
        tipo = self.presupuestoTipoModComboBox.currentText()
        cadena = valor.split(" - ")
        id_pre = cadena[0]
        cadena2 = cadena[1].split(" | ")
        serial = cadena2[0]
        texto = cadena2[1]
        precio = cadena2[2]
        bandera = False
       
        with open(u'./controllers/mod_presupuesto.json','r') as archivo:
            bd = json.load(archivo)

        # Verificar si el nuevo "serial" del nuevo Item a ingresar ya existe en el JSON
        for i in range(len(bd)):
            if bd[i]['serial'] == serial:
                bandera = True


        if cantidad != '':       
            if not bandera:
                monto = float(precio) * int(self.presupuestoCantModLineEdit.text())
                nuevo_reg = {'id':id_pre, 'tipo':tipo, 'serial':serial, 'titulo':texto, 'cantidad':cantidad, 'precio':precio, 'monto_sub':monto}
                
                js = {}
                js["id"] = id_pre
                js["tipo"] = tipo
                js["serial"] = serial
                js["titulo"] = texto
                js["cantidad"] = cantidad
                js["precio"] = precio
                js["monto"] = monto

                bd.append(js)

                with open(u'./controllers/mod_presupuesto.json','w') as archivo:
                    json.dump(bd, archivo)

                data3 = []
                cont = 0
                total_dol = 0
                
                for vector in bd:
                    data2 = (vector['id'], vector['tipo'], vector['serial'], vector['titulo'], vector['cantidad'], vector['precio'], vector['monto'])
                    total_dol = total_dol + (float(vector['monto']))
                    data3.append(data2)
                
                self.table_config_mod_presupuesto()
                
                
                self.presupuestoModTableWidget.setRowCount(len(data3))
                
                for (index_row, row) in enumerate(data3):
                    for (index_cell, cell) in enumerate(row):
                        self.presupuestoModTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
                # Colocar el monto en dolares en dicho Line Edit
                self.presupuestoTotDolarModLineEdit.setText(str(total_dol))

                # Colocar el monto en Bolívares en dicho Line Edit
                if tasa != '':
                    calculo = float(tasa) * total_dol
                    self.presupuestoTotBsModLineEdit.setText(str(round(calculo,2)))

            else:
                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Ya existe un Item con este serial agregado, favor de verificar')
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Debe colocar una cantidad correcta para adicionar el Item')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    # Eliminar un Item del archivo JSON "mod_presupuesto.json"
    def eliminar_item(self, ident):
       index_capt2 = 0
       i = 0
        
       with open(u'./controllers/mod_presupuesto.json','r') as archivo:
        bd = json.load(archivo)

        lista = list(bd)
        arreglo = np.array(lista)
        
        for i in range(len(bd)):
            if bd[i]['serial'] == str(ident):
                index_capt2 = i
                i = len(bd)
        
        bd.pop(int(index_capt2))
    
        with open(u'./controllers/mod_presupuesto.json','w') as archivo:
            json.dump(bd, archivo)
       
       return True
               

    # Función que elimina Items de la tabla interna
    def eliminar_datos_tabla(self):
        
        # Obtener el id seleccionado desde la tabla
        selected_row = self.presupuestoModTableWidget.selectedItems()

        if selected_row:
            item_id = str(selected_row[1].text())
            bandera = self.eliminar_item(item_id)

            if bandera:
                self.refresh_mod_presupuesto_table()

