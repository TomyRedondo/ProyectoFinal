from django.urls import path
from blog.views import index, animes, mangas, videojuegos, usuarios_anime, usuarios_manga, usuarios_videojuego, busqueda_manga, buscar_manga

urlpatterns = [
    path('', index, name='index'),
    path('anime/', animes, name='animes'),
    path('manga/', mangas, name='mangas'),
    path('videojuego/', videojuegos, name='videojuegos'),
    path('usuarioAnime/', usuarios_anime, name='usuarios_anime'),
    path('usuarioManga/', usuarios_manga, name='usuarios_manga'),
    path('usuarioVideojuego/', usuarios_videojuego, name='usuarios_videojuego'),
    path('busquedaManga', busqueda_manga, name='busqueda_manga'),
    path('buscar', buscar_manga, name='buscar_manga')
]
