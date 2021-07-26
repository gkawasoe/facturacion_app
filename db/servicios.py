import sqlite3
from sqlite3 import Error
from .connection import create_connection


#Crear Nuevo Registro de "Servicios"
def crear_serv(data):
    conn = create_connection()
    sql = """INSERT INTO servicios (serial, titulo, precio_unit_dolar, descripcion) 
            VALUES (?, ?, ?, ?)"""

    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        print("Nuevo Registro de 'Servicio' Creado...!!!")
        return True

    except Error as e:
        print("Error creando al nuevo registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Modificar Registro de "Servicio"
def actualizar_serv(_id, data):

    conn = create_connection()
    sql = f"""UPDATE servicios SET 
                            serial = ?, 
                            titulo = ?, 
                            precio_unit_dolar = ?, 
                            descripcion = ?
            WHERE id_servicio = {_id}"""
                            
    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("'Servicio' actualizado...!!!")
        return True

    except Error as e:
        print("Error al actualizar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Eliminar Registro de "Servicio"
def eliminar_serv(_id):
    
    conn = create_connection()
    sql = f"DELETE FROM servicios WHERE id_servicio = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("'Servicio' eliminado...!!!")
        return True
    except Error as e:
        print("Error al eliminar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Visualizar Registros de "Servicio"
def mostrar_serv():
    conn = create_connection()
    sql = "SELECT * FROM servicios"

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

#Buscar clientes por Id
def buscar_serv_id(id_serv):
    conn = create_connection()
    sql = f"SELECT * FROM servicios WHERE id_servicio = {id_serv}"

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

#Buscar clientes por serial
def buscar_serv_serial(serial):
    conn = create_connection()
    sql = f"SELECT * FROM servicios WHERE serial LIKE '%{serial}%'"

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

#Buscar clientes por titulo
def buscar_serv_titulo(titulo):
    conn = create_connection()
    sql = f"SELECT * FROM servicios WHERE titulo LIKE '%{titulo}%'"

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