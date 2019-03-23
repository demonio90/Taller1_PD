import socket
import time

class Client():
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(('localhost', 9091))

        print("[DICCIONARIO BINARIO]")
        time.sleep(1)

        while True:
            self.msj = input(">>: ")
            self.sock.send(self.msj.encode())
            if self.msj == 'cerrar':
                break
            self.response = self.sock.recv(1024)
            print(self.response.decode())

        print("Hasta pronto")
        self.sock.close()

client = Client()