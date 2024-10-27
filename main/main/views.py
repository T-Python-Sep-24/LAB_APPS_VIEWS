from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import requests
from requests import Response
import json
length = '10'
api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
#Yet8vVk/C0pZ9GBnLvEWYQ==oX096deoojArdXNj

def view_car(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")
def view_about(request:HttpRequest):
    return HttpResponse("Car rental is when you rent a car. The company providing you the car becomes the car rental service provider, whereas you become the car hirer, as you hire the car for a fee. The Sixt car rental agency at Munich airport, Germany.")
def view_password(request:HttpRequest):
    response = requests.get(api_url, headers={'X-Api-Key': 'Yet8vVk/C0pZ9GBnLvEWYQ==oX096deoojArdXNj'})
    with open('response.json', 'r') as f:
        data=json.load(f)
        f.close()
    return HttpResponse(data["random_password"])
