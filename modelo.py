import sqlite3 as sq3

class ABMC:

    def __init__(self):
        
        self.path_db = 'agenda.db'

    def abrir_con(self):
        con = sq3.connect(self.path_db)
        return con

    def cerrar_con(self):
        con = self.abrir_con()
        con.close()

    def crear_bd(self):
        con = self.abrir_con()
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre text NOT NULL,
            apellido text NOT NULL,
            telefono INTEGER NOT NULL
            )""")
        con.commit()
        self.cerrar_con()
    
    def alta(self, nombre, apellido, telefono):
        con = self.abrir_con()
        cursor = con.cursor()
        sql_alta = """INSERT INTO contactos (nombre, apellido, telefono)
        VALUES (?,?,?)"""
        cursor.execute(sql_alta, (nombre, apellido, telefono))
        con.commit()
        self.cerrar_con()

    def baja(self, id):
        con = self.abrir_con()
        cursor = con.cursor()
        sql_baja = "DELETE FROM contactos WHERE id = ?"
        cursor.execute(sql_baja, (id,))
        con.commit()
        self.cerrar_con()
    
    def modificacion(self, id, nombre, apellido, telefono):
        con = self.abrir_con()
        cursor = con.cursor()
        sql_modificacion = """UPDATE contactos SET nombre = ?, apellido = ?,
        telefono = ? WHERE id = ?"""
        cursor.execute(sql_modificacion, (nombre, apellido, telefono, id))
        con.commit()
        self.cerrar_con()

    def listar_bd(self):
        con = self.abrir_con()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM contactos")
        con.commit()
        data = cursor.fetchall()
        self.cerrar_con()

        for item in data:
            print(f"""
ID: {item[0]} *Nombre: {item[1]} *Apellido: {item[2]} *Teléfono: {item[3]}""")
    
    def buscar_por_id(self, id):
        con = self.abrir_con()
        cursor = con.cursor()
        sql_buscar_id = "SELECT * FROM contactos WHERE id = ?"
        cursor.execute(sql_buscar_id, (id,))
        con.commit()
        item = cursor.fetchone()
        self.cerrar_con()

        print(f"""
ID: {item[0]} *Nombre: {item[1]} *Apellido: {item[2]} *Teléfono: {item[3]}""")





if __name__ == "__main__":
    # ABMC().crear_bd()
    # ABMC().alta()
    # ABMC().baja()
    # ABMC().consulta_bd()
    ABMC().listar_bd()