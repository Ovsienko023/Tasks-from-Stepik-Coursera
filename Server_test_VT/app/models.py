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
data = {'bob': 1, 'kop': 2}
# data1 = {'1': User('bob', '123')}
class User():
    def __init__(self, name, password, active=True):
        self.name = name
        self.password = password
        self.active = active
        # self.get_id = 'qweqw'

    def get_id(self):
        # u = 'Tr'
        print(f"{self.name}-name {self.password}-password  --вызов get_id'")
        id_ = data.get(self.name) # найти id по имени
        return id_

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
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
   
data1 = {'1': User('bob', '123')}

@login.user_loader
def load_user(id):
    print(id, '-id!') 
    # print(type(name))
    # 1. Fetch against the database a user by `id` 
     # 2. Create a new object of `User` class and return it.
    #  u = DBUsers.query.get(id)
    # return User.query.get(int(id))
    user = data1.get(id) # пойти в БД и найти пользователя по id, потом сделать Юзера если такой есть, если нет None
    return user
