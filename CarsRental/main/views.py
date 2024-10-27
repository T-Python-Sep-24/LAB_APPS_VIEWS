from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
import random
import string 
# Create your views here.

def home_view(request:HttpRequest):

    return render(request, "main/home.html")

def about_view(request:HttpRequest):

    return render(request,"main/about.html")

def password_view(request:HttpRequest):
   
    lenght = 10

    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password = "".join(random.choice(all_characters) for _ in range(lenght))
    return render(request, "main/password.html",context={"password" : password})