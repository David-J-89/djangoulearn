from django.shortcuts import render
from django.http import HttpResponse
import feedparser

# Create your views here.

def index(request):
    url = 'https://www.djangoproject.com/rss/weblog/'

    feed = feedparser.parse(url)

    return render(request, 'rss/reader.html', {
        'feed': feed
    })
