import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))
sock.listen(socket.SOMAXCONN)

coon, add = sock.accept() #Начать принимать соед. Ожидание
while True:
    data = coon.recv(1024)
    if not data:
        break
    print(data.decode("utf8"))

coon.close()
sock.close()
