from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest
import os
from threading import Thread
import app
from trelloapp import Trello
from dotenv import load_dotenv
import json

# Module scope re-uses the fixture; the webdriver is auto updated by the ChromeDriverManager to avoid outdated version issue
@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
  # opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(ChromeDriverManager().install(), options=opts) as driver:
        yield driver

@pytest.fixture(scope='module')
def test_app():
    os.environ['LOGIN_DISABLED']='True' ##added this to pick up LOGIN_DISABLED flag from flask_config to turn off authenticatin for testing
    os.environ['ANON_USER'] = 'TheLegendaryPan'## added as part of module 10
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)

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