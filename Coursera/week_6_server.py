import asyncio
import tempfile
import os


OK = 'ok\n\n'
ERROR = 'error\nwrong comand\n\n'
PACH = tempfile.gettempdir()

data_json = {
    'key': [(42.83, 1585842597)],
    'key1': [(420000, 1585842594), (42.83, 1585842597)],
    'key2': [(42.83, 1585842597)]
}

def is_file(pach):
    pass

def is_data_digit(data):
    ''' check no the valid data '''
    if data[2].replace('.', '1').isdigit():
        try:
            if data[3].isdigit():
                return True
        except IndexError:
            return False       
    return False


def is_comand(data):
    if data[0] == 'put':
        return put(data)
    if data[0] == 'get':
        if data[1] == '*':
            return get_all(data)
        return get(data)
    else:
        return ERROR


def process_data(data):
    is_file_creat()
    data = data.split()
    resive_data = is_comand(data)
    return resive_data
   

def put(data):
    if is_data_digit(data):
        _, key, val, timestamp = data
        if is_key_creat(key):
            data_json[key].append((val, timestamp))
        print(data_json)
        return OK
    else:
        return ERROR


def is_key_creat(key):
    ''' Creat list() in key if not key '''
    if data_json.get(key):
        return True
    else:
        data_json[key] = []
        return True


def get(data):
    if data_json.get(data[1]):
        all_data = 'ok\n'
        for metric in data_json[data[1]]:
            all_data += f'{data[1]} {metric[0]} {metric[1]}\n'
        all_data += '\n'
        return all_data
    else:
        return OK


def get_all(data):
    all_data = 'ok\n'
    for key in data_json:
        for metric in data_json[key]:
            all_data += f'{key} {metric[0]} {metric[1]}\n'
    all_data += '\n'
    return all_data


def is_file_creat():
    """ Creat file if it is not """

    storage_path = os.path.join(tempfile.gettempdir(),  'storage.data')
    if os.path.exists(storage_path):
        return True
    else:
        with open(storage_path, 'w') as w:
            w.write('{}') 
        return True


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())

   
def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

run_server('127.0.0.1', 8888)