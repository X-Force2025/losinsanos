def invertir_con_pila(cadena):
    pila = []
    # Insertar todos los caracteres en la pila
    for caracter in cadena:
        pila.append(caracter)
    
    cadena_invertida = []
    # Extraer todos los caracteres (orden LIFO)
    while pila:
        cadena_invertida.append(pila.pop())
    
    return ''.join(cadena_invertida)

# Pruebas
print(invertir_con_pila("hola"))   # Salida: "aloh"
print(invertir_con_pila("abc"))    # Salida: "cba"
print(invertir_con_pila("a"))      # Salida: "a"
print(invertir_con_pila(""))       # Salida: ""
