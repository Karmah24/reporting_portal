import requests
from bs4 import BeautifulSoup
from .keys import username, password

def get_content(url):
    payload = {'email': username, 'pass': password}
    POST_LOGIN_URL = "https://www.facebook.com/login"
    with requests.Session() as session:
        post = session.post(POST_LOGIN_URL, data=payload)
        result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    post_text = soup.find('div', class_='bx').text
    return post_text