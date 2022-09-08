from django.shortcuts import render
from gestionTareas.models import tarea, usuarios
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.
def ingresar(request):
    #lo comente porque nose que hice mal ingeniero hice todo lo que se hizo en clase

    # if request.method == 'POST':
    #     nombre = request.POST.get('nombreUsuario')
    #     passwordUsuario = request.POST.get('passwordUsuario')
    #     #Validacion de informacion
    #     usuario_registrado = 0
    #     usuarios_totales = usuario.objects.all()

    #     for usuario in usuarios_totales:
    #         if usuario.nombre == nombre and usuario.psw_usuario == passwordUsuario:
    #             usuario_registrado = 1
        
    #     if usuario_registrado == 1:
    #         return HttpResponseRedirect(reverse('gestionTareas:dashboard'))
    #     else:
    #         return render(request,'gestionTareas/ingresar.html',{
    #             'mensaje':'Los datos ingresados son incorrectos',
    #         })
    return render(request,'gestionTareas/ingresar.html')
def dashboard(request):
    
    return render(request,'gestionTareas/dashboard.html')
def creacion(request):
    return render(request,'gestionTareas/creacion.html')
def detalle(request):
    return render(request,'gestionTareas/detalle.html')
def edicion(request):
    return render(request,'gestionTareas/edicion.html')