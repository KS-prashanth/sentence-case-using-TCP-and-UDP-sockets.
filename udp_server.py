import socket

host  = "127.0.0.1"
port    = 4455
bufferSize  = 1024
ServerSideSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ServerSideSocket.bind((host, port))
count  = 0
stationary  = {}
print('Socket is listening..')
while True:
    
    conn, addr = ServerSideSocket.recvfrom(bufferSize)
    
    if addr not in stationary.keys():
        count += 1
        print(f"Client {count} Connected")
        stationary[addr] = count
    
    # print("Message received :", conn.decode())
    if stationary[addr] == 1:
        data = conn.decode()
        if data.isupper():
            data = data.lower()
        else:
            data = data.upper()
            
        
        ServerSideSocket.sendto(data.encode(), addr)
    else:
        
        ServerSideSocket.sendto(conn.decode()[::-1].encode(), addr)