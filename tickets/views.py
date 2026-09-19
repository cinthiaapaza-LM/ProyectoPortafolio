from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket, Usuario

def crear_tickets_prueba(request):
    # Necesitas al menos un usuario ya creado en el admin
    usuario = Usuario.objects.first()

    # Crear el primer ticket de prueba
    Ticket.objects.create(
        titulo="Ticket de prueba 1",
        descripcion="Prueba de la cola FIFO",
        estado="Pendiente",
        usuario=usuario
    )
    messages.success(request, "Ticket 1 creado")

    # Crear el segundo ticket de prueba
    Ticket.objects.create(
        titulo="Ticket de prueba 2",
        descripcion="Prueba de la cola FIFO",
        estado="Pendiente",
        usuario=usuario
    )
    messages.success(request, "Ticket 2 creado")

    return redirect('mostrar_mensajes')


def mostrar_mensajes(request):
    return render(request, 'tickets/mensajes.html')