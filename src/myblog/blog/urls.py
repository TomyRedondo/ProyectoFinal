from django.urls import path
from blog.views import index, animes, mangas, videojuegos, usuarios_manga, usuarios_anime, usuarios_manga, usuarios_videojuego

urlpatterns = [
    path('', index, name='index'),
    path('anime/', animes, name='animes'),
    path('manga/', mangas, name='mangas'),
    path('videojuego/', videojuegos, name='videojuegos'),
    path('usuario/', usuarios_manga, name='usuarios_manga'),
    path('usuarioAnime/', usuarios_anime, name='usuarios_anime'),
    path('usuarioManga/', usuarios_manga, name='usuarios_manga'),
    path('usuarioVideojuego/', usuarios_videojuego, name='usuarios_videojuego'),
]
