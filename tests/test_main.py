from bs4 import BeautifulSoup
import requests


def test_main():
    req = requests.get("http://127.0.0.1:5000/")

    soup = BeautifulSoup(
        req.text,
        "html.parser",
    )

    assert "headline" in req.text
