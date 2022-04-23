
from __future__ import annotations

from typing import Tuple
import socket
import threading


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'
RECEIVED = 'RECEIVED'


class Server(socket.socket):

    __created = False

    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, addr: Tuple[str, int] = ADDR) -> None:

        super().__init__(family=family, type=type)
        super().bind(addr)

        self._family = family
        self._type = type
        self._addr = addr
    
    def __new__(cls: Server, *args, **kwargs) -> Server:

        if not cls.__created:
            cls.__created = True
            return super().__new__(cls, *args, **kwargs)


    def start(self) -> None:

        super().listen()

        print(f'Server is listening on {SERVER}')

        while True:

            conn, addr = super().accept()
            thread = threading.Thread(target=self.__listen_user, args=(conn, addr))
            thread.start()

            print(f'Active connections {threading.activeCount() - 1}')

    def __listen_user(self, conn: socket.socket, addr: Tuple[str, int]) -> None:

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


if __name__ == '__main__':

    test_server = Server()
    test_server.start()

