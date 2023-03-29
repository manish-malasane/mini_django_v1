from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello, Manthan!')


def welcome(request):
    return render(request, "app1/welcome.html")


def login(request):
    return render(request, "app1/dynamic.html", {"name": "Manthan", "surname": "Malasane"})