from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string
# Create your views here.


def main_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)


def about_view(request : HttpRequest):
    content = "Car rentals offer customers the flexibility to rent vehicles for short or long-term use, making travel or commuting convenient without the need for ownership. They provide a range of vehicles, from budget options to premium cars, catering to various needs, such as business trips, vacations, or temporary replacements. Car rental services are accessible through local branches, websites, or apps, allowing for easy booking and quick pickups."
    return HttpResponse(content)

def password_view(request : HttpRequest):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return HttpResponse(f"Generated Password: {password}")
