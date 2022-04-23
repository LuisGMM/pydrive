
from typing import Tuple
import socket
import threading


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT  = 'utf-8'
DISCONNECT = 'DISCONNECT'
RECEIVED = 'RECEIVED'

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)


def handle_client(conn, addr):
    print(f'New connection {addr} .')
    connected: bool = True

    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)

        if not msg_length:
            continue
        
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT:
            connected = False
            print(f'{addr} disconnected.')
            continue

        print(f'{addr} {msg}.')
        conn.send(RECEIVED.encode(FORMAT))

    conn.close()


def start():

    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:

        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f'Active connections {threading.activeCount() - 1}')



class server(socket.socket):

    def __init__(self, family = socket.AF_INET, type = socket.SOCK_STREAM, addr: Tuple[str, int] = ADDR) -> None:
        super().__init__(family=family, type=type)
        self.bind(addr)






if __name__ == '__main__':
    start()
