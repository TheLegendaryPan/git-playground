import os
from threading import Thread
import trelloapp_class as tre
import pytest
from selenium import webdriver
import json
import app

@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome(r"C:\Users\Feng and Li\Desktop\DevOps\git-playground\DevOps-Course-Starter\drivers\chromedriver.exe") as driver:
        yield driver

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    new_board = tre.Trello().create_board_4_test('Test Selenium2')
    board_id_json = json.loads(new_board)
    board_id_extract=(board_id_json['id'])
    
    os.environ['TRELLO_BOARD_ID'] = board_id_extract

    # construct the new application --- HOW?
    application = app.create_app()
    
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    #Tear Down
    thread.join(1)
    delete_board = tre.Trello().delete_board_4_test(board_id_extract)


def test_1(test_app):
    x = 10
    y = 10
    assert x == y

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.current_url == 'http://localhost:5000/items/get_all_cards'
