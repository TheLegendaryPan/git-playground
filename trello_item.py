class TrelloItem:
    def __init__(self, id, title, list_id): 
        self.id=id
        self.title=title
        self.list_id=list_id

    @classmethod
    def from_trello_card(cls, trello_card):
        return cls(trello_card["id"], trello_card["name"], trello_card["idList"])