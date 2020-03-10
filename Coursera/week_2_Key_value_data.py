import os.path
import argparse
import tempfile
import os
import json


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--val', help='value in storage.data')
    parser.add_argument('-k', '--key', help='key in storage.data')
    args = parser.parse_args()
    return (args.key, args.val)


def is_file():
    """ return True, if file available else: return False. """
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    return os.path.exists(storage_path)


def cread_file_data():
    if not is_file():
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'w') as writer:
            writer.write('{}')
    return is_file()


def key_and_val(key, val):
    if key and val:
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'r') as r:
            data = r.read()
            data_json = json.loads(data)

        if data_json.get(key):
            data_json[key].append(val)
        else:
            data_json[key] = [val]

        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'w') as w:

            data = json.dumps(data_json)
            w.write(data)


def key_not_val(key):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as r:
        data = r.read()
        data_json = json.loads(data)

    if key in data_json:
        print(', '.join(data_json[key]))

    else:
        print(None)


def main():
    if is_file():
        args_key_val = create_parser()
        if args_key_val[1]:
            key_and_val(*args_key_val)

        elif args_key_val[1] is None:
            key_not_val(args_key_val[0])
    else:
        cread_file_data()
        main()

main()
