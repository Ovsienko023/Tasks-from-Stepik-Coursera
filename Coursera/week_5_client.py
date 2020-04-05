import socket
import time


class ClientError(Exception):
    """ I'm Error classa Client! """
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))


    def put(self, metrica, numb_val, timestamp=None):
        """ Data transfer to the server """

        timestamp = timestamp or int(time.time())
        data = 'put {} {} {}\n'.format(metrica, numb_val, timestamp)
        self.sock.sendall(data.encode("utf8"))
        otvet = self.sock.recv(1024)
        print(otvet.decode("utf8"))
        if otvet.decode('utf8') == "error\nwrong command\n\n":
            raise ClientError

    
    def get(self, data_key):
        """ Receiving data from the server """

        if data_key == '*':
            self.sock.sendall('get *\n'.encode("utf8"))
            data_r = self.sock.recv(1024)
        else:
            data = 'get {}\n'.format(data_key)
            self.sock.sendall(data.encode("utf8"))
            data_r = self.sock.recv(1024)

        if data_r.decode('utf8') == "error\nwrong command\n\n":
            raise ClientError

        if data_r.decode('utf8') == "ok\n\n":
            return {}
        else:
            try:
                fin_data = dict()
                data_r = data_r.decode('utf8').split('\n')
                for line in data_r:
                    if line and (line not in 'ok'):
                            metrica, numb_val, timestamp = line.split()
                            #print(metrica, numb_val, timestamp)
                            if fin_data.get(metrica):
                                fin_data[metrica].append((int(timestamp), float(numb_val)))
                            else:
                                fin_data[metrica] = [(int(timestamp), float(numb_val))]

                for met in fin_data:
                    fin_data[met] = sorted(fin_data[met], key=lambda typ: typ[0])

                return fin_data
            except:
                raise ClientError
    

    def close(self):
        try:
            self.sock.close()
        except socket.error as err:
            raise ClientError("Error. Do not close the connection", err)

### TEST
client = Client("127.0.0.1", 8888)
#client.put("eardrum.memory", 4200000)
client.put('key', 12.0, 1180864247)
client.put('key', 12.0, 1180864247)
client.put('key', 12.0, 1180864247)
client.put('key', 12.0, 1180864247)
print(client.get('key'))
#print(client.get('wrong command test\n'))
# # client.put("hi")  
# #client = Client("127.0.0.1", 8888, timeout=15)
