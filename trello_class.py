import os
from dotenv import load_dotenv 
load_dotenv()

class TrelloItem:
    list_id_ToDo = os.getenv("list_id_ToDo")
    list_id_Pending = os.getenv("list_id_Pending")
    list_id_Done = os.getenv("list_id_Done")

    def __init__(self, id, title, status): 
        self.id = id
        self.title = title
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls.from_list_id(card["id"], card["name"], card["idList"])

    @classmethod
    def from_list_id(cls, id, title, list_id):
        status = None
        if list_id == cls.list_id_ToDo:
            status = "To Do"
        elif list_id == cls.list_id_Pending:
            status = "Pending"
        elif list_id == cls.list_id_Done:
            status = "Done"
        return cls(id, title, status)

