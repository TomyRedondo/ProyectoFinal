from django.urls import path
from blog.views import index, animes, mangas, videojuegos, usuarios

urlpatterns = [
    path('', index, name='index'),
    path('anime/', animes, name='animes'),
    path('manga/', mangas, name='mangas'),
    # path('novela/', novelas, name='novelas'),
    path('videojuego/', videojuegos, name='videojuegos'),
    path('usuario/', usuarios, name='usuarios')
]
