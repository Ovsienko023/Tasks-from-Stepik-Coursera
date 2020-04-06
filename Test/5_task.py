string = 'python.py'


def num_symbol(sting):
    data = dict()
    for i in string:
        key = i
        val = sting.count(key)
        data[key] = val
    return data


print(num_symbol(string))
