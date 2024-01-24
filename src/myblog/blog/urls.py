from django.urls import path
from blog.views import index, mangas, videojuegos, usuarios_manga, usuarios_videojuego, busqueda_manga, buscar_manga, leer_mangas

urlpatterns = [
    path('', index, name='index'),
    path('mangas/', mangas, name='mangas'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('usuarioManga/', usuarios_manga, name='usuarios_manga'),
    path('usuarioVideojuego/', usuarios_videojuego, name='usuarios_videojuego'),
    path('busquedaManga/', busqueda_manga, name='busqueda_manga'),
    path('buscar/', buscar_manga, name='buscar_manga'),
    path('leerMangas/', leer_mangas, name='leer_mangas'),
    # path('leerMangas/<str:nombre_del_manga>/', leer_mangas, name='leer_mangas_con_parametro'),

]
