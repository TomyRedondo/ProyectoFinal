# ProyectoFinal
Proyecto en Python en Django - Tomás Redondo

Vistas (views.py)

1. ´index(request)´
- Descripción: 
    Renderiza la página de inicio ('index.html').
- Acciones: 
    Muestra la página de inicio del proyecto.


2. ´mangas(request)´
- Descripción:
    Procesa la entrada de datos para la creación de mangas y renderiza el formulario ('crear_manga.html').
- Acciones: 
    Verifica si la solicitud es un POST.
    Valida y guarda los datos del formulario en la base de datos si son válidos.
    Renderiza el formulario para la creación de mangas.


3. ´usuarios_manga(request)´
- Descripción:
    Procesa la entrada de datos para la creación de mangas por parte de usuarios y renderiza el formulario ('usuarios_manga.html').
- Acciones: 
    Verifica si la solicitud es un POST.
    Valida y guarda los datos del formulario en la base de datos si son válidos.
    Renderiza el formulario para la creación de mangas por parte de usuarios.


4. ´busqueda_manga(request)´
- Descripción:
    Renderiza la página de búsqueda de mangas ('busqueda_manga.html').
- Acciones: 
    Verifica si la solicitud es un GET.
    Obtiene el parámetro de búsqueda del manga.


5. ´buscar_manga(request)´
- Descripción:
    Procesa la búsqueda de mangas.
- Acciones: 
    Verifica si la solicitud es un GET.
    Obtiene el nombre del manga a buscar.
    Busca mangas que coincidan con el nombre y los muestra en la página de resultados ('busqueda.html').


6. ´leer_mangas(request)´
- Descripción: 
    Muestra la lista de todos los mangas en la base de datos.
- Acciones: 
    Obtiene todos los mangas de la base de datos y los muestra en la página ('leer_mangas.html').


7. ´eliminar_manga(request, nombreDelManga)´
- Descripción:
    Elimina un manga específico de la base de datos.
- Acciones: 
    Elimina el manga con el nombre proporcionado.
    Obtiene la lista actualizada de mangas y la muestra en la página (leer_mangas.html).


8. ´editar_manga(request, nombreDelManga)´
- Descripción:
    Permite la edición de un manga existente.
- Acciones: 
    Obtiene el manga específico con el nombre proporcionado.
    Renderiza el formulario de edición (editar_manga.html).
    Procesa el formulario si es un POST y actualiza los datos del manga.


9. ´videojuegos(request)´
- Descripción:
    Renderiza la página de videojuegos (videojuegos.html).
- Acciones: 
    Muestra la página de videojuegos del proyecto.


10. ´usuarios_videojuego(request)´
- Descripción:
    Procesa la entrada de datos para la creación de videojuegos por parte de usuarios y renderiza el formulario (usuarios_videojuego.html).
- Acciones: 
    Verifica si la solicitud es un POST.
    Valida y guarda los datos del formulario en la base de datos si son válidos.
    Renderiza el formulario para la creación de videojuegos por parte de usuarios.


11. ´login_request(request)´
- Descripción:
    Procesa la solicitud de inicio de sesión.
- Acciones: 
    Verifica si la solicitud es un POST.
    Valida las credenciales de inicio de sesión.
    Inicia sesión si las credenciales son válidas y muestra la página de inicio.


12. ´registrar(request)´
- Descripción:
    Procesa la solicitud de registro de usuario.
- Acciones: 
    Verifica si la solicitud es un POST.
    Valida y crea un nuevo usuario.
    Muestra la página de inicio si el registro es exitoso.

------------------------------------------------------------------------------------------

Clases de Vista

1. ´VideojuegoList(ListView)´
- Descripción:
    Lista todos los videojuegos.
- Acciones: 
    Utiliza la clase genérica ListView para mostrar todos los videojuegos en una lista (juego_list.html).


2. ´VideojuegoDetalle(DetailView)´
- Descripción:
    Muestra detalles de un videojuego específico.
- Acciones: 
    Utiliza la clase genérica DetailView para mostrar detalles específicos de un videojuego (videojuego_detalle.html).


3. ´VideojuegoCreacion(CreateView)´
- Descripción:
    Permite la creación de nuevos videojuegos.
- Acciones: 
    Utiliza la clase genérica CreateView para renderizar el formulario de creación y gestionar el proceso de creación.


4. ´VideojuegoUpdate(UpdateView)´
- Descripción:
    Permite la edición de un videojuego existente.
- Acciones: 
    Utiliza la clase genérica UpdateView para renderizar el formulario de edición y gestionar el proceso de actualización.


5. ´VideojuegoDelete(DeleteView)´
- Descripción:
    Permite la eliminación de un videojuego existente.
- Acciones: 
    Utiliza la clase genérica DeleteView para renderizar la confirmación de eliminación y gestionar el proceso de eliminación.
