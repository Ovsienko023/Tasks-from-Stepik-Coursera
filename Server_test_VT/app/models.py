from app.scripts.utilites import WrapperDB
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
# class User():


#      def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return '<User {}>'.format(self.username)

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active
        print("User")

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        print("!!!")
        return True

    def is_authenticated(self):
        return False
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
   


@login.user_loader
def load_user(id):
    # 1. Fetch against the database a user by `id` 
     # 2. Create a new object of `User` class and return it.
    #  u = DBUsers.query.get(id)
    return User('bob', '12')