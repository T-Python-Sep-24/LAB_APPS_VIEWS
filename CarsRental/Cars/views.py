from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.
def home(request):
    return render(request , 'Cars/home.html')
def about(request):
    return render(request , 'Cars/about.html')
def password(request):
    char=string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char)for i in range(10))
    return render(request,'Cars/password.html',{'password':password})
