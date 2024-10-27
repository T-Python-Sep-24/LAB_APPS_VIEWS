from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import string


# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/home.html")


def about_view(request:HttpRequest):

    return render(request, "main/about.html")



def password_view(request:HttpRequest):

    lenght = 10

    all_characters = string.ascii_letters + string.digits + string.punctuation

    #length = int(input("Enter the length of the password: "))

    password = ''.join(random.choices(all_characters, k=lenght))

    return render(request, "main/password_generate.html", context={"password": password})
