from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from ..methods import news_scrapper

def check(articles, content):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    content = content.lower()
    corpus = word_tokenize(content)
    doc = [token for token in corpus if ((token.isalpha() or token.isnumeric()) and token not in stop_words)]
    for i in range(len(doc)):
        doc[i] = ps.stem(doc[i])
    total_count = len(doc)
    score = 0
    for key, value in articles.items():
        article_content = news_scrapper.get_content(key)
        score_ = 0
        article_content = article_content.lower()
        corpus = word_tokenize(article_content)
        news = [token for token in corpus if((token.isalpha() or token.isnumeric()) and token not in stop_words)]
        for i in range(len(news)):
            news[i] = ps.stem(news[i])
        for word in doc:
            if(word in news):
                score_ += 1
        score += score_/total_count
    score /= 5

    return score