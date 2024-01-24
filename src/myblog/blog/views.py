from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Anime, Manga, Videojuego
from blog.forms import Mangaformulario


def usuarios_manga(request):
    
    if request.method == "POST":
        miFormulario = Mangaformulario(request.POST)
        
        # print("formulario")
        # print(formulario)
        print(f" is valid: {miFormulario.is_valid}")
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            # nombreDelManga = informacion.get("nombreDelManga")
            # autor = informacion.get("autor")
            # # email = informacion.get("email")

            datos = Manga(nombreDelManga=informacion["nombreDelManga"], autor=informacion["autor"], email=informacion["email"])
            datos.save()
            
            return render(request, 'index.html')
    
    else:
        miFormulario = Mangaformulario()
        
        

    return render(request, 'usuarios_manga.html')
    
    #     autor = request.POST.get("autor")
    #     email = request.POST.get("email")
    #     print(f"""
    #           Nombre: {nombreDelManga}
    #           Seudo: {autor}
    #           Email: {email}
    #           """)
        
    #     manga = Manga(nombreDelManga=nombreDelManga, autor=autor, email=email)
    #     manga.save()
    #     return render(request, 'index.html')
        



def index(request):
    return render(request, 'index.html')

def animes(request):
    return render(request, 'animes.html')

def mangas(request):
    return render(request, 'mangas.html')

def videojuegos(request):
    return render(request, 'videojuegos.html')

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


# def usuarios_manga(request):
    
#     if request.method == "POST":
#         nombreDelManga = request.POST.get("nombreDelManga")
#         autor = request.POST.get("autor")
#         email = request.POST.get("email")
#         print(f"""
#               Nombre: {nombreDelManga}
#               Seudo: {autor}
#               Email: {email}
#               """)
        
#         manga = Manga(nombreDelManga=nombreDelManga, autor=autor, email=email)
#         manga.save()
#         return render(request, 'index.html')
        
#     return render(request, 'usuarios_manga.html')


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




def busqueda_manga(request):
    
    if request.method == "GET":
        manga = request.GET.get("manga")
        print(f"Buscando manga: {manga}")
    
    return render(request, 'busqueda_manga.html')
        

def buscar_manga(request):

    if request.method == "GET":
        
        nombre_manga = request.GET.get("nombreDelManga")
        
        if nombre_manga is None:
            return HttpResponse("Enviar el manga a buscar")

        # Buscar datos
        mangas = Manga.objects.filter(nombreDelManga__icontains=nombre_manga)
        
        contexto = {
            "nombreDelManga": mangas,
        }
        return render(request, "busqueda.html", {'mangas': mangas})
    return HttpResponse(f"Se busco el manga: {mangas}")