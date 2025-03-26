def factorial(n):
    # Caso base: 0! = 1 y 1! = 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    print(factorial(9))  # Output: 120