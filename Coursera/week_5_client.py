import socket


# with socket.create_connection(("127.0.0.1", 10001)) as sock:
#     sock.sendall("ping".encode("utf8"))
#     data = sock.recv(1024)
#     print(data.decode("utf8"))



class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.connect(("127.0.0.1", 10001))


    def put(self, data):
        """ Data transfer to the server """
        self.sock.sendall(data.encode("utf8"))

    
    def get(self, data_key):
        """ Receiving data from the server """
        self.sock.sendall(data_key.encode("utf8"))
        data_r = self.sock.recv(1024)
        print(data_r.decode("utf8"))
    
            


# sock = socket.socket() # Для соединения к серверу
# sock.connect(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()

client = Client("127.0.0.1", 10001)
#client.put('!!!')
client.get('key')

client.put("hi")


#### SERVER

# import socket


# with socket.socket() as sock:
#     sock.bind(("", 10001))
#     sock.listen(5)

#     while True:
#         coonect, addres = sock.accept()
#         print(addres)
#         with coonect:
#             while True:
#                 data = coonect.recv(1024)
#                 if not data:
#                     break
#                 print(data.decode("utf8"))
#                 coonect.send("value".encode("utf8"))
    
