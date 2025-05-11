# Clase que representa un nodo del árbol binario
class TreeNode:
    def __init__(self, value):
        self.val = value          # Almacena el valor del nodo
        self.left = None          # Referencia al hijo izquierdo
        self.right = None         # Referencia al hijo derecho

# Clase que representa un Árbol Binario de Búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None          # Inicializa el árbol con raíz vacía

    # Función para insertar un valor en el árbol
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)  # Inserta recursivamente a partir de la raíz

    # Función recursiva para insertar un valor
    def _insert_recursive(self, node, value):
        if not node:                          # Si el nodo actual es None, crea uno nuevo
            return TreeNode(value)
        if value < node.val:                  # Si el valor es menor, va al subárbol izquierdo
            node.left = self._insert_recursive(node.left, value)
        else:                                 # Si el valor es mayor o igual, va al derecho
            node.right = self._insert_recursive(node.right, value)
        return node                           # Devuelve el nodo actualizado

    # Devuelve una lista con el recorrido inorder (ordenado)
    def inorder(self):
        result = []                           # Lista para almacenar los valores ordenados
        self._inorder_recursive(self.root, result)  # Llama a la función auxiliar con la raíz
        return result                         # Retorna la lista

    # Función recursiva para el recorrido inorder
    def _inorder_recursive(self, node, result):
        if not node:                          # Caso base: nodo vacío
            return
        self._inorder_recursive(node.left, result)  # Recorre el subárbol izquierdo
        result.append(node.val)                      # Agrega el valor del nodo actual
        self._inorder_recursive(node.right, result)  # Recorre el subárbol derecho

# Función que recibe un BST y devuelve uno balanceado
def balance_bst(bst):
    # Función auxiliar para construir el árbol balanceado desde una lista ordenada
    def build_balanced_tree(sorted_vals):
        if not sorted_vals:                    # Caso base: lista vacía
            return None
        mid = len(sorted_vals) // 2            # Calcula el índice del elemento central
        node = TreeNode(sorted_vals[mid])      # Crea el nodo raíz con el valor central
        node.left = build_balanced_tree(sorted_vals[:mid])        # Construye recursivamente el subárbol izquierdo
        node.right = build_balanced_tree(sorted_vals[mid + 1:])   # Construye recursivamente el subárbol derecho
        return node                             # Devuelve el nodo raíz construido

    sorted_nodes = bst.inorder()               # Obtiene los valores ordenados del BST original
    new_bst = BinarySearchTree()               # Crea un nuevo árbol vacío
    new_bst.root = build_balanced_tree(sorted_nodes)  # Asigna la nueva raíz balanceada
    return new_bst                             # Devuelve el árbol balanceado

# Función para imprimir un árbol (o subárbol) en orden inorder como lista
def print_tree_inorder(node):
    if not node:
        return []                              # Si el nodo es None, devuelve lista vacía
    return print_tree_inorder(node.left) + [node.val] + print_tree_inorder(node.right)
    # Combina recorrido del subárbol izquierdo + valor actual + subárbol derecho
