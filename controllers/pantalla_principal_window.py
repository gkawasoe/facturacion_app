from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.pantalla_principal_window import PantallaPrincipalWindow
from db.clientes import mostrar_clientes
from db.ep import mostrar_ep
from db.servicios import mostrar_serv
from db.presupuesto import mostrar_presupuesto
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.image(u'./assets/icons/logo_empresa.jpg', 60, 5, 80)
        self.set_font('helvetica', 'B', 8)
        self.cell(0, 40, 'La Asunción, Calle Ruíz 5-93/ Teléfonos: (0412) 7956536 (0416) 2961764', border=False, ln=1, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'B', 8)
        self.cell(0, 10, 'Autorizado por: TECNO SERVICIOS A.J. ROJAS', border=False, ln=1, align='C')

class PantallaPrincipalVentana(QWidget, PantallaPrincipalWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Cargar datos en el ComboBox de "Clientes"
        arreglo = ('Nombres', 'RIF/Cédula')
        self.clienteBusComboBox.addItem(arreglo[0])
        self.clienteBusComboBox.addItem(arreglo[1])

        # Cargar datos en el ComboBox de "Equipos/Productos"
        arreglo2 = ('Serial', 'Titulo')
        self.equipoBusComboBox.addItem(arreglo2[0])
        self.equipoBusComboBox.addItem(arreglo2[1])

        # Cargar datos en el ComboBox de "Servicios"
        arreglo3 = ('Serial', 'Titulo')
        self.servicioBusComboBox.addItem(arreglo3[0])
        self.servicioBusComboBox.addItem(arreglo3[1])

        # Cargar datos en el ComboBox de "Presupuestos"
        arreglo4 = ('Nro. Presupuesto', 'Cliente', 'Fecha')
        self.presupuestoBusComboBox.addItem(arreglo4[0])
        self.presupuestoBusComboBox.addItem(arreglo4[1])
        self.presupuestoBusComboBox.addItem(arreglo4[2])

        # Acciones de botoneras en "Clientes"
        self.clienteRegBoton.clicked.connect(self.open_nuevo_cliente_window) # Registrar
        self.clienteModBoton.clicked.connect(self.open_mod_cliente_window) # Modificar
        self.clienteElimBoton.clicked.connect(self.remove_cliente) # Eliminar
        self.clienteBusBoton.clicked.connect(self.buscar_cliente) # Buscar

        # Acciones de Botoneras en "Equipos / Productos"
        self.equipoRegBoton.clicked.connect(self.open_nuevo_ep_window) # Registrar
        self.equipoModBoton.clicked.connect(self.open_mod_ep_window) # Modificar
        self.equipoElimBoton.clicked.connect(self.remove_ep) # Eliminar
        self.equipoBusBoton.clicked.connect(self.buscar_ep) # Buscar

        # Acciones de Botoneras en "Servicios"
        self.servicioRegBoton.clicked.connect(self.open_nuevo_serv_window) # Registrar
        self.servicioModBoton.clicked.connect(self.open_mod_serv_window) # Modificar
        self.servicioElimBoton.clicked.connect(self.remove_serv) # Eliminar
        self.servicioBusBoton.clicked.connect(self.buscar_servicio) # Buscar

        # Acciones de Botoneras en "Presupuestos"
        self.presupuestoRegBoton.clicked.connect(self.open_nuevo_presupuesto_window) # Registrar
        self.presupuestoModBoton.clicked.connect(self.open_mod_presupuesto_window) # Modificar  
        self.presupuestoElimBoton.clicked.connect(self.remove_presupuesto) # Eliminar
        self.presupuestoImpBoton.clicked.connect(self.crear_pdf_presupuesto) # Imprimir
        self.presupuestoBusBoton.clicked.connect(self.buscar_presupuesto) # Buscar

        # Inicialización de la tabla en "Clientes"
        self.table_config_cliente()
        self.populate_cliente_table()

        # Inicialización de la tabla en "Equipos / Productos"
        self.table_config_ep()
        self.populate_ep_table()

        # Inicialización de la tabla en "Servicios"
        self.table_config_serv()
        self.populate_serv_table()

        # Inicialización de la tabla en "Presupuestos"
        self.table_config_presupuesto()
        self.populate_presupuesto_table()

    # --- SECCIÓN DE CLIENTES ---    
    
    # Función que refresca la tabla de clientes
    def refresh_clientes_from_child(self):
        data = mostrar_clientes()
        self.populate_cliente_table()
    
    # Función que crea un nuevo cliente
    def open_nuevo_cliente_window(self):
        from controllers.nuevo_cliente_window import NuevoClienteWindow
        window = NuevoClienteWindow(self)
        window.show()

    # Función que modifica un registro de un cliente
    def open_mod_cliente_window(self):
        from controllers.mod_cliente_window import ModClienteWindow
        
        # Obtener el cliente seleccionado desde la tabla
        selected_row = self.clienteTabla.selectedItems()

        if selected_row:
            cliente_id = int(selected_row[0].text())
            window = ModClienteWindow(self, cliente_id)
            window.show()
        
        self.clienteTabla.clearSelection()
        
    # Función que elimina el registro de un cliente
    def remove_cliente(self):
        from db.clientes import eliminar_cliente

        # Obtener el cliente seleccionado desde la tabla
        selected_row = self.clienteTabla.selectedItems()

        if selected_row:
            cliente_id = int(selected_row[0].text())
            bandera = eliminar_cliente(cliente_id)

            if bandera:
                self.refresh_clientes_from_child()

    # Configurar tabla de Clientes
    def table_config_cliente(self):
        column_headers = ("Id Cliente","Nombres / Apellidos", "RIF / Cédula", "Email", "Teléfono")
        self.clienteTabla.setColumnCount(len(column_headers))
        self.clienteTabla.setHorizontalHeaderLabels(column_headers)

        self.clienteTabla.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Cargar datos de Clientes
    def populate_cliente_table(self):
        data = mostrar_clientes()
        self.clienteTabla.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.clienteTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Función que busca en la sección de "Clientes"
    def buscar_cliente(self):
        from db.clientes import buscar_clientes_rif_ced, buscar_clientes_nombre

        opcion = self.clienteBusComboBox.currentText()
        valor_busqueda = self.clienteBusLineEdit.text()
        self.clienteTabla.clearContents()

        if opcion == 'Nombres':
            if valor_busqueda != '':
                data = buscar_clientes_nombre(valor_busqueda)
                self.clienteTabla.setRowCount(len(data))
            else:
                data = mostrar_clientes()
                self.clienteTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.clienteTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

        if opcion == 'RIF/Cédula':
            if valor_busqueda != '':
                data = buscar_clientes_rif_ced(valor_busqueda)
                self.clienteTabla.setRowCount(len(data))
            else:
                data = mostrar_clientes()
                self.clienteTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.clienteTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # --- SECCIÓN DE "EQUIPOS / PRODUCTOS" ---

    # Función que refresca la tabla de "Equipos / Productos"
    def refresh_ep_from_child(self):
        data = mostrar_ep()
        self.populate_ep_table()
    
    # Función que crea un nuevo registro de "Equipos / Productos"
    def open_nuevo_ep_window(self):
        from controllers.nuevo_ep_window import NuevoEpWindow
        window = NuevoEpWindow(self)
        window.show()

    # Función que modifica un registro de "Equipos / Productos"
    def open_mod_ep_window(self):
        from controllers.mod_ep_window import ModEpWindow
        
        # Obtener el id de "Equipos / Producto" seleccionado desde la tabla
        selected_row = self.equipoTabla.selectedItems()

        if selected_row:
            ep_id = int(selected_row[0].text())
            window = ModEpWindow(self, ep_id)
            window.show()
        
        self.equipoTabla.clearSelection()
        
    # Función que elimina un registro de la tabla "Equipos / Productos"
    def remove_ep(self):
        from db.ep import eliminar_ep

        # Obtener el id seleccionado desde la tabla
        selected_row = self.equipoTabla.selectedItems()

        if selected_row:
            ep_id = int(selected_row[0].text())
            bandera = eliminar_ep(ep_id)

            if bandera:
                self.refresh_ep_from_child()

    # Configurar tabla de "Equipos / Productos"
    def table_config_ep(self):
        column_headers = ("Id Equi/Prod","Serial", "Titulo", "Cantidad Stock", "Precio Unit. ($)")
        self.equipoTabla.setColumnCount(len(column_headers))     
        self.equipoTabla.setHorizontalHeaderLabels(column_headers)

        self.equipoTabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # Cargar datos de "Equipos / Productos"
    def populate_ep_table(self):
        data = mostrar_ep()
        self.equipoTabla.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.equipoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Función que busca en la sección de "Equipos/Productos"
    def buscar_ep(self):
        from db.ep import buscar_ep_serial, buscar_ep_titulo

        opcion = self.equipoBusComboBox.currentText()
        valor_busqueda = self.equipoBusLineEdit.text()
        self.equipoTabla.clearContents()

        if opcion == 'Serial':
            if valor_busqueda != '':
                data = buscar_ep_serial(valor_busqueda)
                self.equipoTabla.setRowCount(len(data))
            else:
                data = mostrar_ep()
                self.equipoTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.equipoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

        if opcion == 'Titulo':
            if valor_busqueda != '':
                data = buscar_ep_titulo(valor_busqueda)
                self.equipoTabla.setRowCount(len(data))
            else:
                data = mostrar_ep()
                self.equipoTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.equipoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # --- SECCIÓN DE "SERIVCIOS" ---

    # Función que refresca la tabla de "Servicios"
    def refresh_serv_from_child(self):
        data = mostrar_serv()
        self.populate_serv_table()
    
    # Función que crea un nuevo registro de "Servicios"
    def open_nuevo_serv_window(self):
        from controllers.nuevo_servicio_window import NuevoServWindow
        window = NuevoServWindow(self)
        window.show()

    # Función que modifica un registro de "Servicios"
    def open_mod_serv_window(self):
        from controllers.mod_servicio_window import ModServWindow
        
        # Obtener el id de "Servicios" seleccionado desde la tabla
        selected_row = self.servicioTabla.selectedItems()

        if selected_row:
            serv_id = int(selected_row[0].text())
            window = ModServWindow(self, serv_id)
            window.show()
        
        self.servicioTabla.clearSelection()
        
    # Función que elimina un registro de la tabla "Servicios"
    def remove_serv(self):
        from db.servicios import eliminar_serv

        # Obtener el id seleccionado desde la tabla
        selected_row = self.servicioTabla.selectedItems()

        if selected_row:
            serv_id = int(selected_row[0].text())
            bandera = eliminar_serv(serv_id)

            if bandera:
                self.refresh_serv_from_child()

    # Configurar tabla de "Servicios"
    def table_config_serv(self):
        column_headers = ("Id Servicio","Serial", "Titulo", "Precio Unit. ($)")
        self.servicioTabla.setColumnCount(len(column_headers))     
        self.servicioTabla.setHorizontalHeaderLabels(column_headers)

        self.servicioTabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # Cargar datos de "Servicios"
    def populate_serv_table(self):
        data = mostrar_serv()
        self.servicioTabla.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.servicioTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Función que busca en la sección de "Servicios"
    def buscar_servicio(self):
        from db.servicios import buscar_serv_serial, buscar_serv_titulo

        opcion = self.servicioBusComboBox.currentText()
        valor_busqueda = self.servicioBusLineEdit.text()
        self.servicioTabla.clearContents()

        if opcion == 'Serial':
            if valor_busqueda != '':
                data = buscar_serv_serial(valor_busqueda)
                self.servicioTabla.setRowCount(len(data))
            else:
                data = mostrar_serv()
                self.servicioTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.servicioTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

        if opcion == 'Titulo':
            if valor_busqueda != '':
                data = buscar_serv_titulo(valor_busqueda)
                self.servicioTabla.setRowCount(len(data))
            else:
                data = mostrar_serv()
                self.servicioTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.servicioTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # --- SECCIÓN DE "PRESUPUESTOS" ---

    # Función que refresca la tabla de "Presupuestos"
    def refresh_prespuesto_from_child(self):
        data = mostrar_presupuesto()
        self.populate_presupuesto_table()
    
    # Función que crea un nuevo registro de "Presupuestos"
    def open_nuevo_presupuesto_window(self):
        from controllers.nuevo_presupuesto_window import NuevoPresupuestoWindow
        window = NuevoPresupuestoWindow(self)
        window.show()

    # Función que modifica un registro de "Presupuestos"
    def open_mod_presupuesto_window(self):
        from controllers.mod_presupuesto_window import ModPresupuestoWindow
        
        # Obtener el id de "Presupuestos" seleccionado desde la tabla
        selected_row = self.presupuestoTabla.selectedItems()

        if selected_row:
            presupuesto_id = int(selected_row[0].text())
            window = ModPresupuestoWindow(self, presupuesto_id)
            window.show()
        
        self.presupuestoTabla.clearSelection()
        
    # Función que elimina un registro de la tabla "Presupuestos"
    def remove_presupuesto(self):
        from db.presupuesto import eliminar_presupuesto, eliminar_presupuesto_detalle

        # Obtener el id seleccionado desde la tabla
        selected_row = self.presupuestoTabla.selectedItems()

        if selected_row:
            presupuesto_id = int(selected_row[0].text())
            bandera = eliminar_presupuesto(presupuesto_id)
            bandera2 = eliminar_presupuesto_detalle(presupuesto_id)

            if bandera and bandera2:
                self.refresh_prespuesto_from_child()

    # Configurar tabla de "Presupuestos"
    def table_config_presupuesto(self):
        column_headers = ("Id Presupuesto", "Nro. Prespuesto", "Cliente", "Fecha Creación", "Monto ($)")
        self.presupuestoTabla.setColumnCount(len(column_headers))     
        self.presupuestoTabla.setHorizontalHeaderLabels(column_headers)
        self.presupuestoTabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # Cargar datos de "Presupuestos"
    def populate_presupuesto_table(self):
        data = mostrar_presupuesto()
        self.presupuestoTabla.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.presupuestoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Función que busca en la sección de "Presupuestos"
    def buscar_presupuesto(self):
        from db.presupuesto import buscar_presupuesto_nro, buscar_presupuesto_cliente, buscar_presupuesto_fecha

        opcion = self.presupuestoBusComboBox.currentText()
        valor_busqueda = self.presupuestoBusLineEdit.text()
        self.presupuestoTabla.clearContents()

        if opcion == 'Nro. Presupuesto':
            if valor_busqueda != '':
                data = buscar_presupuesto_nro(valor_busqueda)
                self.presupuestoTabla.setRowCount(len(data))
            else:
                data = mostrar_presupuesto()
                self.presupuestoTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.presupuestoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

        if opcion == 'Cliente':
            if valor_busqueda != '':
                data = buscar_presupuesto_cliente(valor_busqueda)
                self.presupuestoTabla.setRowCount(len(data))
            else:
                data = mostrar_presupuesto()
                self.presupuestoTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.presupuestoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        if opcion == 'Fecha':
            if valor_busqueda != '':
                data = buscar_presupuesto_fecha(valor_busqueda)
                self.presupuestoTabla.setRowCount(len(data))
            else:
                data = mostrar_presupuesto()
                self.presupuestoTabla.setRowCount(len(data))
            
            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    self.presupuestoTabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Crear archivo PDF de un "Presupuesto"
    def crear_pdf_presupuesto(self):
        from db.presupuesto import buscar_presupuesto_id, cargar_renglon
        from db.clientes import buscar_clientes_id

        # Obtener el id seleccionado desde la tabla
        selected_row = self.presupuestoTabla.selectedItems()
        arreglo = []
        i = 0
        j = 10
        k = 0

        if selected_row:
            presupuesto_id = int(selected_row[0].text())
            presupuesto_info = buscar_presupuesto_id(presupuesto_id)
            cliente_id = presupuesto_info[2]
            cliente_info = buscar_clientes_id(cliente_id)
            presupuesto_detalles_info = cargar_renglon(presupuesto_id)
            
            pdf2 = PDF('P','mm','Letter')
            # Colocar saltos de linea
            pdf2.set_auto_page_break(auto=True, margin=15)
            
            #Agregar la página
            pdf2.add_page()
            pdf2.set_font('helvetica','B',12)
            
            # Agregar el titulo de "DATOS DEL CLIENTE"
            pdf2.cell(0, -10, 'DATOS DEL CLIENTE:', border=False, ln=True, align='L')

            # Nro Presupuesto
            pdf2.set_xy(120, 40)
            pdf2.cell(15, 10, 'PRESUPUESTO N°:', border=False, ln=0, align='L')
            pdf2.set_font('helvetica','',10)
            pdf2.set_xy(165, 40)
            pdf2.cell(15, 10, presupuesto_info[1], border=False, ln=0, align='L')
            
            # Agregar titulos "Nombre, Rif, Dirección"
            pdf2.set_font('helvetica','B',10)
            pdf2.rect(8, 50, 120, 40, 'D')
            pdf2.set_y(44)
            pdf2.cell(10, 20, 'Nombre ó Razón Social: ', ln=True, align='L')
            pdf2.set_y(58)
            pdf2.cell(10, 20, 'R.I.F / Cédula: ', ln=True, align='L')
            pdf2.set_y(64)
            pdf2.cell(10, 20, 'Dirección: ', ln=True, align='L')

            # Agregar datos de "Nombre, Rif, Dirección"
            pdf2.set_font('helvetica','',10)
            pdf2.set_y(49)
            pdf2.cell(10, 20, cliente_info[1], ln=True)
            pdf2.set_xy(37, 58)
            pdf2.cell(10, 20, cliente_info[2], ln=True)
            pdf2.set_y(76)
            pdf2.multi_cell(100, 4, cliente_info[5], )
            
            # Agregar titulos "Fecha Emisión" y "Fecha Vencimiento"
            pdf2.set_font('helvetica','B',10)
            pdf2.rect(140, 50, 70, 40, 'D')
            pdf2.set_xy(145, 44)
            pdf2.cell(10, 20, 'Fecha Emisión: ', ln=True)
            pdf2.set_xy(145, 62)
            pdf2.cell(10, 20, 'Fecha Vencimiento: ', ln=True)

            # Agregar datos de "Fecha Emisión" y "Fecha Vencimiento"
            pdf2.set_font('helvetica','',10)
            pdf2.set_xy(149, 51)
            pdf2.cell(10, 20, presupuesto_info[4], ln=True)
            pdf2.set_xy(149, 69)
            pdf2.cell(10, 20, presupuesto_info[5], ln=True)
            
            # Crear la fila principal
            pdf2.set_fill_color(128, 128, 128)
            pdf2.set_font('helvetica','B',12)
            pdf2.set_xy(8, 100)
            pdf2.cell(25, 10, 'Items', border=0, ln=1, align='C', fill=1)
            pdf2.set_xy(33, 100)
            pdf2.cell(87, 10, 'Concepto / Descripción', border=0, ln=1, align='C', fill=1)
            pdf2.set_xy(120, 100)
            pdf2.cell(30, 10, 'Cantidad', border=0, ln=1, align='C', fill=1)
            pdf2.set_xy(150, 100)
            pdf2.cell(30, 10, 'Precio U.', border=0, ln=1, align='C', fill=1)
            pdf2.set_xy(180, 100)
            pdf2.cell(30, 10, 'Total', border=0, ln=1, align='C', fill=1)
            
            # Datos para la tabla
            while k < len(presupuesto_detalles_info):
                if i % 2 == 0:
                    pdf2.set_fill_color(255, 255, 255)
                else:
                    pdf2.set_fill_color(192, 192, 192)
                
                pdf2.set_font('helvetica','',10)
                pdf2.set_xy(8, 100 + j)
                pdf2.multi_cell(25, 10, str(presupuesto_detalles_info[k][4]), border=0, align='L', fill=1)
                pdf2.set_xy(33, 100 + j)
                pdf2.multi_cell(87, 10, str(presupuesto_detalles_info[k][5]), border=0, align='L', fill=1)
                pdf2.set_xy(120, 100+ j)
                pdf2.multi_cell(30, 10, str(presupuesto_detalles_info[k][6]), border=0, align='C', fill=1)
                pdf2.set_xy(150, 100 + j)
                pdf2.multi_cell(30, 10, str(presupuesto_detalles_info[k][7]), border=0, align='C', fill=1)
                pdf2.set_xy(180, 100 + j)
                pdf2.multi_cell(30, 10, str(presupuesto_detalles_info[k][8]), border=0, align='C', fill=1)

                i = i + 1
                j = j + 10
                k = k + 1

            if j < 129:
                #Total Neto
                pdf2.set_font('helvetica','B',14)
                pdf2.set_fill_color(255, 255, 255)
                pdf2.set_xy(33, 130 + j)
                pdf2.cell(10, 10, 'Total Neto:', border=0, align='C', fill=1)
                pdf2.set_xy(55, 130 + j)
                pdf2.set_font('helvetica','',14)
                pdf2.cell(10, 10, str(presupuesto_info[7]), border=0, align='C', fill=1)

                #Total
                pdf2.set_font('helvetica','B',14)
                pdf2.set_fill_color(255, 255, 255)
                pdf2.set_xy(37, 140 + j)
                pdf2.cell(15, 10, 'Total:', border=0, align='C', fill=1)
                pdf2.set_xy(53, 140 + j)
                pdf2.set_font('helvetica','',14)
                pdf2.cell(15, 10, str(presupuesto_info[7]), border=0, align='C', fill=1)

            else:
                pdf2.add_page()
                #Total Neto
                pdf2.set_font('helvetica','B',14)
                pdf2.set_fill_color(255, 255, 255)
                pdf2.set_xy(33, j)
                pdf2.cell(10, 10, 'Total Neto:', border=0, align='C', fill=1)
                pdf2.set_xy(55, j)
                pdf2.set_font('helvetica','',14)
                pdf2.cell(10, 10, str(presupuesto_info[7]), border=0, align='C', fill=1)

                #Total                
                pdf2.set_font('helvetica','B',14)
                pdf2.set_fill_color(255, 255, 255)
                pdf2.set_xy(37, 10 + j)
                pdf2.cell(15, 10, 'Total:', border=0, align='C', fill=1)
                pdf2.set_xy(53, 10 +j)
                pdf2.set_font('helvetica','',14)
                pdf2.cell(15, 10, str(presupuesto_info[7]), border=0, align='C', fill=1)

            # Archivo PDF creado
            pdf2.output('presupuesto_pdf.pdf')
            
            # Abre el archivo PDF
            os.startfile('presupuesto_pdf.pdf')

