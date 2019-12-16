from flask import Flask, escape, request
from src.prog_logic.main import Temp

app = Flask(__name__)                         #  app кземпляр сервера(__name__)-лужебная переменная

@app.route('/')                               # / - адресс нашего сервера 127...../
def hello():
    t = Temp()
    t.temp_five_day()
    return str(t.temp_five_day()) #f'Hello, {escape(name)}!'
app.run('0.0.0.0', port=8080)                 # запуск сервера port='любой можно для SSH='

