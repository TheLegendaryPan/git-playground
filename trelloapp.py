import requests
import os
from flask import Flask, render_template
import json
from dotenv import load_dotenv  #to invoke .env file
load_dotenv()

trelloapp = Flask(__name__)

class Trello:
    APP_KEY = os.getenv("APP_KEY")  # take .env from dotenv
    APP_TOKEN = os.getenv("APP_TOKEN")
    board_id= os.getenv("board_id")
    list_id_ToDo = os.getenv("list_id_ToDo")
    list_id_Pending = os.getenv("list_id_Pending")
    list_id_Done = os.getenv("list_id_Done")

    def get_card(self):
        url = 'https://api.trello.com/1/cards/5ef1186efc0b5b3a63063ecd'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}

        response=requests.request("GET", url, headers=headers, params=query)
        print(self.APP_KEY)
        print(self.APP_TOKEN)
        return response.text

    def get_all_cards_from_board(self):
        url = f'https://api.trello.com/1/boards/{self.board_id}/cards/'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}

        response=requests.request("GET", url, headers=headers, params=query)
        return response.text
        print("my board id is:" + self.board_id)

    def get_all_cards_from_todo_list(self):
        url = f'https://api.trello.com/1/lists/{self.list_id_ToDo}/cards'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}
        response=requests.request("GET", url, headers=headers, params=query)
        return response.text  

    def get_all_cards_from_done_list(self):
        url = f'https://api.trello.com/1/lists/{self.list_id_Done}/cards'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}
        response=requests.request("GET", url, headers=headers, params=query)
        return response.text  

    def get_all_lists_from_board(self):
        url = f'https://api.trello.com/1/boards/{self.board_id}/lists/'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}
        response=requests.request("GET", url, headers=headers, params=query)
        return response.text  

    def get_card_name_and_id(self):
        all_card_details = []
        all_card_details = json.loads(self.get_all_cards_from_board())
        for card in all_card_details:
            print(card['id'] + ' : ' + card['name'])

    def get_list_name_and_id(self):
        all_list_details = []
        all_list_details = json.loads(self.get_all_lists_from_board())
        for list_status in all_list_details:
            print(list_status['id'] + ' : ' + list_status['name'])

    def create_new_card(self, card_name):
        url = f'https://api.trello.com/1/cards/'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN, "idList": self.list_id_ToDo, "name": {card_name}}
        response=requests.request("POST", url, headers=headers, params=query)
        return response.text

    def move_card_to_done(self, card_id):
        url = f'https://api.trello.com/1/cards/{card_id}'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN, "idList": self.list_id_Done}
        response=requests.request("PUT", url, headers=headers, params=query)
        return response.text

    def move_card_to_do(self, card_id):
        url = f'https://api.trello.com/1/cards/{card_id}'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN, "idList": self.list_id_ToDo}
        response=requests.request("PUT", url, headers=headers, params=query)
        return response.text
    
    def delete_card(self, card_id):
        url = f'https://api.trello.com/1/cards/{card_id}'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}

        response = requests.request("DELETE", url, headers=headers, params=query)

    def create_test_board(self, name):
        url = f'https://api.trello.com/1/boards/'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN, "name": name}

        response = requests.request("POST", url, headers=headers, params=query)
        return response.text

    def delete_test_board(self, id):
        url = f'https://api.trello.com/1/boards/{id}'
        headers = {"Accept": "application/json"}
        query = {"key": self.APP_KEY, "token": self.APP_TOKEN}

        response = requests.request("DELETE", url, params=query)

# result_card=Trello()
# print(result_card.get_card())

# result_cards_board=Trello()
# print(result_cards_board.get_all_cards_from_board())

# result_cards_todo=Trello()
# print(result_cards_todo.get_all_cards_from_todo_list())

# result_cards_done=Trello()
# print(result_cards_done.get_all_cards_from_done_list())

# result_lists_board=Trello()
# print(result_lists_board.get_all_lists_from_board())

# result_card_and_id=Trello()
# print(result_card_and_id.get_card_name_and_id())

# result_list_and_id=Trello()
# print(result_card_and_id.get_list_name_and_id())

# result_new_card=Trello()
# result_new_card.create_new_card('Test')

#result_move_to_done=Trello()
#result_move_to_done.move_card_to_done('5ef1186efc0b5b3a63063ecd')

# result_move_to_do=Trello()
# result_move_to_do.move_card_to_do('5ef1186efc0b5b3a63063ecd')

#result_delete_card=Trello()
#result_delete_card.delete_card('5f1dc511b904ac8ef068bd0c')

#result_create_board=Trello()
#result_create_board.create_board_4_test('Test 11')

#result_delete_board=Trello()
#result_delete_board.delete_board_4_test('5f1dc5c68a5b70844aab9209')

## ALL ABOVE TESTS ARE VALID ## 
