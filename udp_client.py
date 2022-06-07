import socket

host='127.0.0.1'
port= 4455

connection=(host, port)
bufferSize = 1024

ServerSideSocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    message = input("Input : ")
    ServerSideSocket.sendto(message.encode(), connection)
    message = ServerSideSocket.recvfrom(bufferSize)[0].decode()
    print('Server message: ' + message)
