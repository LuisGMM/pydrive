
from typing import Tuple
import socket


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'


class user(socket.socket):

    def __init__(self, id: str = None, username: str = None, password: str = None, email: str = None,
                 family=socket.AF_INET, type=socket.SOCK_STREAM, addr: Tuple[str, int] = ADDR) -> None:

        super().__init__(family=family, type=type)

        self.id = id
        self.username = username
        self.password = password
        self.email = email

        self.addr = addr

    def connect(self) -> None:
        super().connect(self.addr)

    def send(self, msg: str):

        message: bytes = msg.encode(FORMAT)
        message_length: int = len(message)

        send_length: bytes = str(message_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        super().send(send_length)
        super().send(message)

        return self.recv(2048)


if __name__ == '__main__':

    test_user = user()
    test_user.connect()
    test_user.send('Hello World')
    test_user.send('Hello World')
    test_user.send('Hello World')

    test_user.send(DISCONNECT)
