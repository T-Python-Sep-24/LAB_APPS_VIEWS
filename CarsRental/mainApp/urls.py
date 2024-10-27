from django.urls import path
from . import views

app_name = "mainApp"

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("about/", views.aboutView, name="aboutView"),
    path("password/generate/", views.passwordGenView, name="passwordGenView")
]