from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '9b3c16a278767e93f7cf3cdc61b1481a'

def home(request):
    if request.method == 'POST':
        # 입력된 내용을 바탕으로
        # https://api.themoviedb.org/3/search/movie?api_key=9b3c16a278767e93f7cf3cdc61b1481a&language=en-US&page=1&include_adult=false
        # 위 형태의 url로 get 요청 보내기
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key=' + my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):

    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    # https://api.themoviedb.org/3/movie/{movie_id}?api_key=9b3c16a278767e93f7cf3cdc61b1481a&language=en-US
    # 이 url에 get 요청 보내기
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {"resdata":resdata})
