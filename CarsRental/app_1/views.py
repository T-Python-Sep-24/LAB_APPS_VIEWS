from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)
def about(request:HttpRequest):
    return HttpResponse("Car rental is when you rent a car.")
def rand_pass(request:HttpRequest):
    length=10
    characters= string.ascii_letters + string.digits+string.punctuation
    generate_pass=''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(generate_pass)