from socket import *
import threading
import time

def send(sock):
    while True:
        send_data = input(">>>")
        sock.send(send_data.encode('utf-8'))

def receive(sock):
    while True:
        recv_data = sock.recv(1024)
        print("USER : ", recv_data.decode('utf-8'))

PORT = 8080

# 소켓생성밑 포트번호 8080으로 bind, 접속가능 인원 1명
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', PORT))
serverSock.listen(1)

print("%d번포트 접속 대기중"%PORT)


#클라이언트 소켓과 접속 성공
connection_sock, addr = serverSock.accept()

print(str(addr) + "에서 접속이 확인되었습니다")

sender = threading.Thread(target=send, args=(connection_sock,))
receiver = threading.Thread(target=receive, args=(connection_sock, ))

sender.start()
receiver.start()

while(1):
    time.sleep(0.1)
    pass

