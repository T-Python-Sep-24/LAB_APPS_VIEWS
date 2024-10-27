from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import string

def welcome(request: HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def aboutUs(request: HttpRequest):
    return HttpResponse("A car rental website is a place where you can find and book cars to use for a short time. You go to the website, choose the car you want, and select the days you need it. It is easy to see pictures of the cars and read about their prices. When you finish, you can pay online and pick up the car at a nearby location. This helps you travel easily without owning a car.")

def passGenerator(request: HttpRequest):
    allChars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    randomChoice = ""
    for i in range(6):
        randomChoice += random.choice(allChars)
        
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + randomChoice + random.choice(string.punctuation)
    
    return HttpResponse(password)
