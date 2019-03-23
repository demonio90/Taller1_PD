import socket
from db import Database

class Server():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("127.0.0.1", 9993))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        database = Database()
        database.create_database("crud")
        database.create_table("usuarios", "nombre", "edad")

        while True:
            while True:
                conexion.send("Opciones:\n1. Ver"
                              "\n2. Agregar"
                              "\n3. Editar"
                              "\n4. Eliminar"
                              "\n0. Salir\n".encode())
                try:
                    mensaje = conexion.recv(1024)
                    if int(mensaje) > 4:
                        mensaje = "error"
                    mensaje = int(mensaje)
                    break
                except ValueError:
                    conexion.send("\n\n<<Opción Invalida>>\n\n".encode())

            print(">>: "+str(mensaje))

            if(mensaje == 0):
                break

            if(mensaje == 1):
                usuarios = database.select("usuarios")
                conexion.send("\n<<Cargando presione ENTER>>\n".encode())

                for usuario in usuarios:
                    conexion.send(("\n [Id]: "+str(usuario[0])).encode())
                    conexion.send(("\n [Nombre]: "+str(usuario[1])).encode())
                    conexion.send(("\n [Edad]: "+str(usuario[2])).encode())
                    conexion.send("\n\n****************************\n".encode())

            if(mensaje == 2):
                conexion.send("[Nombre del usuario]: ".encode())
                nombre = conexion.recv(1024).decode()
                conexion.send("[Edad del usuario]: ".encode())
                edad = conexion.recv(1024).decode()
                database.insert("usuarios", "nombre", str(nombre), "edad", str(edad))

            if(mensaje == 3):
                conexion.send("[Ingrese el id del usuario que desea editar]".encode())
                id = conexion.recv(1024).decode()
                conexion.send("[Nombre del usuario]: ".encode())
                nombre = conexion.recv(1024).decode()
                conexion.send("[Edad del usuario]: ".encode())
                edad = conexion.recv(1024).decode()


                result = database.update("usuarios", "nombre", str(nombre), "edad", str(edad), id)

                if result == False:
                    conexion.send("\n[El usuario no existe]\n".encode())

            if(mensaje == 4):
                conexion.send("[Ingrese el id del usuario que desea eliminar]".encode())
                id = conexion.recv(1024).decode()
                database.delete("usuarios", id)

        print("\n\n<<Presione 'ENTER' para salir>>\n\n")
        conexion.close()
        self.mi_socket.close()

server = Server()