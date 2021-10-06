# src/tests/conftest.py

import pytest
from app import main

# see: http://flask.pocoo.org/docs/1.0/testing/
@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client

# http://flask.pocoo.org/docs/1.0/testing/#testing-json-apis
def test_hello_greets_greetee(client):
   request_payload = {"greetee": "world"}
   response = client.post("/hello", json=request_payload)
   result = response.get_json()

   assert response.status_code == 200
   assert result is not None
   assert "message" in result
   assert result['message'] == "hello world"
   
@pytest.fixture()
def create_valid_greeting_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_greeting_request(greetee="fixture"):
        return {
            "greetee": greetee
        }
    return _create_valid_greeting_request