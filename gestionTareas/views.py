from django.shortcuts import render

# Create your views here.
def ingresar(request):
    return render(request,'gestionTareas/ingresar.html')
def dashboard(request):
    return render(request,'gestionTareas/dashboard.html')
def creacion(request):
    return render(request,'gestionTareas/creacion.html')
def detalle(request):
    return render(request,'gestionTareas/detalle.html')
def edicion(request):
    return render(request,'gestionTareas/edicion.html')