def buscar_articulo(articulos, titulo_buscado):
    inicio = 0
    fin = len(articulos) - 1
    comparaciones = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2

        comparaciones += 1

        titulo_actual = articulos[medio].titulo.lower()
        titulo_buscado_lower = titulo_buscado.lower()

        if titulo_actual == titulo_buscado_lower:
            return articulos[medio], comparaciones

        elif titulo_actual < titulo_buscado_lower:
            inicio = medio + 1

        else:
            fin = medio - 1

    return None, comparaciones