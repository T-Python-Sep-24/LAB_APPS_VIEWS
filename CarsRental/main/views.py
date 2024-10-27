from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
import random
import string 
# Create your views here.

def home_view(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")

def about_view(request:HttpRequest):

    return HttpResponse("Car rental agencies primarily serve people who require a temporary vehicle, for example, those who do not own their own car, travelers who are out of town .")

def password_view(request:HttpRequest):
   


    lenght = 10

    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password = "".join(random.choice(all_characters) for _ in range(lenght))
    return HttpResponse(password)