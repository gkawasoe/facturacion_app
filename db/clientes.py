import sqlite3
from sqlite3 import Error
from .connection import create_connection

#Crear Nuevo Registro de Cliente
def crear_cliente(data):
    conn = create_connection()
    sql = """INSERT INTO clientes (nombre_cliente, rif_ced_cliente, email_cliente, telf_cliente, dir_cliente) 
            VALUES (?, ?, ?, ?, ?)"""

    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        # self.table_config_cliente()
        # self.populate_cliente_table()

        print("Nuevo Cliente Creado...!!!")
        return True

    except Error as e:
        print("Error creando al nuevo cliente: "+ str(e))
    finally:
        if conn:
            # cur.close()
            conn.close()

#Modificar Registro de Cliente
def actualizar_cliente(_id, data):

    conn = create_connection()
    sql = f"""UPDATE clientes SET 
                            nombre_cliente = ?, 
                            rif_ced_cliente = ?, 
                            email_cliente = ?, 
                            telf_cliente = ?, 
                            dir_cliente = ?
            WHERE cliente_id = {_id}"""
                            
    try:
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Cliente actualizado...!!!")
        return True

    except Error as e:
        print("Error al actualizar al cliente: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Eliminar Registro de Cliente
def eliminar_cliente(_id):
    
    conn = create_connection()
    sql = f"DELETE FROM clientes WHERE cliente_id = {_id}"

    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Cliente eliminado...!!!")
        return True
    except Error as e:
        print("Error al eliminar el cliente: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Visualizar Registros de Clients
def mostrar_clientes():
    conn = create_connection()
    sql = "SELECT * FROM clientes"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        clientes = cur.fetchall()
        
        return clientes
    except Error as e:
        print("Error al mostrar los clientes: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar clientes por Rif/Cédula
def buscar_clientes_id(rif_ced):
    conn = create_connection()
    sql = f"SELECT * FROM clientes WHERE cliente_id = {rif_ced}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        cliente = cur.fetchone()
        return cliente
    except Error as e:
        print("Error al buscar cliente: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#Buscar clientes por nombre
def buscar_clientes_nombre(nombre):
    conn = create_connection()
    sql = f"SELECT * FROM clientes WHERE nombre_cliente LIKE '%{nombre}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        cliente = cur.fetchall()
        return cliente
    except Error as e:
        print("Error al buscar cliente: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

# Buscar clientes por "RIF/Cédula"
def buscar_clientes_rif_ced(rif_ced):
    conn = create_connection()
    sql = f"SELECT * FROM clientes WHERE rif_ced_cliente LIKE '%{rif_ced}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        cliente = cur.fetchall()
        return cliente
    except Error as e:
        print("Error al buscar cliente: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()