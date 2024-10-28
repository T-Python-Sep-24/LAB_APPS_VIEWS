from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'home.html')  

def about(request):
    return render(request, 'about.html')  

def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return HttpResponse(password)
