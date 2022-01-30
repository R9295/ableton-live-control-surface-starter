import socket
import errno
import time
import threading

sync_addr = ("127.0.0.1", 9000)
client_addr = ("127.0.0.1", 9001)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setblocking(0)
server.bind(client_addr)


def listen():
    try:
        while True:
            data, addr = server.recvfrom(65536)
            print("\n%s" % data.decode())
    except socket.error as e:
        if e.errno == errno.EAGAIN:
            pass
    time.sleep(1)
    listen()


def send_to_server(msg):
    client.sendto(msg, sync_addr)


listener_thread = threading.Thread(target=listen)
listener_thread.daemon = True
listener_thread.start()

while True:
    data = input(">>>")
    if data == "":
        pass
    else:
        send_to_server(data.encode())
