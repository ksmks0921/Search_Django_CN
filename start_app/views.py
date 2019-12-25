from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User 
# Create your views here.
def start(request):
    return render(request, 'start.html', {})

def searchResult(request):

    
    return redirect('deals_by_search_data', search_key=request.POST['search_key'])
def deals_by_search_data(request, search_key):
    
    return render(request, 'deals_by_search_data.html', {'search_word': search_key,})

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

# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password =  request.POST['password']
#         post = User.objects.filter(username=username)
#         if post:
#             username = request.POST['username']
#             request.session['username'] = username
#             return redirect("profile")
#         else:
#             return render(request, 'app_foldername/login.html', {})
#     return render(request, 'signin.html', {})

# def profile(request):
#     if request.session.has_key('username'):
#         posts = request.session['username']
#         query = User.objects.filter(username=posts) 
#         return render(request, 'signup.html', {"query":query})
#     else:
#         return render(request, 'login.html', {})

# def logout(request):
#     try:
#         del request.session['username']
#     except:
#      pass
#     return render(request, 'app_foldername/login.html', {})

    