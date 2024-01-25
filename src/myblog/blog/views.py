from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Manga, Videojuego
from blog.forms import Mangaformulario
        

def index(request):
    return render(request, 'index.html')


# ------------- MANGAS -------------------

def mangas(request):
    
    if request.method == "POST":
        #leer los datos que vienen en el post
        datos_manga = Mangaformulario(request.POST)
        print(datos_manga)

        if datos_manga.is_valid():
            # datos_base = datos_manga.cleaned_data
            datos = datos_manga.cleaned_data
            nombre = datos.get("nombreDelManga")
            autor = datos.get("autor")
            email = datos.get("email")
            
            datos = Manga(nombreDelManga=datos["nombreDelManga"], autor=datos["autor"], email=datos["email"])
            datos.save()
            
            return render(request, 'index.html')
            # datos = Manga(nombreDelManga=datos_base["nombreDelManga"], autor=datos_base["autor"], email=datos_base["email"])

        else:
            mangaFormulario = Mangaformulario()
        
    else:
        mangaFormulario = Mangaformulario()
    
    return render(request, 'crear_manga.html', {"mangaFormulario": mangaFormulario})


def usuarios_manga(request):
    
    if request.method == "POST":
        miFormulario = Mangaformulario(request.POST)
        
        print(f" is valid: {miFormulario.is_valid}")
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            datos = Manga(nombreDelManga=informacion["nombreDelManga"], autor=informacion["autor"], email=informacion["email"])
            datos.save()
            
            return render(request, 'index.html')
    
    else:
        miFormulario = Mangaformulario()
        
    return render(request, 'usuarios_manga.html')


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


def leer_mangas(request):
    
    mangas = Manga.objects.all()
    
    contexto = {"mangas": mangas}

    return render(request, 'leer_mangas.html', contexto)


def eliminar_manga(request, nombreDelManga):
    
    manga = Manga.objects.filter(nombreDelManga=nombreDelManga)
    
    manga.delete()
    
    mangas = Manga.objects.all()
    
    contexto = {"mangas": mangas}

    return render(request, 'leer_mangas.html', contexto)
    


# ------------- VIDEOJUEGOS -------------------

def videojuegos(request):
    return render(request, 'videojueos.html')


def usuarios_videojuego(request):
    
    if request.method == "POST":
        nombreDelJuego = request.POST.get("nombreDelJuego")
        autor = request.POST.get("autor")
        email = request.POST.get("email")
        fecha = request.POST.get("fecha")
        print(f"""
              Nombre: {nombreDelJuego}
              Autor: {autor}
              Email: {email}
              Fecha: {fecha}
              """)
        
        juego = Videojuego(nombreDelJuego=nombreDelJuego, autor=autor, email=email, fecha=fecha)
        juego.save()
        return render(request, 'index.html')
        
    return render(request, 'usuarios_videojuego.html')