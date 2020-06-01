from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['POST'])
def test_func():
    data = request.json
    print(data)
    return '{"status": True}'# render_template('index.html')


app.run()