from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string


# Create your views here.
def home_page(request:HttpRequest):
    date="2024-28-10"
    return render(request,"main/home_page.html",context={"date_time":date})



def about(request:HttpRequest):
    return render (request,"main/about.html")


def car_view(request:HttpRequest):
    return render(request,"main/car_view.html")



def generate_password(request):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(characters, k=10))
    return HttpResponse(password)



def available_car(request:HttpRequest):
    rate=[
        {"company":"BMW","model":"2022","status":False},
        {"company":"Toyota","model":"2024","status":True}



    ]
    return render(request,"main/available_car.html",context={"ratte":rate})



