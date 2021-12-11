from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    charactes = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactes.extend('ABCDEFGHIJKLMOPQRSTUVWXYZ')
    if request.GET.get('special'):
        charactes.extend('!@#$%^&*()_+')
    if request.GET.get('numbers'):
        charactes.extend('1234567890')
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charactes)

    return render(request, 'generator/password.html', {'password': thepassword})
