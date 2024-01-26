from django.urls import path
from django.contrib.auth.views import LogoutView

from blog.views import (
    index, 
    mangas, 
    videojuegos, 
    usuarios_manga, 
    usuarios_videojuego, 
    busqueda_manga, 
    buscar_manga, 
    leer_mangas, 
    eliminar_manga,
    editar_manga,
    login_request,
    registrar,
    VideojuegoList,
    VideojuegoDetalle,
    VideojuegoCreacion,
    VideojuegoUpdate,
    VideojuegoDelete,
)

urlpatterns = [
    path('', index, name='index'),
    path('mangas/', mangas, name='mangas'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('usuarioManga/', usuarios_manga, name='usuarios_manga'),
    path('usuarioVideojuego/', usuarios_videojuego, name='usuarios_videojuego'),
    path('busquedaManga/', busqueda_manga, name='busqueda_manga'),
    path('buscar/', buscar_manga, name='buscar_manga'),
    path('leerMangas/', leer_mangas, name='leer_mangas'),
    path('eliminarManga/<str:nombreDelManga>/', eliminar_manga, name='eliminar_manga'),
    path('editarManga/<str:nombreDelManga>/', editar_manga, name='editar_manga'),
    path('videojuego/list', VideojuegoList.as_view(), name='List'),
    path('detalle-videojuego/<pk>', VideojuegoDetalle.as_view(), name='Detail'),
    path('editar-videojuego/<pk>', VideojuegoUpdate.as_view(), name='Edit'),
    path('borrar-videojuego/<pk>', VideojuegoDelete.as_view(), name='Delete'),
    path('crear-videojuego/<pk>', VideojuegoCreacion.as_view(), name='Create'),
    path('login', login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('registrar', registrar, name='Registrar'),
]
