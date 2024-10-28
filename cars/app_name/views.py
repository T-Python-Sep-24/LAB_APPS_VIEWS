from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import string

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")

def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")

def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    for index in range(10):
        password += random.choice(characters)  
    
    return HttpResponse(password)