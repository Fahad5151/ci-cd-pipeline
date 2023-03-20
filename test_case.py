import requests;

url = "http://127.0.0.1:5000/"

def test_root_url():
    response = requests.get(url)
    assert response.status_code == 200
    assert "Hello World!" in response.text

