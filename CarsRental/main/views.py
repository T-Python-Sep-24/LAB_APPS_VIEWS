from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random 
import string
# Create your views here.


def page_view(request : HttpRequest):
 
  return render(request,"main\page.html")



def about_view(request : HttpRequest):
 
  return render(request,"main/about.html")





def generate_pass(request):
 length = 10
 characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password
 password = ''.join(random.choice(characters) for _ in range(length))
 return render(request,"main\password.html", context={'password':password})