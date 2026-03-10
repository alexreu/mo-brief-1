from fastapi.testclient import TestClient
from api import app

def test_analyse_sentiment():
    client = TestClient(app)
    response = client.post("/analyse_sentiment/", json={"text": "I'm so happy to do what I do for living"})
    assert response.status_code == 200
    data = response.json()
    assert "pos" in data
    assert "neg" in data
    assert "neu" in data
    assert "compound" in data
