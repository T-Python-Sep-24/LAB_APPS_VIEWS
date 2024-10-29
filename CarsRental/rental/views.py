from django.shortcuts import render
import random
import string
from django.http import HttpRequest ,HttpResponse

def home(request):
    return render(request, 'rental/home.html')

def about(request):
    return render(request, 'rental/about.html')

def generate_password(request):
    # Generate a random password
    password_length = 12
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))

    # Render the template with the generated password
    context = {
        'password': password
    }
    return render(request, ' generate_password.html', context)