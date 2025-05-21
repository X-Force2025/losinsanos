class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value  # Valor del nodo (operador o operando)
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho

def build_expression_tree(postfix):
    """Construye un árbol de expresión a partir de una expresión en notación postfija"""
    stack = []  # Pila para mantener nodos temporales

    for token in postfix:  # Recorre cada token de izquierda a derecha
        if token not in '+-*/':  # Si el token es operando
            stack.append(Node(token))  # Se crea nodo hoja
        else:
            right = stack.pop()  # Extrae el operando derecho
            left = stack.pop()   # Extrae el operando izquierdo
            node = Node(token)   # Crea nodo operador
            node.left = left     # Asigna hijo izquierdo
            node.right = right   # Asigna hijo derecho
            stack.append(node)   # Añade nuevo subárbol a la pila

    return stack[-1]  # La raíz del árbol es el único elemento restante
