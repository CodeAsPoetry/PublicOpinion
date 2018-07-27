from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    data = bytes(data, encoding='utf-8')

    if not data:
        break
    tcpCliSock.send(data)

    recv_data = tcpCliSock.recv(BUFSIZ)
    if not recv_data:
        break

    recv_data = str(recv_data, encoding='utf-8')
    print(recv_data)




tcpCliSock.close()