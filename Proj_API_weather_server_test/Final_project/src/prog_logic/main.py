import requests


class Temp():
    def today(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        params = {'q': 'Moscow', 'appid': '9ec5da958d9a8ed6d92b631fc13c11a8', 'units': 'metric'}
        res = requests.get(url, params=params)
        data = res.json()
        temp = 'Temperature in Moscow, today: {}\u2103'
        print(temp.format(data['main']['temp']))
        return  temp.format(data['main']['temp'])

    def temp_five_day(self):
        url = 'http://api.openweathermap.org/data/2.5/forecast?'
        params = {'q': 'Moscow', 'appid': '9ec5da958d9a8ed6d92b631fc13c11a8', 'units': 'metric'}
        res = requests.get(url, params=params)
        data = res.json()

        print('Temperature in Moscow for 5 days:')
        st = str()
        for key in data['list']:
            print('Temp: {}\u2103'.format((key['main']['temp'])))
            st = st + 'Temp: {}\u2103'.format((key['main']['temp'])) + '<br />'
            print('Date: {}'.format((key['dt_txt'])))
            st = st + 'Date: {}'.format((key['dt_txt'])) + '<br />'
        return st

# temp = Temp()
# #temp.temp_five_day()
# temp.today()


