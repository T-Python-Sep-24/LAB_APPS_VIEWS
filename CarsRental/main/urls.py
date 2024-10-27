from django.urls import path
from . import views

main="main"

urlpatterns = [
 path("", views.page_view, name="page_view"),
 path("about/",views.car_view,name="car_view"),
 path("password/generate/",views.generate_password,name="generate_password")
 ]