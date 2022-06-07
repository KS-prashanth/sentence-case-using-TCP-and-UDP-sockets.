import socket
import os
from _thread import *
from threading import Thread
ServerSideSocket = socket.socket()
host = '127.0.0.1'

port = 4455
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('SERVER STARTED')
ServerSideSocket.listen(5)
def multi_threaded_client(connection,flags=False):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        if flags == True:

            response = 'Server message: ' + data.decode('utf-8')[::-1]
        else:
            if data.decode('utf-8').isupper():  
                response = 'Server message: ' + data.decode('utf-8').lower()
            else:
                response = 'Server message: ' + data.decode('utf-8').upper()
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    ThreadCount += 1
    if (ThreadCount == 1):
        start_new_thread(multi_threaded_client, (Client,False, ))
    else:
        start_new_thread(multi_threaded_client, (Client,True, ))

ServerSideSocket.close()