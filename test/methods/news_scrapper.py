import requests
from bs4 import BeautifulSoup

def get_content(url):
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    content_ = soup.findAll("p")
    content = ""
    for tag in content_:
        content += tag.text
    return content