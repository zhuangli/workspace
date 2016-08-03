from socket import *
HOST='localhost'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)
while(True):
    udpSerSock=socket(AF_INET,SOCK_DGRAM)
    udpSerSock.connect(ADDR)
    data=input('>')
    if not data:
        break
    udpSerSock.send(('%s\r\n'%data).encode())
    data=udpSerSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data.strip())
udpSerSock.close()