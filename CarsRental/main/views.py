from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random,string
# Create your views here.

def home(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about(request:HttpRequest):

    return HttpResponse("A simple paragraph about Car Rentals.")

def password_gen(request:HttpRequest):
    chars=string.ascii_letters+string.digits+string.punctuation
    password=[random.choice(chars) for i in range(10)]
    return HttpResponse(''.join(password))
