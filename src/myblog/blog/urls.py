from django.urls import path
from blog.views import index, animes, mangas, videojuegos, about

urlpatterns = [
    path('', index, name='index'),
    path('anime/', animes, name='animes'),
    path('manga/', mangas, name='mangas'),
    # path('novela/', novelas, name='novelas'),
    path('videojuego/', videojuegos, name='videojuegos'),
    path('about/', about, name='about'),
]
