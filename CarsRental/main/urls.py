from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # index Page
    path("", views.index_view, name="index_view"),
    # About Page
    path("about/",views.about_view, name="about_view"),
    # Password Generator page
    path("password/generate/",views.password_view, name="password_view")
    

]

