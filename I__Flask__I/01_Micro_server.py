from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return ("Home Page")

# "/about" Это ссылка на следующую страницу
@app.route("/about")
def about():
    return ("About Me")


    
if (__name__ =="__main__"):
    app.run(debug=True)