# Definimos una clase para un nodo de árbol binario
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Valor del nodo
        self.left = left  # Hijo izquierdo del nodo
        self.right = right  # Hijo derecho del nodo

# Función para contar la cantidad de nodos hoja en un árbol binario
def count_leaves(root):
    if root is None:
        return 0  # Si el árbol está vacío (o el subárbol es vacío), retornamos 0
    if root.left is None and root.right is None:
        return 1  # Si el nodo no tiene hijos, es un nodo hoja → retornamos 1
    # Llamadas recursivas para contar las hojas en los subárboles izquierdo y derecho
    return count_leaves(root.left) + count_leaves(root.right)

# Función para probar la función count_leaves con diferentes casos
def test_count_leaves():
    # Caso de prueba 1: Árbol normal
    root = TreeNode(1)  # Nodo raíz con valor 1
    root.left = TreeNode(2)  # Hijo izquierdo con valor 2
    root.right = TreeNode(3)  # Hijo derecho con valor 3
    root.left.left = TreeNode(4)  # Hijo izquierdo de nodo 2 con valor 4
    root.left.right = TreeNode(5)  # Hijo derecho de nodo 2 con valor 5
    assert count_leaves(root) == 3  # Hojas esperadas: 4, 5, 3 → total = 3
    
    # Caso de prueba 2: Árbol vacío
    empty_tree = None  # Árbol vacío
    assert count_leaves(empty_tree) == 0  # Cantidad de hojas esperada = 0
    
    # Caso de prueba 3: Árbol con un solo nodo
    single_node = TreeNode(1)  # Árbol con solo un nodo raíz
    assert count_leaves(single_node) == 1  # La raíz es hoja → esperado = 1
    
    # Caso de prueba 4: Sin nodos hoja en el primer nivel
    no_leaves_at_first = TreeNode(1)  # Nodo raíz
    no_leaves_at_first.left = TreeNode(2)  # Hijo izquierdo
    no_leaves_at_first.right = TreeNode(3)  # Hijo derecho
    assert count_leaves(no_leaves_at_first) == 2  # Hojas son nodos 2 y 3 → esperado = 2
    
    # Caso de prueba 5: Todos los nodos son hojas excepto la raíz
    all_leaves = TreeNode(1)  # Nodo raíz
    all_leaves.left = TreeNode(2)  # Hijo izquierdo
    all_leaves.right = TreeNode(3)  # Hijo derecho
    all_leaves.left.left = TreeNode(4)  # Nodo hoja
    all_leaves.left.right = TreeNode(5)  # Nodo hoja
    all_leaves.right.left = TreeNode(6)  # Nodo hoja
    all_leaves.right.right = TreeNode(7)  # Nodo hoja
    assert count_leaves(all_leaves) == 4  # Hojas son 4, 5, 6, 7 → esperado = 4

# Ejecutamos todas las pruebas
test_count_leaves()  # Llamada a la función de prueba
print("All test cases passed!")  # Imprime el mensaje si todas las pruebas pasan
