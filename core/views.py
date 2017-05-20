from django.shortcuts import render
from .rf433 import send, teste_usb


def home(request):
    con = teste_usb()
    return render(request, 'core/index.html', {"send": con})


def luz(request):
    con = teste_usb()
    send('l')
    return render(request, 'core/index.html', {"send": con})


def ventilador(request):
    con = teste_usb()
    send('v')
    return render(request, 'core/index.html', {"send": con})
