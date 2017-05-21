from django.shortcuts import render
from .rf433 import send, teste_usb
from .tratutor import Traduzir


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


def tradutor(request):
    if request.method == "POST":
        frase = request.POST['texto']
        traduzir = Traduzir.traduzir(frase)
        return render(request, 'core/tradutor.html', {'tradução': traduzir})

    else:
        return render(request, 'core/tradutor.html')
