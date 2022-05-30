from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
    # routes always ends with forward slash /
]