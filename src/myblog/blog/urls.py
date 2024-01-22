from django.urls import path
from blog.views import index, animes, videojuegos, usuarios_manga

urlpatterns = [
    path('', index, name='index'),
    path('anime/', animes, name='animes'),
    # path('manga/', mangas, name='mangas'),
    path('videojuego/', videojuegos, name='videojuegos'),
    path('usuario/', usuarios_manga, name='usuarios_manga'),
]
