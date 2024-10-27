from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.
def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")
def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")
def password(request):
    char=string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char)for i in range(10))
    return HttpResponse(password)
