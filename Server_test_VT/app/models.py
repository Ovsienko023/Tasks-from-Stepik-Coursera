from app.scripts.utilites import WrapperDB
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User():
    def __init__(self, name, password, active=True):
        self.name = name
        self.password = password
        self.active = active

    def get_id(self):
        # print(f"{self.name}-name {self.password}-password  --вызов get_id'")
        try:
            _id = str(WrapperDB().get_id(self.name, self.password))
        except TypeError:
            return None
        return _id

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        print("!!!")
        return True

    def is_authenticated(self):
        print("is_authenticated")
        return True
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)


@login.user_loader
def load_user(id):
    # print(id, '-id!') 
    try:
        id = str(id)
        data = WrapperDB().get_user(id)
        # print(data)
        name, password = data
        user = User(name, password)
    except:
        return None
    return user
