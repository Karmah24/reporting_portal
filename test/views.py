from django.shortcuts import render
from django.http import HttpResponse
from .methods import scrapper, news_search, match_keywords, verify_post
from nltk.corpus import stopwords
# Create your views here.
def home(request):
    return render(request, 'index.html') 

def faq(request):
    return render(request, 'faq.html')

def verify(request):
    url = (request.POST['link'])
    time_frame = request.POST['time_frame']
    keywords = request.POST['keywords']
    keywords = keywords.split()
    url = url.replace('www.', 'mbasic.')
    content = scrapper.get_content(url)
    if(match_keywords.check(content,keywords)):
        articles = news_search.get_articles(time_frame, keywords)
        match = verify_post.check(articles, content)
        if(match >= 0.5):
            return render(request, 'result.html', {'link_to_post': url, 'content': content, 
                'articles': articles, 'prob': match})
        else:
            return HttpResponse("The post is fake")
    else:
        return HttpResponse("error: keywords not contained in the post")

