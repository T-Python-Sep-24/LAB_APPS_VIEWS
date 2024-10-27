from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string
# Create your views here.


def main_view(request : HttpRequest):
    return render(request, "main/main.html")



def about_view(request : HttpRequest):
    return render(request, "main/about.html")

def password_view(request : HttpRequest):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return render(request, "main/password.html", context={"password" : password})
