from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random 
import string
# Create your views here.

def home(request:HttpRequest):
    return render(request, 'app_car/home.html')

def about(request:HttpRequest):
    return render(request, "app_car/about.html")

def generate_password(request:HttpRequest):
    characters = string.digits + string.ascii_letters + string.punctuation
    password  = ''.join(random.choice(characters) for _ in range(10))
    return render(request, 'app_car/password.html', context={'generate_password': password})
