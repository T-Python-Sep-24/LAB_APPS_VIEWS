from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.
def page_view(request : HttpRequest):
    return render(request, 'app_1/page_view.html')

def about(request:HttpRequest):
    return render(request, 'app_1/about.html')

def rand_pass(request:HttpRequest):
    length=10
    characters= string.ascii_letters + string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return render(request, 'app_1/rand_pass.html', {'password': password})