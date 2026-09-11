class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if self.elementos:
            return self.elementos.pop()
        return None
class Ticket:
    def __init__(self, codigo, estado="Abierto"):
        self.codigo = codigo
        self.estado = estado
        self.historial = Pila()

    def cambiar_estado(self, nuevo_estado):
        self.historial.push(self.estado)
        self.estado = nuevo_estado

    def deshacer_ultimo_cambio(self):
        estado_anterior = self.historial.pop()

        if estado_anterior is not None:
            self.estado = estado_anterior

        return self.estado
ticket = Ticket("T001")
print("Estado inicial:", ticket.estado)

ticket.cambiar_estado("En progreso")
print("Cambio 1:", ticket.estado)

ticket.cambiar_estado("En revisión")
print("Cambio 2:", ticket.estado)

ticket.cambiar_estado("Resuelto")
print("Cambio 3:", ticket.estado)

print("Estado antes de deshacer:", ticket.estado)
ticket.deshacer_ultimo_cambio()

print("Estado después de deshacer:", ticket.estado)

# cambio-2
