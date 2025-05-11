class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val    # Valor almacenado en el nodo
        self.left = left  # Referencia al hijo izquierdo
        self.right = right # Referencia al hijo derecho

class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol (inicialmente vacía)
    
    def build_tree_from_list(self, lst):
        """Construye un árbol binario a partir de una lista en formato nivel por nivel"""
        if not lst:  # Si la lista está vacía
            return None
        
        self.root = TreeNode(lst[0])  # El primer elemento es la raíz
        queue = [self.root]  # Usamos una cola para construcción por niveles
        i = 1  # Índice para recorrer la lista
        
        while queue and i < len(lst):
            current = queue.pop(0)  # Tomamos el primer nodo de la cola
            
            # Procesamos el hijo izquierdo
            if i < len(lst) and lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            i += 1
            
            # Procesamos el hijo derecho
            if i < len(lst) and lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            i += 1

def prune_tree(root, target):
    """
    Poda un árbol binario eliminando todos los subárboles que no contienen el valor objetivo.
    Retorna el árbol modificado.
    """
    # Caso base: si llegamos a un nodo nulo, retornamos nulo
    if not root:
        return None
    
    # Primero procesamos los hijos recursivamente (post-order traversal)
    root.left = prune_tree(root.left, target)
    root.right = prune_tree(root.right, target)
    
    # Después de procesar los hijos, decidimos si este nodo debe permanecer
    # Si el valor no es el objetivo y no tiene hijos, lo podamos (retornamos None)
    if root.val != target and not root.left and not root.right:
        return None
    
    # En cualquier otro caso, mantenemos el nodo
    return root

def test_prune_tree():
    """Función de prueba para verificar el correcto funcionamiento de prune_tree"""
    print("Iniciando pruebas...")
    
    # Test Case 1: Árbol normal, podar por valor 1
    print("\nTest 1: Árbol normal, podar por valor 1")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    pruned1 = prune_tree(tree1.root, 1)
    assert pruned1.val == 1
    assert pruned1.left is None
    assert pruned1.right is None
    print("Test 1 pasado ✓")
    
    # Test Case 2: Árbol con múltiples ocurrencias del valor objetivo
    print("\nTest 2: Árbol con múltiples 1s")
    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(1)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.right = TreeNode(1)
    pruned2 = prune_tree(tree2.root, 1)
    assert pruned2.val == 1
    assert pruned2.left.val == 2
    assert pruned2.left.left.val == 1
    assert pruned2.left.right is None
    assert pruned2.right.val == 3
    assert pruned2.right.right.val == 1
    assert pruned2.right.left is None
    print("Test 2 pasado ✓")
    
    # Test Case 3: Árbol vacío
    print("\nTest 3: Árbol vacío")
    tree3 = BinaryTree()
    pruned3 = prune_tree(tree3.root, 1)
    assert pruned3 is None
    print("Test 3 pasado ✓")
    
    # Test Case 4: Valor objetivo no existe en el árbol
    print("\nTest 4: Valor objetivo no existe")
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    pruned4 = prune_tree(tree4.root, 4)
    assert pruned4 is None
    print("Test 4 pasado ✓")
    
    # Test Case 5: Todos los nodos tienen el valor objetivo
    print("\nTest 5: Todos los nodos con valor objetivo")
    tree5 = BinaryTree()
    tree5.root = TreeNode(5)
    tree5.root.left = TreeNode(5)
    tree5.root.right = TreeNode(5)
    pruned5 = prune_tree(tree5.root, 5)
    assert pruned5.val == 5
    assert pruned5.left.val == 5
    assert pruned5.right.val == 5
    print("Test 5 pasado ✓")
    
    print("\n¡Todas las pruebas pasaron con éxito! ✅")

# Ejecutar las pruebas
test_prune_tree()