from socket import socket
from threading import Thread
import  sys



class Client(Thread):

    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            #try:
                # Recibir datos del cliente.
            input_data = self.conn.recv(1024)
            print(input_data)
            #except error:
            #print("[%s] Error de lectura." % self.name)
            #break
            #else:
                # Reenviar la información recibida.
            if input_data:
                self.conn.send(input_data)


def main():
    s = socket()

    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(0)

    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)

if __name__ == "__main__":
    main()