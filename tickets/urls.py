from django.urls import path
from . import views

urlpatterns = [
    path('crear-prueba/', views.crear_tickets_prueba, name='crear_tickets_prueba'),
    path('mensajes/', views.mostrar_mensajes, name='mostrar_mensajes'),
]