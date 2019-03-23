import mysql.connector

class Database():
    def __init__(self):
        self.nombre_db = ''
        self.conexion = ''

    def create_database(self, database):
        self.nombre_db = database
        self.conexion = mysql.connector.connect(host="127.0.0.1", user="root", passwd="1112771855", database=self.nombre_db)
        cursor = self.conexion.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.nombre_db)

    def create_table(self, table_db, column_table_db, precio_db):
        cursor = self.conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + table_db + " (id INT AUTO_INCREMENT PRIMARY KEY, " + column_table_db + " VARCHAR(255), " + precio_db + " INT(10))")

    def select(self, table_db):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM " + table_db)
        result = cursor.fetchall()
        return result

    def insert(self, table_db, column_table_db, message_db, precio_db, valor_db):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO " + table_db + " (" + column_table_db + ", " + precio_db + ") VALUES('" + message_db + "', '" + valor_db + "')")
        self.conexion.commit()

    def update(self, table_db, producto_db, nombre_prod_db, precio_db, valor_db, code_db):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE " + table_db + " SET " + producto_db + " = '" + nombre_prod_db + "', " + precio_db + " = " + valor_db + " WHERE id = " + code_db)

        result = cursor.rowcount

        if result > 0:
            self.conexion.commit()
        else:
            return False

    def delete(self, table_db, code_db):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM " + table_db + " WHERE id = " + code_db)
        self.conexion.commit()

