from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random 
import string
# Create your views here.


def page_view(request : HttpRequest):
 
  return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")



def about_view(request : HttpRequest):
 
  return HttpResponse("A car rental reservation system is a software solution that helps manage the car rental business, streamlining and automating the majority of operational workflows.")



 

def generate_pass(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(password)  