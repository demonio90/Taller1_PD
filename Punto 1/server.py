import socket

class Server():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("localhost",9999))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        global nombre
        nombre = conexion.recv(1024)
        conexion.send("nombre aceptado".encode())

        while True:
            mensaje = conexion.recv(1024)
            print(nombre.decode()+">> "+mensaje.decode())
            conexion.send("recibido".encode())
            if mensaje.decode() == 'cerrar':
                break
        print("Cerrado")
        conexion.close()
        self.mi_socket.close()

server = Server()