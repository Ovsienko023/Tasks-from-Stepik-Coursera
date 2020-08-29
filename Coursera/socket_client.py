import socket


sock = socket.socket() # Для соединения к серверу
sock.connect(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf8"))
sock.close()


# send, sendall или recv/ получение данных