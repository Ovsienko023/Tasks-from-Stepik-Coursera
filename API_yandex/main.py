import requests
import json


params = {'key': 'trnsl.1.1.20200101T170917Z.2023ca317ec893c7.e8549916eb75939aa6878a1e7a453489f4302654',
          'text': ''}
params['text'] = input()
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?lang=en-ru&text={text}&key={key}'


go = requests.get(url, params=params)
data = json.loads(go.content)
print(data['text'][1])
