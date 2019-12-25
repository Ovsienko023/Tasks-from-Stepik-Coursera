from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


# "/about" Это ссылка на следующую страницу
@app.route("/about")
def about():
    return ("About Me")

    
if (__name__ =="__main__"):
    app.run(debug=True)