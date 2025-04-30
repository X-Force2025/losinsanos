def mostrar_arbol_TF(n):
    def generar_combinaciones(prefijo, nivel):
        if nivel == 0:
            return [prefijo] if prefijo else ['""']
        return [c for opcion in ['T', 'F'] 
                for c in generar_combinaciones(prefijo + opcion, nivel - 1)]

    def imprimir_arbol(combinaciones, n):
        ancho = 2 ** (n + 2)  # Ajuste de espaciado
        for nivel in range(n + 1):
            comb_nivel = [c for c in combinaciones if len(c.replace('"', '')) == nivel or (nivel == 0 and c == '""')]
            espacios = " " * (ancho // (2 ** (nivel + 1)))
            linea = espacios.join(comb_nivel)
            print(" " * (ancho // (2 ** (nivel + 1))) + linea)
            if nivel < n:
                print(" " * (ancho // (2 ** (nivel + 2)) - 1) + "/ \\" * len(comb_nivel))

    combinaciones = generar_combinaciones("", n)
    imprimir_arbol(['""'] + [c for c in combinaciones if c != '""'], n)

# Ejemplo para n=2
mostrar_arbol_TF(2)
