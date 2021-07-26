import sqlite3
from sqlite3 import Error
from .connection import create_connection


#Crear Nuevo Registro de "Equipo / Producto"
def crear_ep(data):
    conn = create_connection()
    sql = """INSERT INTO equipos_productos (serial, titulo, cantidad, precio_unit_dolar, descripcion) 
            VALUES (?, ?, ?, ?, ?)"""

    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        print("Nuevo Registro de 'Equipo / Producto' Creado...!!!")
        return True

    except Error as e:
        print("Error creando al nuevo registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Modificar Registro de "Equipo / Producto"
def actualizar_ep(_id, data):

    conn = create_connection()
    sql = f"""UPDATE equipos_productos SET 
                            serial = ?, 
                            titulo = ?, 
                            cantidad = ?,
                            precio_unit_dolar = ?, 
                            descripcion = ?
            WHERE id_equipo_producto = {_id}"""
                            
    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("'Equipo / Producto' actualizado...!!!")
        return True

    except Error as e:
        print("Error al actualizar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Eliminar Registro de "Equipo / Producto"
def eliminar_ep(_id):
    
    conn = create_connection()
    sql = f"DELETE FROM equipos_productos WHERE id_equipo_producto = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("'Equipo / Producto' eliminado...!!!")
        return True
    except Error as e:
        print("Error al eliminar el registro: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Visualizar Registros de "Equipo / Producto"
def mostrar_ep():
    conn = create_connection()
    sql = "SELECT * FROM equipos_productos"

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
def buscar_ep_id(id_ep):
    conn = create_connection()
    sql = f"SELECT * FROM equipos_productos WHERE id_equipo_producto = {id_ep}"

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
def buscar_ep_serial(serial):
    conn = create_connection()
    sql = f"SELECT * FROM equipos_productos WHERE serial LIKE '%{serial}%'"

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

#Buscar clientes por Titulo
def buscar_ep_titulo(titulo):
    conn = create_connection()
    sql = f"SELECT * FROM equipos_productos WHERE titulo LIKE '%{titulo}%'"

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