from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random 
import string
# Create your views here.

def home(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about(request:HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def generate_password(request:HttpRequest):
    characters = string.digits + string.ascii_letters + string.punctuation
    password  = ''.join(random.choice(characters) for _ in range(10))
    return HttpResponse(password)
