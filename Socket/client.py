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
        print("admin : ", recv_data.decode('utf-8'))

PORT = 8080

client_sock = socket(AF_INET, SOCK_STREAM)
client_sock.connect(('127.0.0.1', PORT))

print("연결 확인되었습니다.")

sender = threading.Thread(target=send, args=(client_sock,))
receiver = threading.Thread(target=receive, args=(client_sock, ))

sender.start()
receiver.start()

while(1):
    time.sleep(0.1)
    pass
