from unittest import mock
import app
import pytest
from trelloapp import Trello
from todo_item import TodoItem
from dotenv import find_dotenv, load_dotenv
import json
import pymongo
from bson import ObjectId, json_util
from unittest.mock import patch, Mock
from dotenv import load_dotenv  #to invoke .env file
import os

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    # file_path = find_dotenv('.env.test') removed post MONGO connection
    # load_dotenv(file_path, override=True) removed post MONGO connection
    # Create the new app.
    test_app = app.create_app()
    load_dotenv() # added
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def substitute_mongo_api_mock(): ## list
    return  [{
                "_id": "12345",
                "title": "Test to do item",
                "status": "To Do",
                "update_time": "2020-08-01T12:52:06.278Z"
            }]

#works. just client.get('/') triggers redirect and result in 302 error. 
def test_index_page(client):
    response = client.get('/items/get_all_cards')
    assert response.status_code == 200 
    assert response.location == None

def test_index_page2(client):
    response = client.get('/')
    assert response.status_code == 302

@patch('pymongo.MongoClient')
def test_index_page_with_mock(mock_mongo_card, client):
    MONGO_LOGIN = os.getenv("MONGO_LOGIN")  # take .env from dotenv
    MONGO_PASS = os.getenv("MONGO_PASS")  

    myclient = pymongo.MongoClient('mongodb+srv://%s:%s@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority' % (MONGO_LOGIN, MONGO_PASS))    
    mydb = myclient["ToDo"]
    mycollection = mydb["All Items"]

    mock_mongo_card.return_value["ToDo"]["All Items"].find = substitute_mongo_api_mock
    response = client.get('/items/get_all_cards')
    assert response.status_code == 200 


# Cant get below to work!! Get AssertionError assert <MagicMcok.... == {'_id':'1234...} HELP
#@patch('pymongo.MongoClient')
#def test_index_page_with_mock2(mock_mongo_card, client):
#   mock_mongo_card.return_value["ToDo"]["All Items"].find = substitute_mongo_api_mock  # returns a cursor
#   data = [TodoItem.from_mongo_card(card) for card in mock_mongo_card]    
#   assert mock_mongo_card.return_value[0] == {'_id': '123456', 'title': 'Test to do item', 'update_time': '2020-08-01T12:52:06.278Z'}
#   assert data[1]['title'] == "Test to do item"
#   assert "Test to do item" in data
#   assert "12345" in mock_mongo_card
#   assert "2020-08-01T12:52:06.278Z" in mock_mongo_card
#   assert data2[0] == {'_id': '12345', 'title': 'Test to do item', 'update_time': '2020-08-01T12:52:06.278Z'}
#   assert mock_mongo_card[0]['title'] == "Test to do item"