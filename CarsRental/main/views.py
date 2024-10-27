from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random

# Create your views here.

def index_view(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals.")

def password_view(request: HttpRequest):
    length = 10  
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))
    print(password)  

    return HttpResponse(password)

