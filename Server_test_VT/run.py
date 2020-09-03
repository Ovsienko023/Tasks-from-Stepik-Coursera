from app import app
# # print(app.config)
# for i, j in app.config.items():
#     print(i,'---', j)
# app.run()
# app.config['SERVER_NAME'] = '0.0.0.0'
# print(app.config['SERVER_NAME'])

# from flask import Flask
# from config import Config


# app = Flask(__name__)
# app.config.from_object(Config)
# app.config['SERVER_NAME'] = '0.0.0.0:8888'
app.config['SERVER_NAME'] = None
app.run()