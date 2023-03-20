from app import app

url = "http://127.0.0.1:5000"

def test_index_route():
    response = app.test_client().get(url)
    assert response.status_code == 200
    assert "Hello World!" in response.text

