from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    items = {
        "fruit": "apple",
        "price": 200,
        "origin": "finland"
    }
    return render(request, "home.html", items)


def info(request):
    return render(request, "info.html", {"number": 13})
