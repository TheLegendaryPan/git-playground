from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pytest
import os

#driver = webdriver.Chrome(r"C:\Users\Feng and Li\Desktop\DevOps\git-playground\DevOps-Course-Starter\drivers\chromedriver.exe")

username = os.getenv('username')
password = os.getenv('password')
url = os.getenv('url')
myboard = os.getenv('myboard')

# driver.get(url)
# time.sleep(1)
# driver.find_element_by_id('user').send_keys(username)
# time.sleep(2)

# loginclick = driver.find_elements_by_id('login')
# for loginclick in loginclick: 
#     loginclick.send_keys(Keys.ENTER)
# time.sleep(2)

# loginpass = driver.find_element_by_id('password').send_keys(password)
# time.sleep(2)

# login4real = driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
# time.sleep(10)

# driver.get(myboard)


# Module scope re-uses the fixture
@pytest.fixture(scope='module')
def driver():
    with webdriver.Chrome(r"C:\Users\Feng and Li\Desktop\DevOps\git-playground\DevOps-Course-Starter\drivers\chromedriver.exe") as driver:
        yield driver

def test_trello(driver):
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_id('user').send_keys(username)
    time.sleep(2)

    loginclick = driver.find_elements_by_id('login')
    for loginclick in loginclick: 
        loginclick.send_keys(Keys.ENTER)
    time.sleep(2)

    loginpass = driver.find_element_by_id('password').send_keys(password)
    time.sleep(2)

    login4real = driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    time.sleep(12)

    driver.get(myboard)
    time.sleep(5)
    assert driver.current_url == myboard

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'http://localhost:5000/items/get_all_cards'

# driver.set_page_load_timeout(10)

# driver.get("http://google.com")
# time.sleep(2)
# search = driver.find_elements_by_css_selector('input[name=q]')
# for search in search:
#     search.send_keys('Automation step by step')
#     search.send_keys(Keys.ENTER)

# def test_python_home(driver):
#     driver.get("https://www.python.org")
#     assert driver.title == 'Welcome to Python.org'

# def test_downloads_page(driver):
#     driver.get("https://www.python.org")
#     link = driver.find_element_by_link_text('Downloads')
#     link.click()
#     assert driver.current_url == 'https://www.python.org/downloads/'
