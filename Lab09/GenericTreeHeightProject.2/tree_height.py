# Clase que representa un nodo de un árbol genérico
class GenericTreeNode:
    def __init__(self, value):
        self.value = value        # Guarda el valor del nodo (por ejemplo, 'A', '1', etc.)
        self.children = []        # Lista de hijos (nodos conectados a este nodo)

# Clase que representa el árbol genérico completo
class GenericTree:
    def __init__(self, root=None):
        self.root = root          # Nodo raíz del árbol (puede ser None si el árbol está vacío)

    # Método que calcula la altura del árbol
    def height(self):
        """Calcula la altura del árbol"""

        # Función auxiliar recursiva para recorrer el árbol desde cualquier nodo
        def _height(node):
            if not node:
                return -1         # Caso base: Si el nodo es None, el árbol está vacío → altura = -1

            if not node.children:
                return 0          # Caso base: Si no tiene hijos, es una hoja → altura = 0

            # Calcular la altura de cada hijo recursivamente
            child_heights = [_height(child) for child in node.children]

            # Retornar 1 + la altura máxima de los hijos
            return 1 + max(child_heights)

        # Llamar a la función recursiva comenzando desde la raíz
        return _height(self.root)
# -------------------
# Test 1: Árbol vacío
# -------------------
empty_tree = GenericTree(None)              # Árbol sin raíz
print(empty_tree.height() == -1)            # Debería imprimir True porque el árbol está vacío

# -----------------------------
# Test 2: Árbol con un solo nodo
# -----------------------------
single = GenericTree(GenericTreeNode('A'))  # Solo un nodo, sin hijos
print(single.height() == 0)                 # Debería imprimir True (altura = 0)

# -------------------------------
# Test 3: Árbol lineal A → B → C
# -------------------------------
linear_root = GenericTreeNode('A')          # Nodo raíz
linear_b = GenericTreeNode('B')             # Hijo de A
linear_c = GenericTreeNode('C')             # Hijo de B
linear_root.children = [linear_b]           # A tiene un hijo: B
linear_b.children = [linear_c]              # B tiene un hijo: C
linear_tree = GenericTree(linear_root)      # Crear árbol con raíz A
print(linear_tree.height() == 2)            # Altura: A→B→C → 2 aristas → altura = 2

# ---------------------------------------------
# Test 4: Árbol balanceado con múltiples hijos
# ---------------------------------------------
balanced_root = GenericTreeNode('A')        # Nodo raíz

# Crear nodos hijos
b = GenericTreeNode('B')
c = GenericTreeNode('C')
d = GenericTreeNode('D')
e = GenericTreeNode('E')
f = GenericTreeNode('F')
g = GenericTreeNode('G')
h = GenericTreeNode('H')

# Conectar los hijos a la raíz
balanced_root.children = [b, c, d]          # A tiene 3 hijos: B, C, D
b.children = [e, f, g]                      # B tiene 3 hijos: E, F, G
d.children = [h]                            # D tiene 1 hijo: H

balanced_tree = GenericTree(balanced_root)
print(balanced_tree.height() == 2)          # Camino más largo: A → B → E → altura = 2

# ----------------------------------------
# Test 5: Árbol desbalanceado (más profundo)
# ----------------------------------------
unbalanced_root = GenericTreeNode('A')      # Nodo raíz
ub_b = GenericTreeNode('B')
ub_c = GenericTreeNode('C')
ub_d = GenericTreeNode('D')

# Conectar en forma lineal: A → B → C → D
unbalanced_root.children = [ub_b]
ub_b.children = [ub_c]
ub_c.children = [ub_d]

unbalanced_tree = GenericTree(unbalanced_root)
print(unbalanced_tree.height() == 3)        # Altura: 3 (3 aristas entre nodos)
