from flask_login import UserMixin
import pymongo
from dotenv import load_dotenv  #to invoke .env file
import os

load_dotenv()
MONGO_LOGIN = os.getenv("MONGO_LOGIN")  # take .env from dotenv
MONGO_PASS = os.getenv("MONGO_PASS")  # take .env from dotenv

myclient = pymongo.MongoClient('mongodb+srv://%s:%s@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority' % (MONGO_LOGIN, MONGO_PASS))    
mydb = myclient["ToDo"]
mycollection = mydb["user"]


class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        myquery = {"name": ObjectId(name)}
        user = mycollection.find_one(myquery)
        if not user:
            return None

    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        db.commit()