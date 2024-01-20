from django.urls import path
from blog.views import leer_anime, leer_manga

urlpatterns = [
    path('anime/', leer_anime),
    path('manga/', leer_manga)
]