import os
from dotenv import load_dotenv 
from datetime import datetime, date
load_dotenv()

class TodoItem: # renamed from TrelloItem and renamed file from trello_class.py to todo_item.py
    list_id_ToDo = os.getenv("list_id_ToDo")
    list_id_Pending = os.getenv("list_id_Pending")
    list_id_Done = os.getenv("list_id_Done")

    def __init__(self, id, title, status, update_time): 
        self.id = id
        self.title = title
        self.status = status
        self.update_time = update_time

    @classmethod
    def from_trello_card(cls, card):
        update_time = datetime.strptime(card["dateLastActivity"],'%Y-%m-%dT%H:%M:%S.%fZ') #date converstion from trello string to date
        return cls.from_list_id(card["id"], card["name"], card["idList"], update_time)

    @classmethod # new class for mongo DB data
    def from_mongo_card(cls, card):
#       update_time = datetime.strptime(card["update_time"],'%Y-%m-%dT%H:%M:%S.%fZ') #date converstion from trello string to date
        return cls(card["_id"], card["title"], card["status"], card["update_time"])

    @classmethod
    def from_list_id(cls, id, title, list_id, update_time):
        status = None
        if list_id == cls.list_id_ToDo:
            status = "To Do"
        elif list_id == cls.list_id_Pending:
            status = "Pending"
        elif list_id == cls.list_id_Done:
            status = "Done"
        return cls(id, title, status, update_time)

