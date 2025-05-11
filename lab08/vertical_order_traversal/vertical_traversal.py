from collections import defaultdict, deque  # Importa defaultdict para agrupar por columnas y deque para la cola BFS

# Clase que representa un nodo del árbol binario
class TreeNode:
    def __init__(self, val):             # Constructor que recibe el valor del nodo
        self.val = val                   # Asigna el valor recibido
        self.left = None                 # Inicializa el hijo izquierdo como None
        self.right = None                # Inicializa el hijo derecho como None

# Clase auxiliar para construir un árbol binario a partir de una lista (nivel por nivel)
class BinaryTree:
    def __init__(self):                  # Constructor de la clase
        self.root = None                 # Inicializa la raíz del árbol como vacía

    def build_tree_from_list(self, values):  # Construye el árbol desde una lista de valores (formato de recorrido por niveles)
        if not values:                      # Si la lista está vacía
            self.root = None                # No hay árbol que construir
            return

        self.root = TreeNode(values[0])     # El primer valor de la lista es la raíz
        queue = deque([self.root])          # Cola para recorrer el árbol por niveles
        i = 1                               # Índice para recorrer la lista

        while queue and i < len(values):    # Mientras haya nodos por procesar y valores en la lista
            current = queue.popleft()       # Obtiene el nodo actual desde la cola

            if values[i] is not None:       # Si el siguiente valor no es None
                current.left = TreeNode(values[i])  # Crea el hijo izquierdo
                queue.append(current.left)          # Lo añade a la cola
            i += 1

            if i < len(values) and values[i] is not None:  # Verifica si hay un valor válido para el hijo derecho
                current.right = TreeNode(values[i])         # Crea el hijo derecho
                queue.append(current.right)                 # Lo añade a la cola
            i += 1

# Función que realiza el recorrido vertical del árbol binario
def vertical_order_traversal(root):
    if not root:                           # Si el árbol está vacío
        return []                          # Retorna lista vacía

    col_table = defaultdict(list)          # Diccionario para agrupar los nodos por columna (distancia horizontal)
    queue = deque([(root, 0)])             # Cola para recorrido BFS con tuplas (nodo, columna)

    while queue:                           # Mientras haya elementos en la cola
        node, col = queue.popleft()        # Extrae un nodo y su columna correspondiente
        col_table[col].append(node.val)    # Añade el valor del nodo a su columna correspondiente

        if node.left:                      # Si el nodo tiene hijo izquierdo
            queue.append((node.left, col - 1))  # Lo agrega a la cola con columna -1

        if node.right:                     # Si el nodo tiene hijo derecho
            queue.append((node.right, col + 1))  # Lo agrega a la cola con columna +1

    return [col_table[x] for x in sorted(col_table.keys())]  # Retorna los valores agrupados y ordenados por columna
