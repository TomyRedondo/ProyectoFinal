from django.db import models
    
class Manga(models.Model):
    nombreDelManga = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelManga"]
    
    def __str__(self):
        return f"{self.nombreDelManga}"

        
class Videojuego(models.Model):
    nombreDelJuego = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelJuego"]
        
    def __str__(self):
        return f"{self.nombreDelJuego}"
