from django.db import models

class Anime(models.Model):
    nombre = models.CharField(max_length=30)
    seudonimo = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.seudonimo}"
    
    
class Manga(models.Model):
    nombre = models.CharField(max_length=30)
    seudonimo = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombre"]
    
    def __str__(self):
        return f"{self.nombre}, {self.seudonimo}"

        
class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
    class Meta:
        ordering=["nombre"]
    
 
    
    