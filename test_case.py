from app import app

url = "/"

def test_root_url():
    response = app.test_client.get(url)
    assert response.status_code == 200
    assert "Hello World!" in response.text

