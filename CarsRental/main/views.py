from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import faker

def main_view(request:HttpRequest):
    return render(request,"index.html")

def about_view(request:HttpRequest):
    return render(request,"about.html")

def password_generator_view(request:HttpRequest):
    password = faker.Faker()
    random_password = password.password(10,True,True,True,True)
    return render(request,"password.html",context={"random_password":random_password})
