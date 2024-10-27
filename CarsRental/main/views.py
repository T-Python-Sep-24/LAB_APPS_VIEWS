from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random

# Create your views here.

def home_view(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):
    
    return HttpResponse("Car rentals offer a convenient and flexible way for individuals and businesses to access vehicles without the long-term commitment of ownership. Whether for a weekend getaway, a business trip, or everyday errands, renting a car allows customers to choose from a diverse fleet that suits their specific needs.")


def pass_generator_view(request:HttpRequest):
    characters=list(string.ascii_letters + string.digits + "!@#$%^&*()-=_+\}{[]:;.,")
    random.shuffle(characters)
    password=""
    
    for n in range(10):
        char=random.choice(characters)
        password+=char
        
    return HttpResponse(password)