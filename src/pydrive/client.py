import socket


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT  = 'utf-8'
DISCONNECT = 'DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048))



send('Hello World')
send('Hello World')
send('Hello World')

send(DISCONNECT)


class user(socket.socket):

    def __init__(self, id: str, username: str, password: str, email: str, family = socket.AF_INET, type = socket.SOCK_STREAM) -> None:
        
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def connect(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
