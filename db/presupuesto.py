import sqlite3
from sqlite3 import Error
from .connection import create_connection
import json

#Cargar Renglon de un registro de "Presupuesto" en especifico
def cargar_renglon(_id):
    conn = create_connection()
    sql = f"SELECT * FROM presupuestos_detalles WHERE id_presupuesto = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al buscar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Cargar clientes en pantallas de "Nuevo Presupuesto" / "Modificar Presupuesto"
def cargar_clientes_combobox(data):
    conn = create_connection()
    sql = "SELECT * FROM clientes"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al mostrar los registros: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            
#Cargar datos en las pantallas de "Nuevo Presupuesto" / "Modificar Presupuesto"
def cargar_equipos_combobox(data):
    conn = create_connection()
    sql = """SELECT * FROM equipos_productos"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al mostrar los registros: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Cargar datos en las pantallas de "Nuevo Presupuesto" / "Modificar Presupuesto"
def cargar_servicios_combobox(data):
    conn = create_connection()
    sql = """SELECT * FROM servicios"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al mostrar los registros: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Crear Nuevo Registro de "Presupuesto"
def crear_presupuesto(data):
    
    conn = create_connection()
    sql = """INSERT INTO presupuestos (nro_presupuesto, id_cliente, tasa, fecha_inicio, fecha_fin, renglones, monto_total) 
            VALUES (?, ?, ?, ?, ?, ?, ?)"""

    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        print("Nuevo Registro de 'Presupuesto' Creado...!!!")
        return True

    except Error as e:
        print("Error creando al nuevo registro: "+ str(e))
    finally: 
        if conn:
            cur.close()
            conn.close()

#Buscar el MAX Id de la tabla "presupuestos"
def buscar_max_id(data):
    
    conn = create_connection()
    sql = f"SELECT MAX(id_presupuesto) FROM presupuestos"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        max_id = cur.fetchone()
        
        return max_id
    except Error as e:
        print("Error al buscar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Crear Nuevo Registro de "presupuesto_detalles"
def crear_presupuesto_detalle(data):
    
    conn = create_connection()
    sql = """INSERT INTO presupuestos_detalles (id_presupuesto, id, tipo, serial, titulo, cantidad, precio, monto) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        print("Nuevo Registro de 'presupuesto_detalle' Creado...!!!")
        return True

    except Error as e:
        print("Error creando al nuevo registro: "+ str(e))
    finally: 
        if conn:
            cur.close()
            conn.close()

#Modificar Registro de "Presupuesto"
def actualizar_presupuesto(_id, data):

    conn = create_connection()
    sql = f"""UPDATE presupuestos SET 
                            nro_presupuesto = ?, 
                            id_cliente = ?, 
                            tasa = ?, 
                            fecha_inicio = ?,
                            fecha_fin = ?,
                            renglones = ?,
                            monto_total = ?
            WHERE id_presupuesto = {_id}"""
                            
    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("'Presupuesto' actualizado...!!!")
        return True

    except Error as e:
        print("Error al actualizar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Eliminar Registro de "presupuestos"
def eliminar_presupuesto(_id):
    
    conn = create_connection()
    sql = f"DELETE FROM presupuestos WHERE id_presupuesto = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("'Presupuesto' eliminado...!!!")
        return True
    except Error as e:
        print("Error al eliminar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Eliminar Registro de "presupuestos_detalles"
def eliminar_presupuesto_detalle(_id):
    
    conn = create_connection()
    sql = f"DELETE FROM presupuestos_detalles WHERE id_presupuesto = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("'Presupuesto detalle' eliminado...!!!")
        return True
    except Error as e:
        print("Error al eliminar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Visualizar Registros de "Presupuesto"
def mostrar_presupuesto():
    conn = create_connection()
    sql = "SELECT p.id_presupuesto as id_presupuesto, p.nro_presupuesto as nro_presupuesto, c.nombre_cliente as nombre_cliente, p.fecha_inicio as fecha, p.monto_total as monto_total FROM presupuestos as p LEFT JOIN clientes as c ON p.id_cliente = c.cliente_id"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al mostrar los registros: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar "presupuesto" por Id
def buscar_presupuesto_id(id_presupuesto):
    conn = create_connection()
    sql = f"SELECT * FROM presupuestos WHERE id_presupuesto = {id_presupuesto}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchone()
        return ep
    except Error as e:
        print("Error al buscar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar presupuesto por "Nro. Presupuesto"
def buscar_presupuesto_nro(nro_presupuesto):
    conn = create_connection()
    sql = f"SELECT p.id_presupuesto as id_presupuesto, p.nro_presupuesto as nro_presupuesto, c.nombre_cliente as nombre_cliente, p.fecha_inicio as fecha_inicio, p.monto_total as monto_total FROM presupuestos as p LEFT JOIN clientes as c ON p.id_cliente = c.cliente_id WHERE p.nro_presupuesto LIKE '%{nro_presupuesto}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al buscar el registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar presupuesto por "Cliente"
def buscar_presupuesto_cliente(cliente):
    conn = create_connection()
    sql = f"SELECT p.id_presupuesto as id_presupuesto, p.nro_presupuesto as nro_presupuesto, c.nombre_cliente as nombre_cliente, p.fecha_inicio as fecha_inicio, p.monto_total as monto_total FROM presupuestos as p LEFT JOIN clientes as c ON p.id_cliente = c.cliente_id WHERE c.nombre_cliente LIKE '%{cliente}%'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al buscar el registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar presupuesto por "Fecha Inicio"
def buscar_presupuesto_fecha(fecha):
    conn = create_connection()
    sql = f"SELECT p.id_presupuesto as id_presupuesto, p.nro_presupuesto as nro_presupuesto, c.nombre_cliente as nombre_cliente, p.fecha_inicio as fecha_inicio, p.monto_total as monto_total FROM presupuestos as p LEFT JOIN clientes as c ON p.id_cliente = c.cliente_id WHERE p.fecha_inicio LIKE '%{fecha}%'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        ep = cur.fetchall()
        return ep
    except Error as e:
        print("Error al buscar el registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

