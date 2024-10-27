from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import faker

def main_view(request:HttpRequest):
    return HttpResponse("<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>")

def about_view(request:HttpRequest):
    return HttpResponse("<p1>A simple paragraph about Car Rentals.</p1>")

def password_generator_view(request:HttpRequest):
    password = faker.Faker()
    random_password = password.password(10,True,True,True,True)
    return HttpResponse(random_password)
