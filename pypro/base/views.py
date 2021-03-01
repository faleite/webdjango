from django.http import HttpResponse  # noqa
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')
