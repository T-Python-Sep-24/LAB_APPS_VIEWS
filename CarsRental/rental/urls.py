from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('generate_password/', views.generate_password, name='generate_password'),
]