from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pytest
import os
from threading import Thread
import app
from trelloapp import Trello
from dotenv import load_dotenv

#file_path = find_dotenv('.env.test')
#load_dotenv(file_path, override=True)
username = os.getenv('username1')
password = os.getenv('password')
url = os.getenv('url')
myboard = os.getenv('myboard')

# Module scope re-uses the fixture; note the webdriver chromedriver.exe is stored under python script folder
@pytest.fixture(scope='module')
def driver():
    with webdriver.Chrome() as driver:
        yield driver

#r"C:\Users\DevOps-Feng\Desktop\DevOps\git-playground\DevOps-Course-Starter\drivers\chromedriver.exe

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = Trello().create_test_board("Tasks_Selenium")
    #First of all, you're setting TRELLO_BOARD_ID, but TrelloApp.py is doing board_id= os.getenv("board_id")
    #os.environ['TRELLO_BOARD_ID'] = board_id 
    Trello.board_id = board_id
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)
    Trello().delete_test_board(board_id)

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.current_url == 'http://localhost:5000/items/get_all_cards'
    assert driver.title == 'To-Do App'

##below finds the add item button and clicks on it, adds a new item and returns back to home page.
##assert then checks the url and that new value is added.  
def test_add_item_todo(driver, test_app):
    driver.get('http://localhost:5000/')
    time.sleep(2)
    driver.find_element_by_partial_link_text('Click here to add new card to ToDo').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name('card_name').send_keys('NewItem for Selenium')
    time.sleep(2)
    driver.find_element_by_name('card_name').send_keys(Keys.ENTER)
    time.sleep(5)
    new_card = driver.find_element_by_css_selector("input[value=\"NewItem for Selenium\"]")
    assert new_card.get_attribute('value') == 'NewItem for Selenium'
    assert driver.current_url == 'http://localhost:5000/items/get_all_cards'



#def test_trello(driver):
#    driver.get(url)
#    time.sleep(2)
#    driver.find_element_by_id('user').send_keys(username)
#    time.sleep(2)
#
#    loginclick = driver.find_elements_by_id('login')
#    for loginclick in loginclick: 
#        loginclick.send_keys(Keys.ENTER)
#    time.sleep(2)

#    loginpass = driver.find_element_by_id('password').send_keys(password)
#    time.sleep(2)

#    login4real = driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
#    time.sleep(12)
#
#    driver.get(myboard)
#    time.sleep(5)
#    assert driver.current_url == myboard
    