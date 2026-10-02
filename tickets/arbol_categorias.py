class CategoriaTicket:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, categoria):
        self.subcategorias.append(categoria)


def recorrer_categorias(nodo, nivel=0):
    print("  " * nivel + "- " + nodo.nombre)

    for subcategoria in nodo.subcategorias:
        recorrer_categorias(subcategoria, nivel + 1)


# Categorías principales
hardware = CategoriaTicket("Hardware")
software = CategoriaTicket("Software")
redes = CategoriaTicket("Redes")

# Subcategorías de Hardware
hardware.agregar_subcategoria(CategoriaTicket("Impresoras"))
hardware.agregar_subcategoria(CategoriaTicket("Computadoras"))

# Subcategorías de Software
software.agregar_subcategoria(CategoriaTicket("Sistema operativo"))
software.agregar_subcategoria(CategoriaTicket("Aplicaciones"))

# Subcategorías de Redes
redes.agregar_subcategoria(CategoriaTicket("Internet"))
redes.agregar_subcategoria(CategoriaTicket("WiFi"))


# Categoría raíz
categorias = CategoriaTicket("Categorías de Tickets")

categorias.agregar_subcategoria(hardware)
categorias.agregar_subcategoria(software)
categorias.agregar_subcategoria(redes)


# Recorrer el árbol
recorrer_categorias(categorias)