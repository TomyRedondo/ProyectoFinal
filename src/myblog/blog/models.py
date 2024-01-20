from django.db import models

class Anime(models.Model):
    nombre = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.autor}"