from django.db import models

class Anime(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.autor}"
    
class Manga(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}, {self.autor}"
    
    
# class Novela(models.Model):
#     nombre = models.CharField(max_length=30)
#     año = models.IntegerField()
    
#     def __str__(self):
#         return f"{self.nombre} -- {self.año}"
    
        
class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
 
    
    