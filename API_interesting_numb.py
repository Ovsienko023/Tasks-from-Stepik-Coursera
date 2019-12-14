import requests
import sys


def intrest_num(numb):
    api_url = 'http://numbersapi.com/{}/?'
    params = {'trivia': 'trivia', 'default': 'None'}
    res = requests.get(api_url.format(numb), params=params)
    data = res.content
    if data != b'None':
        print("Interesting")
    else:
        intrest_num_2(numb)


def intrest_num_2(numb):
    api_url = 'http://numbersapi.com/{}/math/?'
    params_math = {'default': 'None'}
    res_num = requests.get(api_url.format(numb), params=params_math)
    data_num = res_num.content
    if data_num == b'None':
        print("Boring")
    else:
        print("Interesting")


for line in sys.stdin:
    line = line.rstrip()
    intrest_num(line)
