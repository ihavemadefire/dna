from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    pirates = Pirate.objects.all()
    context = {'pirates': pirates}
    return render(request, 'index.html', context)

def detail(request, name):
    pirates = Pirate.objects.all()
    pirate = Pirate.objects.get(name=name)
    context = {'pirate': pirate, 'pirates': pirates}
    return render(request, 'detail.html', context)

def all(request):
    pirates = Pirate.objects.all()
    context = {'pirates': pirates}
    return render(request, 'all.html', context)
