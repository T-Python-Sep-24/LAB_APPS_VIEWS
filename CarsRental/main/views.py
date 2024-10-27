from django.shortcuts import render
import random 
import string

# Create your views here.
from django.http import HttpRequest , HttpResponse

def home_view(request:HttpRequest):
    phrase  = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"

    return HttpResponse(phrase)

def about_view (request:HttpRequest):
    
    paragraph = "Car rentals are an easy way to get a temporary vehicle.\nYou can choose the type of car you need and rent it for a short or long period. Booking is simple, and you can pick up and drop off the car at convenient locations.\n It’s a cost-effective option without the hassle of maintenance or insurance. "

    return HttpResponse(paragraph)

def password_view (requste : HttpRequest): 
    passwords = []
    for i in range(10):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) )
        passwords.append(password)
    return HttpResponse(''.join(passwords))