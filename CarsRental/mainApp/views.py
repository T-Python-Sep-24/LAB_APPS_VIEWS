from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets, string

#Home page
def homeView(request: HttpRequest):

    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")

#About us page
def aboutView(request: HttpRequest):

    return HttpResponse("Quickly rent a car in Saudi Arabia with Car Rentals!<br>Explore the kingdom comfortably with our services.")

#Password generator page
def passwordGenView(request: HttpRequest):

    #Generate a password that is 10 characters long
    password = secrets.token_urlsafe(10)
    return HttpResponse("Your password: " + password)