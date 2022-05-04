
import pickle as p
from typing import Tuple, Union
import socket


from pydrive.core.filemanager import Item


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'


class User(socket.socket):

    def __init__(self, id: Union[None, str] = None, username: Union[None, str] = None , password: Union[None, str] = None, email: Union[None, str] = None,
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


def main():

    test_user = User()
    test_user.connect()
    test_user.send('Hello World')
    test_user.send(input('Message: '))
    test_user.send(DISCONNECT)


if __name__ == '__main__':
    main()
