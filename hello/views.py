from django.shortcuts import render
from django.http import HttpResponse


def wys(request):
    return render(request, "index.html")
