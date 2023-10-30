import socket
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
PORT = 12345
SERVER = socket.gethostbyname(gethostname())
ADDRESS = (SERVER, PORT)
print(ADDRESS)

SERVER.bind(ADDRESS)


while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = SERVER.accept()
    try:
        message = "Content-Type: text/html\r\n"
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = "GET ./Hello World.html"
        #Send one HTTP header line intop socket
        for i in range(0, len(outputdata)):
            connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        error = "Error! File not found."
        connectionSocket.send(error)
        #Close client socket
        connectionSocket.close()



serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data