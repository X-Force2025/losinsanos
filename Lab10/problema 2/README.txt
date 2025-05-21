# Challenge 2: Build Expression Tree from Postfix

## Enunciado
Construir un árbol de expresiones a partir de una expresión postfija (postfix).

## Algoritmo
1. Usamos una pila para almacenar nodos temporales.
2. Recorremos los tokens de izquierda a derecha.
3. Si encontramos un operando, creamos un nodo hoja.
4. Si encontramos un operador, sacamos dos nodos de la pila y creamos un nuevo nodo con ellos como hijos.
5. Al final, el nodo restante en la pila es la raíz del árbol.

## Complejidad
Tiempo: O(n) donde n es la cantidad de tokens.
Espacio: O(n) para la pila.

## Archivos
- `expression_tree.py`: Contiene la clase `Node` y la función `build_expression_tree` con comentarios línea por línea.
- `tests.py`: Casos de prueba para validar la estructura del árbol.
- `README.txt`: Este resumen del problema, enfoque, y archivos.
