from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime, Manga, Videojuego

def index(request):
    return render(request, 'index.html')

def animes(request):
    return render(request, 'animes.html')

def mangas(request):
    return render(request, 'mangas.html')

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

def usuarios_anime(request):
    
    if request.method == "POST":
        nombreDelAnime = request.POST.get("nombreDelAnime")
        autor = request.POST.get("autor")
        email = request.POST.get("email")
        print(f"""
              Nombre: {nombreDelAnime}
              Seudo: {autor}
              Email: {email}
              """)
        
        manga = Manga(nombreDelAnime=nombreDelAnime, autor=autor, email=email)
        manga.save()
        return render(request, 'index.html')
        
    return render(request, 'usuarios_anime.html')


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
        
    return render(request, 'usuarios_manga.html')


def usuarios_videojuego(request):
    
    if request.method == "POST":
        nombreDelJuego = request.POST.get("nombreDelJuego")
        fechaDeEntrega = request.POST.get("fechaDeEntrega")
        email = request.POST.get("email")
        print(f"""
              Nombre: {nombreDelJuego}
              Seudo: {fechaDeEntrega}
              Email: {email}
              """)
        
        manga = Manga(nombreDelJuego=nombreDelJuego, fechaDeEntrega=fechaDeEntrega, email=email)
        manga.save()
        return render(request, 'index.html')
        
    return render(request, 'usuarios_videojuego.html')





