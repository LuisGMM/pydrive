import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT  = 'utf-8'
DISCONNECT = 'DISCONNECT'
RECEIVED = 'RECEIVED'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


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


