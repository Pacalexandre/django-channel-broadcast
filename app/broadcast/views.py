from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.icndb.com/jokes/ramdom'
    response = requests.get(url).json()
    joke = response.get('value')[0]
    return render(request, 'index.html', context=joke)
