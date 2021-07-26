from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QLineEdit, QComboBox
from PySide2.QtCore import Qt
from views.nuevo_presupuesto_window import nuevoPresupuestoWindow
from views.pantalla_principal_window import PantallaPrincipalWindow
from db.presupuesto import mostrar_presupuesto
from db.presupuesto import crear_presupuesto, buscar_max_id, crear_presupuesto_detalle
from db.presupuesto import cargar_equipos_combobox, cargar_servicios_combobox, cargar_clientes_combobox
from os import remove
import numpy as np
import sys
import shutil
import json
import os

class NuevoPresupuestoWindow(QWidget, nuevoPresupuestoWindow, PantallaPrincipalWindow):
    # Constructor
    def __init__(self, parent=None):
        super().__init__(parent)
        #Esto es para atrapar a la clase padre que fue capturado en "pantalla_principal_window"
        self.parent = parent 
                
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        arreglo = cargar_equipos_combobox(self)
        arreglo2 = ("Productos","Servicios")
        arreglo3 = cargar_clientes_combobox(self)

        self.presupuestoTipoRegComboBox.addItem(arreglo2[0])
        self.presupuestoTipoRegComboBox.addItem(arreglo2[1])

        i = 0 
        j = 0
        vacio = []

        # Crear Archivo .json
        with open(u'./controllers/nuevo_presupuesto.json','w') as archivo:
            json.dump(vacio, archivo)

        # Cargar listdo de "Productos" en el combobox correspondiente
        if len(arreglo) > 0:
            while i < len(arreglo):
                self.presupuestoProdServRegComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][4]))
                i = i + 1
                self.presupuestoProdServRegComboBox.setCurrentIndex(0)

        # Cargar listado de "Clientes" en el combobox correspondiente
        if len(arreglo3) > 0:
            while j < len(arreglo3):
                self.presupuestoClienteRegComboBox.addItem("Id: " + str(arreglo3[j][0]) + " | RIF / Cédula: " + arreglo3[j][2] + " | Nombre: " + arreglo3[j][1])
                j = j + 1
                self.presupuestoClienteRegComboBox.setCurrentIndex(0)

        # Acción de teclear en "Tasa"
        self.presupuestoTasaRegLineEdit.textChanged.connect(self.calcular_total)
        
        # Acción de cambiar "Producto / Servicio"
        self.presupuestoTipoRegComboBox.activated.connect(self.cambiar_prod_serv)
        
        # Acción de "Agregar"
        self.presupuestoNuevoAddPushButton.clicked.connect(self.cargar_datos_tabla)

        # Acción de "Eliminar"
        self.presupuestoNuevoElimPushButton.clicked.connect(self.eliminar_datos_tabla)

        # Acción de "Aceptar"
        self.presupuestoAceptarRegPushButton.clicked.connect(self.agregar_presupuesto)
        
        # Acción de "Cancelar"
        self.presupuestoCancelarRegPushButton.clicked.connect(self.close)
    
    # Función que modifica el ComboBox de "Producto / Servicio"
    def cambiar_prod_serv(self):
        opc_capt = self.presupuestoTipoRegComboBox.currentText()
        
        if opc_capt == 'Productos':
            arreglo = cargar_equipos_combobox(self)
            i = 0

            # Limpiar el Combobox de "Producto / Servicio"
            self.presupuestoProdServRegComboBox.clear()

            # Cargar listdo de "Productos" en el combobox correspondiente
            while i < len(arreglo):
                self.presupuestoProdServRegComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][4]))
                i = i + 1
                self.presupuestoProdServRegComboBox.setCurrentIndex(0)
        
        if opc_capt == 'Servicios':
            arreglo = cargar_servicios_combobox(self)
            i = 0

            # Limpiar el Combobox de "Producto / Servicio"
            self.presupuestoProdServRegComboBox.clear()

            # Cargar listdo de "Servicios" en el combobox correspondiente
            while i < len(arreglo):
                self.presupuestoProdServRegComboBox.addItem(str(arreglo[i][0]) + " - " + arreglo[i][1] + " | " + arreglo[i][2] + " | " + str(arreglo[i][3]))
                i = i + 1
                self.presupuestoProdServRegComboBox.setCurrentIndex(0)

    # Función que verifica el input de "Tasa"
    def verf_tasa(self):
        valor = self.presupuestoTasaRegLineEdit.text()
        bandera = False
        try:
            if valor == '': valor = 0

            valor = float(valor)
            
            bandera = True

        except ValueError:
        
            self.presupuestoTasaRegLineEdit.clear()
            msg = QMessageBox()
            msg.setWindowTitle('SISTEMA')
            msg.setText('Solo se aceptan valores númericos enteros y/o decimales en este campo. Favor de verificar')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        finally:

            return bandera

    # Función que calcula el total en Bolívares
    def calcular_total(self):
        tasa_capt = self.presupuestoTasaRegLineEdit.text()
        total_dol_capt = self.presupuestoTotDolarLineEdit.text()

        if self.verf_tasa():    
            if total_dol_capt != '' and tasa_capt != '':
                total_bs = float(tasa_capt) * float(total_dol_capt)
                self.presupuestoTotBsLineEdit.setText(str(round(total_bs,2)))
    
    # Función que verifica los campos en esta vista
    def verf_inputs(self):
        nro_presupuesto = self.presupuestoNroReglineEdit.text()
        tasa = self.presupuestoTasaRegLineEdit.text()
        
        with open(u'./controllers/nuevo_presupuesto.json','r') as archivo:
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

    def agregar_presupuesto(self):
        nro_presupuesto = self.presupuestoNroReglineEdit.text()
        tasa = self.presupuestoTasaRegLineEdit.text()
        fecha_inicio = self.presupuestoEmiRegDateEdit.text()
        fecha_fin = self.presupuestoVencRegDateEdit.text()
        cliente = self.presupuestoClienteRegComboBox.currentText()
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

        with open(u'./controllers/nuevo_presupuesto.json','r') as archivo:
            bd = json.load(archivo)
        
        renglones = bd
        monto_total = self.presupuestoTotDolarLineEdit.text()
        
        if self.verf_inputs():
            data = (nro_presupuesto, int(id_cliente), round(float(tasa),2), str(fecha_inicio), str(fecha_fin), str(renglones), monto_total)

            if crear_presupuesto(data):
                # Buscar el Max Id de la tabla "presupuestos"
                arr_max_id = buscar_max_id(self)
                ite = 0

                for arreglo in arr_max_id:
                    if ite == 0:
                        max_id = arreglo
                        ite = ite + 1
                
                # Recorrer el JSON para agregarlos a la tabla en la BD "presupuestos_detalles"
                with open(u'./controllers/nuevo_presupuesto.json','w') as archivo:
                    json.dump(bd, archivo)

                for vector in bd:
                    data2 = (int(max_id), int(str(vector['id'])), str(vector['tipo']), str(vector['serial']), str(vector['titulo']), int(str(vector['cantidad'])), float(str(vector['precio'])), float(str(vector['monto'])))
                    crear_presupuesto_detalle(data2) 

                self.limpiar_inputs()
                self.parent.refresh_prespuesto_from_child() 

                # Crear Archivo .json
                vacio = []
                with open(u'./controllers/nuevo_presupuesto.json','w') as archivo:
                    json.dump(vacio, archivo)

                msg = QMessageBox()
                msg.setWindowTitle('SISTEMA')
                msg.setText('Presupuesto creado satisfactoriamente')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
    # Limpiar Inputs o Campos de esta vista                
    def limpiar_inputs(self):
        self.presupuestoNroReglineEdit.clear()
        self.presupuestoTasaRegLineEdit.clear()
        self.presupuestoClienteRegComboBox.clearFocus()
        self.presupuestoTotDolarLineEdit.clear()
        self.presupuestoTotBsLineEdit.clear()
        self.presupuestoCantRegLineEdit.clear()
        
        # Eliminar Datos de la tabla interna de la vista "Nuevo Presupuesto"
        while(self.presupuestoRegTableWidget.rowCount() > 0):
            self.presupuestoRegTableWidget.removeRow(0)
        
        self.presupuestoRegTableWidget.reset()

        #Eliminar el archivo "nuevo_presupuesto.json"
        remove("./controllers/nuevo_presupuesto.json")
    
    # Configurar tabla de "Nuevo Presupuesto"
    def table_config_nuevo_presupuesto(self):
        column_headers = ("Id","Tipo", "Serial","Titulo", "Cantidad", "Precio Unit. ($)","Monto ($)")
        self.presupuestoRegTableWidget.setColumnCount(len(column_headers))     
        self.presupuestoRegTableWidget.setHorizontalHeaderLabels(column_headers)

        self.presupuestoRegTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # Función que recarga la tabla interna de la vista de "Nuevo Presupuesto"
    def refresh_nuevo_presupuesto_table(self):
        data3 = []
        cont = 0
        total_dol = 0
        tasa = self.presupuestoTasaRegLineEdit.text()
        
        with open(u'./controllers/nuevo_presupuesto.json','r') as archivo:
            bd = json.load(archivo)
        
        for vector in bd:
            data2 = (vector['id'], vector['tipo'], vector['serial'], vector['titulo'], vector['cantidad'], vector['precio'], vector['monto'])
            total_dol = total_dol + (float(vector['monto']))
            data3.append(data2)
        
        self.table_config_nuevo_presupuesto()
        
        
        self.presupuestoRegTableWidget.setRowCount(len(data3))
        
        for (index_row, row) in enumerate(data3):
            for (index_cell, cell) in enumerate(row):
                self.presupuestoRegTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        # Colocar el monto en dolares en dicho Line Edit
        self.presupuestoTotDolarLineEdit.setText(str(total_dol))

        # Colocar el monto en Bolívares en dicho Line Edit
        if tasa != '':
            calculo = float(tasa) * total_dol
            self.presupuestoTotBsLineEdit.setText(str(calculo))
    
    # Función que ingresa un "Producto / Servicio" en la tabla de "Presupuestos"
    def cargar_datos_tabla(self):
        indice = self.presupuestoProdServRegComboBox.currentIndex()
        valor = self.presupuestoProdServRegComboBox.itemText(indice)
        cantidad = self.presupuestoCantRegLineEdit.text()
        tasa = self.presupuestoTasaRegLineEdit.text()
        tipo = self.presupuestoTipoRegComboBox.currentText()
        cadena = valor.split(" - ")
        id_pre = cadena[0]
        cadena2 = cadena[1].split(" | ")
        serial = cadena2[0]
        texto = cadena2[1]
        precio = cadena2[2]
        bandera = False
       
        with open(u'./controllers/nuevo_presupuesto.json','r') as archivo:
            bd = json.load(archivo)

        # Verificar si el nuevo "serial" del nuevo Item a ingresar ya existe en el JSON
        for i in range(len(bd)):
            if bd[i]['serial'] == serial:
                bandera = True


        if cantidad != '':       
            if not bandera:
                monto = float(precio) * int(self.presupuestoCantRegLineEdit.text())
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

                with open(u'./controllers/nuevo_presupuesto.json','w') as archivo:
                    json.dump(bd, archivo)

                data3 = []
                cont = 0
                total_dol = 0
                
                for vector in bd:
                    data2 = (vector['id'], vector['tipo'], vector['serial'], vector['titulo'], vector['cantidad'], vector['precio'], vector['monto'])
                    total_dol = total_dol + (float(vector['monto']))
                    data3.append(data2)
                
                self.table_config_nuevo_presupuesto()
                
                
                self.presupuestoRegTableWidget.setRowCount(len(data3))
                
                for (index_row, row) in enumerate(data3):
                    for (index_cell, cell) in enumerate(row):
                        self.presupuestoRegTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
                # Colocar el monto en dolares en dicho Line Edit
                self.presupuestoTotDolarLineEdit.setText(str(total_dol))

                # Colocar el monto en Bolívares en dicho Line Edit
                if tasa != '':
                    calculo = float(tasa) * total_dol
                    self.presupuestoTotBsLineEdit.setText(str(round(calculo,2)))

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

    # Eliminar un Item del archivo JSON "nuevo_presupuesto.json"
    def eliminar_item(self, ident):
       id_capturado = 0
       i = 0
       index_capt = 0
        
       with open(u'./controllers/nuevo_presupuesto.json','r') as archivo:
        bd = json.load(archivo)

        lista = list(bd)
        arreglo = np.array(lista)
        
        for i in range(len(bd)):
            if bd[i]['serial'] == str(ident):
                index_capt = i
                i = len(bd)

        bd.pop(int(index_capt))
    
        with open(u'./controllers/nuevo_presupuesto.json','w') as archivo:
            json.dump(bd, archivo)
       
       return True
               

    # Función que elimina Items de la tabla interna
    def eliminar_datos_tabla(self):
        
        # Obtener el id seleccionado desde la tabla
        selected_row = self.presupuestoRegTableWidget.selectedItems()

        if selected_row:
            item_id = str(selected_row[1].text())
            bandera = self.eliminar_item(item_id)

            if bandera:
                self.refresh_nuevo_presupuesto_table()