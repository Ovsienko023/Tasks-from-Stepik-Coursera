from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ksjbjshevlwvwkevl2'

menu = [{"name": "Главное меню", "url": "mainmenu"},
        {"name": "О сайте", "url": "about"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
@app.route("/mainmenu")
def index():
    return render_template("index.html", title="Главное меню", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О сайте", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():        
    if request.method == "POST":
        print(request.form) # (это dict) сюда приходят данные с формы contact.html 
        if len(request.form["username"]) > 2: # тестовый вариант проверки на корректное заполнение формы
            flash('Сообщение отправлено', category='success')
        else:
            flash("Ошибка отправки")
    return render_template("contact.html", title="Обратная связь", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
