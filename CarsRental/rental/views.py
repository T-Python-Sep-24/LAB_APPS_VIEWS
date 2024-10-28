from django.shortcuts import render

import random
import string
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")

def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")

def generate_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return HttpResponse(password)