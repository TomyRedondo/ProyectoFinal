from django.db import models

class Anime(models.Model):
    nombreDelAnime = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelAnime"]

    def __str__(self):
        return f"{self.nombreDelAnime}, {self.autor}"
    
    
class Manga(models.Model):
    nombreDelManga = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelManga"]
    
    def __str__(self):
        return f"{self.nombreDelManga}, {self.autor}"

        
class Videojuego(models.Model):
    nombreDelJuego = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelJuego"]
    
 
    
    