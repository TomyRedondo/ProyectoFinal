from django.urls import path
from blog.views import ver_anime, leer_manga, index

urlpatterns = [
    path('', index),
    path('anime/', ver_anime),
    path('manga/', leer_manga),
]
