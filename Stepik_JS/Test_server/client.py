import requests

url = r'http://127.0.0.1:5000/test'
data = {"login": "Bob", "messages": "I'm the best!"}
a = requests.post(url, json=data)

print(a.content)