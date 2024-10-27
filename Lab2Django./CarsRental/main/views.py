import random
import string
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


# Create your views here.
def main_view(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

#A simple paragraph about Car Rentals.

def about_view(request:HttpRequest):
    paragraph="Welcome to our car rental service, where your journey begins with convenience and excitement! Whether you're exploring a new city, planning a weekend getaway, or in need of a reliable vehicle for business travel, we’ve got you covered. Our diverse fleet features everything from compact cars to spacious SUVs, ensuring you find the perfect ride for your adventure. With competitive rates, flexible rental options, and a commitment to exceptional customer service, we make it easy to hit the road and create unforgettable memories. Join us and discover the freedom of travel at your fingertips!"
    return HttpResponse(paragraph)

#When requesting http://127.0.0.1:8000/password/generate/, it should return a randomly generated password of length 10 characters (letters, upper, lower, symbols) :

def generate_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(password)