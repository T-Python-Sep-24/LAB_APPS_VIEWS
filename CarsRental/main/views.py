from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import string


# Create your views here.

def main_view(request:HttpRequest):

    return HttpResponse("<h1>Hello World,</h1><h3 style='color:blue;'>This is my new HOME for Car Rentals Website!</h3> We're excited to welcome you here.")



def about_view(request:HttpRequest):

    return HttpResponse("""
                        <p style='background-color:powderblue;' 'color:white;'>
                        Car rentals provide a convenient solution for travelers, offering temporary access to vehicles without the long-term commitment of ownership.
                        <br>Whether for business trips, vacations, or simply exploring a new city, renting a car allows individuals the freedom to move at their own pace.</br>
                        With various car types available, customers can choose from economy, luxury, or family-sized vehicles based on their needs and budget.
                        </p>
                        """)



def password_view(request:HttpRequest):

    lenght = 10

    all_characters = string.ascii_letters + string.digits + string.punctuation

    #length = int(input("Enter the length of the password: "))

    password = ''.join(random.choices(all_characters, k=lenght))

    return HttpResponse(f"Your password is: {password}")
