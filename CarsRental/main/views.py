from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random,string
# Create your views here.

def home(request:HttpRequest):

    return render (request,"main/index.html")
def about(request:HttpRequest):

    return render(request,"main/about.html")

def password_gen(request:HttpRequest):
    chars=string.ascii_letters+string.digits+string.punctuation
    password=[random.choice(chars) for i in range(10)]
    generated_password=''.join(password)
    return render (request,"main/password_generator.html",context={"password":generated_password})
