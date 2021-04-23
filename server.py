import socket
import random

FORMAT = "UTF-8"
LOCALHOST = "127.0.0.1"


def random_port():
    return random.randint(20000, 30000)


my_socket = socket.socket()

addr_and_port = (LOCALHOST, random_port())
my_socket.bind(addr_and_port)
print(f"Started socket on {addr_and_port}")

my_socket.listen(10)

conn, addr = my_socket.accept()
print("Got connection", conn, addr)
data = conn.recv(1024)

conn.send(f"HTTP/1.1 200 OK\n Content-Lenght: 100\n Content-Type: text/html\n\n {data.decode(FORMAT)}".encode(FORMAT))

my_socket.close()
