from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime


def ver_anime(request):

    return HttpResponse("Ver Anime")


def leer_manga(request):
    return render(request, 'plantilla.html', {"nombre": "Milu"})

def index(request):
    return render(request, 'index.html')