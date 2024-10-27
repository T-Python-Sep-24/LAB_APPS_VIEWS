from django.urls import path

from . import views
app_name = 'car_rental_main_app'

urlpatterns = [
    path("", views.main_view, name='main_view'),
    path("about/", views.about_view, name='about_view'),
    path("password/generate/", views.password_generate_view, name='pass_gen_view'),
]