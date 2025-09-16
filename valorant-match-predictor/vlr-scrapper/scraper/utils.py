import requests
from bs4 import BeautifulSoup

def fetch_html(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html: str):
    return BeautifulSoup(html, "html.parser")
