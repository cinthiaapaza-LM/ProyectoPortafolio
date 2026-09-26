class ColaCircular:
    def __init__(self, capacidad=4):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamano = 0

    def esta_vacia(self):
        return self.tamano == 0

    def esta_llena(self):
        return self.tamano == self.capacidad

    def enqueue(self, ticket):
        if self.esta_llena():
            self.redimensionar()

        self.elementos[self.final] = ticket
        self.final = (self.final + 1) % self.capacidad
        self.tamano += 1

    def dequeue(self):
        if self.esta_vacia():
            return None

        ticket = self.elementos[self.frente]
        self.elementos[self.frente] = None

        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1

        return ticket

    def redimensionar(self):
        nueva_capacidad = self.capacidad * 2
        nuevos_elementos = [None] * nueva_capacidad

        for i in range(self.tamano):
            nuevos_elementos[i] = self.elementos[
                (self.frente + i) % self.capacidad
            ]

        self.elementos = nuevos_elementos
        self.capacidad = nueva_capacidad
        self.frente = 0
        self.final = self.tamano