from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User 
from start_app.searchItem import SearchItem
from googleapiclient.discovery import build
import pprint

# Create your views here.
def start(request):
    return render(request, 'start.html', {})

def searchResult(request):


    return redirect('deals_by_search_data', request.POST['search_key'])




    
def deals_by_search_data(request, search_key):

  
    
    results = google_search(search_key, my_api_key, my_cse_id, num=10)
    all_results = []
    for result in results:

        pprint.pprint(result)
        title = result['title']
        link = result['formattedUrl']
        dis = result['snippet']
        

        all_results.append(SearchItem(title,link,dis))
        print(title)
        print(link)
        print(dis)
    
    return render(request, 'deals_by_search_data.html', {'data': all_results,})

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey = api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
    
def signin(request):
     return render(request, 'signin.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('start')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



    