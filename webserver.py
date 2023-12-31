#import socket module
#modified by Nassim Marhari
from socket import *
import sys
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Main thread that listens for clients at a fixed port (12345)
serverSocket.bind(("192.168.1.121", 12345))
serverSocket.listen(1)

def start():
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        #When it receives a TCP connection, set up TCP connection
        #through another port in a separate thread
        thread = threading.Thread(target=connect, args=(connectionSocket, addr))
        thread.start()
        
def connect(connectionSocket, addr):
    #Show which port the TCP connection is on
    print('Connected from: ', addr)
    while True:
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            break
        except IOError:
            #Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><head/><body><strong>404 Not Found</strong></body></html>".encode())
            #Close client socket
            connectionSocket.close()
            break
            
start()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data