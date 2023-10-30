#import socket module
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
serverSocket.bind(("localhost", 12345))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = "HelloWorld.html"
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        serverSocket.send("HTTP/1.1 200 OK")
        serverSocket.send("\r\n")
        #Send the content of the requested file to the client
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