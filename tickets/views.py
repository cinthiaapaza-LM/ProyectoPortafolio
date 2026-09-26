from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket, Usuario
from .cola_circular import ColaCircular

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

def lista_tickets(request):
    tickets_pendientes = Ticket.objects.filter(
        estado="Pendiente"
    ).order_by("id")

    cola = ColaCircular()

    for ticket in tickets_pendientes:
        cola.enqueue(ticket)

    tickets = []

    while not cola.esta_vacia():
        ticket = cola.dequeue()
        tickets.append(ticket)

    return render(
        request,
        "tickets/lista_tickets.html",
        {"tickets": tickets}
    )

def detalle_ticket(request, id):
    ticket = Ticket.objects.get(id=id)

    return render(
        request,
        "tickets/detalle_ticket.html",
        {"ticket": ticket}
    )