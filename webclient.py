from socket import *
import sys

FORMAT = 'UTF-8'
HEADER = 64

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.121", 12345))

def send(message):
    msg = message.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)

send("Hello planet!")
