from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Manga, Videojuego
from blog.forms import Mangaformulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView     

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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

@login_required
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

def editar_manga(request, nombreDelManga):
    manga = Manga.objects.get(nombreDelManga=nombreDelManga)

    if request.method == "POST":
        formulario = Mangaformulario(request.POST)
        if formulario.is_valid():
            manga.nombreDelManga = formulario.cleaned_data['nombreDelManga']
            manga.autor = formulario.cleaned_data['autor']
            manga.email = formulario.cleaned_data['email']
            manga.save()
            return redirect('leer_mangas')
    else:
        formulario = Mangaformulario(initial={"nombreDelManga": manga.nombreDelManga, "autor": manga.autor, "email": manga.email})

    return render(request, "editar_manga.html", {"formulario": formulario, "manga_nombreDelManga": nombreDelManga})


# ------------- VIDEOJUEGOS -------------------

def videojuegos(request):
    return render(request, 'videojueos.html')


def usuarios_videojuego(request):
    
    if request.method == "POST":
        nombreDelJuego = request.POST.get("nombreDelJuego")
        autor = request.POST.get("autor")
        email = request.POST.get("email")
        print(f"""
              Nombre: {nombreDelJuego}
              Autor: {autor}
              Email: {email}
              """)
        
        juego = Videojuego(nombreDelJuego=nombreDelJuego, autor=autor, email=email)
        juego.save()
        return render(request, 'index.html')
        
    return render(request, 'usuarios_videojuego.html')


class VideojuegoList(ListView):
    model = Videojuego
    template_name = 'juego_list.html'

class VideojuegoDetalle(DetailView):
    model = Videojuego
    template_name = 'videojuegos_detalle.html'
    
class VideojuegoCreacion(CreateView):
    model = Videojuego
    fields = ['nombreDelJuego', 'email', 'autor']
    template_name = 'juego_form.html'
    success_url = "/blog/videojuego/list"
    
class VideojuegoUpdate(UpdateView):
    model = Videojuego
    fields = ['nombreDelJuego', 'email', 'autor']
    template_name = 'juego_form.html'
    success_url = "/blog/videojuego/list"
    
class VideojuegoDelete(DeleteView):
    model = Videojuego
    template_name = 'juego_confirm_delete.html'
    success_url = "/blog/videojuego/list"


# ------------- LOGIN -------------------


def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data =request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)

                return render(request, 'index.html', {"mensaje": f"Bienvenido '{username}'"})
            else:
                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'index.html', {"mensaje": "Datos form incorrectos"})
    
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def registrar(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST) 

        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            form.save()
            
            return render(request, 'index.html', {"mensaje": f"Se dio de alta el usuario {username}"})
    
    form = UserCreationForm()
    return render(request, 'registrar.html', {"form": form})
    
    

