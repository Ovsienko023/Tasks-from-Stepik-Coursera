import pymongo
import os
import json
import sys
import time
from bson.objectid import ObjectId
OS = sys.platform

conf = {"Data_Base":{"host": "mongodb://127.0.0.1", "port": "27017"}}


class ConnectDB():
    def __init__(self):
        self.info_db = self.get_info_db()
        self.conn = pymongo.MongoClient(*self.info_db)
        self.db = self.conn.mydb

    def get_info_db(self):
        info_db = conf['Data_Base']
        host, port = info_db['host'], info_db['port']
        return host, int(port)


class WrapperDB:
    def __init__(self):
        self.db = ConnectDB().db
        self.coll_users = self.db.users
        self.coll_message = self.db.message
    
    def is_authentication(self, login, password) -> bool:
        print(login, password)
        find = self.coll_users.find_one({"user_name": login,
                                         "password": password})
        print(find)
        if find:
            return True
        return False
    
    def registration(self, login, password) -> bool:
        doc = {"user_name": login, "password": password, "friends": []}
        if self.coll_users.insert_one(doc):
            return True
        return False

    def is_user(self, login) -> bool:
        data = self.coll_users.find({"user_name": login})
        status = [user for user in data]
        print(status)
        if status:
            return True
        return False
