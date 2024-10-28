from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# import the PasswordGenerator class from the generator module
from password_generator.generator import PasswordGenerator
 

# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/home.html")

def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def password_generate_view(request: HttpRequest):
    # create an instance of the PasswordGenerator class
    generator = PasswordGenerator(
        length=10,
        include_lowercase=True,
        include_uppercase=True,
        include_numbers=True,
        include_special_symbols=True,
        dont_begin_with_number_or_symbol=True,
        no_repeated_characters=True,
        no_sequential_characters=True,
        quantity=1
    )

    # call generate method
    password = generator.generate()

    return render(request, "main/password_generate.html", context = {"password_key": password})