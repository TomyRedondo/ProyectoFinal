from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime, Manga, Videojuego

def index(request):
    return render(request, 'index.html')

def animes(request):
    return render(request, 'animes.html')

# def mangas(request):
#     return render(request, 'mangas.html')

def videojuegos(request):
    return render(request, 'videojuegos.html')

def usuarios_manga(request):
    
    if request.method == "POST":
        nombreDelManga = request.POST.get("nombreDelManga")
        autor = request.POST.get("autor")
        email = request.POST.get("email")
        print(f"""
              Nombre: {nombreDelManga}
              Seudo: {autor}
              Email: {email}
              """)
        
        manga = Manga(nombreDelManga=nombreDelManga, autor=autor, email=email)
        manga.save()
        return render(request, 'index.html')
        
    return render(request, 'usuarios.html')



