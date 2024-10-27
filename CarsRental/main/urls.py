from django.urls import path
from . import views

main="main"

urlpatterns = [
 path("", views.home_page, name="page_view"),
 path("car/view",views.car_view,name="car_view"),
 path("password/generate/",views.generate_password,name="generate_password"),
 path("available/car",views.available_car,name="available_car"),
 path("about/us",views.about,name="about_us")
 ]