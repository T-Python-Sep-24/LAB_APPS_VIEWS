import random
import faker
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def main_view(requist:HttpRequest):

    return HttpResponse("<h1 style='text-align: center'> Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here</h1>")
def about_view(requist:HttpRequest):
    return HttpResponse("<h2>About TuwWeels Car Rental</h2> <h3 style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)'>Welcome to TuwWeels Car Rental, where we’re committed to providing a seamless and enjoyable car rental experience. With a diverse fleet of well-maintained vehicles, from compact cars to luxury sedans and spacious SUVs, we have the perfect ride for every journey. Our mission is to make transportation easy, affordable, and convenient, whether you’re planning a business trip, a family vacation, or an adventure on the open road. We pride ourselves on exceptional customer service, transparent pricing, and flexible rental options to fit your schedule and needs. Let us be your trusted travel partner on the road ahead!</h3>")

def password_generate_view(requist: HttpRequest):
    o = faker.Faker()
    newPassword = o.password(length=10)

    return HttpResponse(f"<h1 style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)'> New Password: <code style = 'background-color: red'>{newPassword} </code></h1>")


