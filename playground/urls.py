from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('hello/', views.say_hello2),
    path('__debug__/', include('debug_toolbar.urls')),
    # routes always ends with forward slash /
]