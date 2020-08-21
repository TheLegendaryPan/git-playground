from hello import app
import pytest

#testing my hello flask app
def test_app():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'