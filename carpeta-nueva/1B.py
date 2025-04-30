def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Caso base: Si la cadena tiene 0 o 1 caracteres, es un palíndromo
    if len(cadena) <= 1:
        return True
    
    # Comparar los primeros y últimos caracteres
    if cadena[0] != cadena[-1]:
        return False
    
    # Llamada recursiva para los caracteres internos
    return es_palindromo(cadena[1:-1])

# Ejemplo de uso
cadena = input("Introduce una cadena: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
