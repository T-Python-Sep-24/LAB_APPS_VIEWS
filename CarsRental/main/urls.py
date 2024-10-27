from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("about/", views.aboutUs, name="aboutUs"),
    path("password/generate/", views.passGenerator, name="passGenerator"),
]