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
    file_path = find_dotenv('.env.test') 
    load_dotenv(file_path, override=True) 
    # Create the new app.
    test_app = app.create_app()
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
    mock_mongo_card.return_value["ToDo"]["All Items"].find = substitute_mongo_api_mock
    response = client.get('/items/get_all_cards')
    assert response.status_code == 200 


@patch('pymongo.MongoClient')
def test_index_page_with_mock2(mock_mongo_card, client):
    mock_mongo_card.return_value["ToDo"]["All Items"].find = substitute_mongo_api_mock
    response = client.get('/items/get_all_cards')
    assert "Test to do item" in response.data.decode()