from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random

# Create your views here.

def index_view(request:HttpRequest):
    return render(request, 'main/index.html')

def about_view(request:HttpRequest):
    return render(request, 'main/about.html')

def password_view(request: HttpRequest):
    length = 10  # Fixed length of 10
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))
    return render(request, 'main/password_generator.html', {'password': password})

