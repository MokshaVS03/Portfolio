from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    #send a GET request to the root URL
    response = client.get("/")

    #check if the response status is 200 OK
    assert response.status_code == 200

    #Check if the HTML content returned contains a specific string
    assert "<title>Moksha VS</title>" in response.text