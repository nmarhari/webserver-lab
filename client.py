#Nassim Marhari
from socket import *
import sys

HEADER = 64
FORMAT = 'UTF-8'

client = socket(AF_INET, SOCK_STREAM)


def send(argv):
    client.connect((sys.argv[1], int(sys.argv[2])))
    msg = ("GET /")
    msg += sys.argv[3]
    msg += (" HTTP/1.1\r\nHost:")
    msg += sys.argv[1]
    msg += ("\r\nConnection: close\r\n\r\n")
    msg = msg.encode()
    client.send(bytes(msg))
    response = client.recv(4096)
    print(response.decode())


send(sys.argv)
