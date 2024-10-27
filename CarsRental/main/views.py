from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random

# Create your views here.

def home_view(request:HttpRequest):

    return render(request, "main/home.html")


def about_view(request:HttpRequest):
    
    return render(request, "main/about.html")


def pass_generator_view(request:HttpRequest):
    characters=list(string.ascii_letters + string.digits + "!@#$%^&*()-=_+\}{[]:;.,")
    random.shuffle(characters)
    password=""
    
    for n in range(10):
        char=random.choice(characters)
        password+=char
        
    return render(request, "main/pass_generator.html", context={"password":password})