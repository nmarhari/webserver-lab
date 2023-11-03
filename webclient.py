#Nassim Marhari
from socket import *
import sys

HEADER = 64
FORMAT = 'UTF-8'

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.121", 12345))

def send():
    msg = ("GET /HelloWorld.html HTTP/1.1\r\nHost:192.168.1.121\r\nConnection: close\r\n\r\n".encode())
    client.send(bytes(msg))
    response = client.recv(4096)
    print(response.decode())


send()
