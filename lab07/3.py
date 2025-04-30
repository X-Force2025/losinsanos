class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val                 # Valor del nodo
        self.left = left               # Referencia al hijo izquierdo
        self.right = right             # Referencia al hijo derecho

def mirror_tree(root):
    if root is None:                  # Caso base: si el nodo es nulo, no se hace nada
        return None
    root.left, root.right = root.right, root.left  # Se intercambian los hijos izquierdo y derecho
    mirror_tree(root.left)           # Llamada recursiva al hijo izquierdo (originalmente era derecho)
    mirror_tree(root.right)          # Llamada recursiva al hijo derecho (originalmente era izquierdo)
    return root

# Imprime el árbol en orden por niveles
def print_tree(root):
    if not root:
        print("Árbol vacío")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("None")
    while result and result[-1] == "None":
        result.pop()
    print(" -> ".join(result))
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("ANTES:")
print_tree(root)
mirror_tree(root)
print("DESPUÉS:")
print_tree(root)

empty_tree = None
print("ANTES:")
print_tree(empty_tree)
mirror_tree(empty_tree)
print("DESPUÉS:")
print_tree(empty_tree)

single = TreeNode(42)
print("ANTES:")
print_tree(single)
mirror_tree(single)
print("DESPUÉS:")
print_tree(single)
