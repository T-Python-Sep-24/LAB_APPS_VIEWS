import random
import string
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


# Create your views here.
def main_view(request:HttpRequest):
    return render(request,"main/main.html")

#A simple paragraph about Car Rentals.

def about_view(request:HttpRequest):
    return render(request , "main/about.html")

#When requesting http://127.0.0.1:8000/password/generate/, it should return a randomly generated password of length 10 characters (letters, upper, lower, symbols) :
def generate_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Render the template with the generated password
    return render(request, 'main/generatePassword.html', context= {'password': password})