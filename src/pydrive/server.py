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


