import asyncio
import tempfile
import json
import os


OK = 'ok\n\n'
ERROR = 'error\nwrong command\n\n'
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data_json = dict()



class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())
    


    def is_data_digit(self, data):
        ''' check no the valid data '''
        if data[2].replace('.', '1').isdigit():
            try:
                if data[3].isdigit():
                    return True
            except IndexError:
                return False       
        return False


    def is_comand(self, data):
        if (len(data) <= 1) or (len(data) > 4):
            return ERROR
        if data[0] == 'put':
            return self.put(data)
        if data[0] == 'get':
            if data[1] == '*':
                return self.get_all(data)
            return self.get(data)
        else:
            return ERROR


    def process_data(self, data):
        data = data.split()
        resive_data = self.is_comand(data)
        return resive_data


    def is_key_creat(self, key):
        ''' Creat list() in key if not key '''
        if data_json.get(key):
            return True
        else:
            data_json[key] = []
            return True


    def is_replay(self, key, val, timestamp):
        for i in range(len(data_json.get(key))):
            keys = data_json.get(key)[i]
            if keys[1] == timestamp:
                data_json.get(key)[i] = (float(val), int(timestamp))
                return False
            
        return True 



    def put(self, data):
        if self.is_data_digit(data):
            _, key, val, timestamp = data
            if ((self.is_key_creat(key)) 
                and ((float(val), int(timestamp)) 
                not in data_json[key]) 
                and (self.is_replay(key, float(val), int(timestamp)))):

                data_json[key].append((float(val), int(timestamp)))
            return OK
        else:
            return ERROR


    def get(self, data):
        if len(data) <= 2:
            #print(data[1])
            if data_json.get(data[1]):
                all_data = 'ok\n'
                for metric in data_json[data[1]]:
                    all_data += f'{data[1]} {metric[0]} {metric[1]}\n'
                all_data += '\n'
                return all_data
            else:
                return OK
        else:
            return ERROR


    def get_all(self, data):
        all_data = 'ok\n'
        for key in data_json:
            for metric in data_json[key]:
                all_data += f'{key} {metric[0]} {metric[1]}\n'
        all_data += '\n'
        return all_data


   
def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol,host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

# run_server('127.0.0.1', 8888)