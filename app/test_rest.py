import requests

def test_text_endpoint():
    url = "http://localhost:8080/text"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == "Hello from Flask!"
