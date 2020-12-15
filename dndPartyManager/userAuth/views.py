from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
    else:
        # Return an 'invalid login' error message.
        