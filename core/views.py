from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def luz(request):
    print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
    return render(request, 'core/index.html')


def ventilador(request):
    print('swçjobjabsdfojkbdsojbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbguierrrrrrrrrrrr')
    return render(request, 'core/index.html')