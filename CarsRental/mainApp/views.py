from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets, string

#Home page
def homeView(request: HttpRequest):
    
    return render(request, "mainApp/home.html")

#About us page
def aboutView(request: HttpRequest):

    return render(request, "mainApp/about.html")

#Password generator page
def passwordGenView(request: HttpRequest):

    #Generate a password that is 10 characters long
    password = secrets.token_urlsafe(10)
    return render(request, "mainApp/passwordGen.html", context={"password" : password})