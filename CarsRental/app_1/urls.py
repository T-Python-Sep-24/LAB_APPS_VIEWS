from django.urls import path
from .views import *
urlpatterns = [
    path('', page_view, name="page_view"),
    path('about/',about,name='about' ),
    path('generate/password',rand_pass,name='rand_pass'),

]