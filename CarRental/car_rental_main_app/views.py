import random
import faker
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(requist:HttpRequest):

    return render(requist, 'car_rental_main_app/main_view.html', )

def about_view(requist:HttpRequest):

    return render(requist, 'car_rental_main_app/about_view.html')

def password_generate_view(requist: HttpRequest):

    o = faker.Faker()
    newPassword = o.password(length=10)

    return render(requist, 'car_rental_main_app/pass_gen_view.html', context={"pass": newPassword})


