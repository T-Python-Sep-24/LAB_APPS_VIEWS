from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import string

def welcome(request: HttpRequest):
    return render(request, "main/welcome.html")

def aboutUs(request: HttpRequest):
    return render(request, "main/about.html")

def passGenerator(request: HttpRequest):
    allChars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    randomChoice = ""
    for i in range(6):
        randomChoice += random.choice(allChars)
        
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + randomChoice + random.choice(string.punctuation)
    
    return render(request, "main/password.html", context={"password": password})
