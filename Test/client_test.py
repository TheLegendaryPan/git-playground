import app
import pytest
from trelloapp import Trello
from dotenv import find_dotenv, load_dotenv
import json

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

def substitute_trello_api_mock(self):
    return  str("""[{
                "id": "12345",
                "name": "Test to do item",
                "idList": "67890",
                "dateLastActivity": "2020-08-01T12:52:06.278Z"
            }]""")

# whenever you include a fixture in text function, code inside
# the fixture runs before the test itself is run. 
# in below monkey patch example, I'm replacing get_all_cards_from_board from Trello with substitute_trello_api_mock
@pytest.fixture
def mock_get_requests(monkeypatch):
    monkeypatch.setattr(Trello, "get_all_cards_from_board", substitute_trello_api_mock)


#works. just client.get('/') triggers redirect and result in 302 error. 
def test_index_page(client):
    response = client.get('/items/get_all_cards')
    assert response.status_code == 200 

#works
def test_index_page_with_mock(mock_get_requests, client):
    response = client.get('/items/get_all_cards')
    assert response.status_code == 200 

#magically worked... 
def test_index_page_with_mock2(mock_get_requests, client):
    response = client.get('/items/get_all_cards')
    data = Trello.get_all_cards_from_board(response)
    data2 = json.loads(data)
    assert "Test to do item" in data
    assert "12345" in data
    assert "67890" in data
    assert "2020-08-01T12:52:06.278Z" in data
    assert data2[0] == {'id': '12345', 'name': 'Test to do item', 'idList': '67890', 'dateLastActivity': '2020-08-01T12:52:06.278Z'}
    assert data2[0]['name'] == "Test to do item"