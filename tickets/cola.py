class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if self.elementos:
            return self.elementos.pop(0)
        return None
def asignar_siguiente_ticket(cola):
    ticket = cola.dequeue()

    if ticket is not None:
        print("Ticket asignado:", ticket.titulo)
        return ticket

    print("No hay tickets pendientes.")
    return None
class TicketPrueba:
    def __init__(self, titulo):
        self.titulo = titulo
cola = Cola()

ticket1 = TicketPrueba("Error al iniciar sesión")
ticket2 = TicketPrueba("Problema con el registro")
ticket3 = TicketPrueba("Error al cargar el perfil")
ticket4 = TicketPrueba("Problema con contraseña")

cola.enqueue(ticket1)
cola.enqueue(ticket2)
cola.enqueue(ticket3)
cola.enqueue(ticket4)

print("Orden de atención:")

asignar_siguiente_ticket(cola)
asignar_siguiente_ticket(cola)
asignar_siguiente_ticket(cola)
asignar_siguiente_ticket(cola)