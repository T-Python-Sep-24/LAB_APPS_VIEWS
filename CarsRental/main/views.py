from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string


# Create your views here.
def page_view(request:HttpRequest):
    return HttpResponse("<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>")


def car_view(request:HttpRequest):
    return HttpResponse("Car rentals allow people to borrow cars for a short time, perfect for travel or temporary use. Customers can choose from different types of cars and pay only for the days they need. This is a flexible and easy way to have a car without owning one.")



def generate_password(request):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(characters, k=10))
    return HttpResponse(password)
