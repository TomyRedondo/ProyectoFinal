from django.db import models
    
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
    autor = models.CharField(max_length=30, default='Desconocido')
    email = models.EmailField()
    
    class Meta:
        ordering=["nombreDelJuego"]
        
    def __str__(self):
        return f"{self.nombreDelJuego}, {self.autor}"
    
 
    
    