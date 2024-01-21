from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime


# def ver_anime(request):
#     return HttpResponse("Ver Anime")

# def leer_manga(request):
#     return render(request, 'plantilla.html', {"nombre": "Tomy"})



def index(request):
    return render(request, 'index.html')

def animes(request):
    return render(request, 'animes.html')

def mangas(request):
    return render(request, 'mangas.html')

# def novelas(request):
#     return render(request, 'novelas.html')

def videojuegos(request):
    return render(request, 'videojuegos.html')

def about(request):
    return render(request, 'about.html')