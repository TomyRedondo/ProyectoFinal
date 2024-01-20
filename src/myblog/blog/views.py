from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime


def leer_anime(request):

    return HttpResponse("Anime")


def leer_manga(request):
    
    return render(request, 'plantilla.html', {"nombre": "Milu"})