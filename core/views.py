from django.shortcuts import render
from .main import ligar_luz, ligar_ventilador


def home(request):
    return render(request, 'core/index.html')


def luz(request):
    ligar_luz()
    return render(request, 'core/index.html')


def ventilador(request):
    ligar_ventilador()
    return render(request, 'core/index.html')
