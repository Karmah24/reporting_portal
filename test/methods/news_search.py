import requests
from bs4 import BeautifulSoup

def get_articles(time_frame, keywords):
    query = "q="
    for keyword in keywords:
        query += keyword+"%20"
    if(time_frame == "hour"):
        query += "when%3A1h"
    elif(time_frame == "day"):
        query += "when%3A1d"
    elif(time_frame == "week"):
        query += "when%3A7d"
    elif(time_frame == "year"):
        query += "when%3A1y"
    
    url = "https://news.google.com/search?"+query+"&hl=en-IN&gl=IN&ceid=IN%3Aen"
    
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    articles = []
    for a in soup.select('h3:nth-of-type(-n+5)'):   
        articles.append(a)
    article_headlines = []
    article_links = []
    for i in range(5):
        article_links.append(articles[i].find("a").attrs['href'])
        article_headlines.append(articles[i].text)
    for i in range(5):
        article_links[i] = article_links[i].replace("./", "https://news.google.com/")
    articles_dict = {}
    for i in range(5):
        articles_dict[article_links[i]] = article_headlines[i]
    return articles_dict
