from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello2(request):
    return render(request, 'index.html',{'name': 'abhi'} )
