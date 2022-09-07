from . import views
from django.urls import path

app_name = 'gestionTareas'

urlpatterns = [
    path('',views.ingresar,name='ingresar'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('creacion',views.creacion,name='creacion'),
    path('detalle',views.detalle,name='detalle'),
    path('edicion',views.edicion,name='edicion'),

    
]