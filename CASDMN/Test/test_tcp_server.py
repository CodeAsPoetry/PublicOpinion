from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')

    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)


    while True:
        data = tcpCliSock.recv(BUFSIZ)

        data = str(data, encoding='utf-8')
        print(data)

        data = bytes(data, encoding='utf-8')
        tcpCliSock.send(data)

        if not data:
            tcpCliSock.close
            break


tcpSerSock.close