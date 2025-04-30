class TreeNode:
    def __init__(self, val=0, left=None, right=None): #constructor que tienen parametros que toman los valores de val, left ,right con valores predeterminados
        self.val = val #instancia de la clase TreeNode que toma el valor de val
        self.left = left #instancia de la clase TreeNode que toma el valor de left
        self.right = right #instancia de la clase TreeNode que toma el valor de right

def tree_height(root): #funcion que sirve para poder calcular la altura de un arbol binario
    # Caso base: un árbol vacío tiene altura -1
    if root is None: #condiciona que evalue si la riz de arbol que es root es igual a None
        return -1 # en caso sea si se retorna -1 que signifca que no hay raiz ya que raiz vale 0 y -1 es menor que 0
    
    # Caso recursivo: la altura es 1 + la altura máxima de los subárboles
    left_height = tree_height(root.left) #se llama a la funcion tree_height para calcular la altura del subarbol izquierdo
    right_height = tree_height(root.right)#se llama a la funcion tree_height para calcular la altura del subarbol derecho
    # Si el árbol es un nodo hoja, la altura es 0 esto sucede si no hay mas nodos en el arbol
    
    # Retornar la altura máxima del subárbol izquierdo o derecho más 1
    return max(left_height, right_height) + 1 # retorna el maximo valor de los sub arboles izquierdo y derecho mas 1 lo que signfica que si la riz es 1 los nodos que nacen de esa raiz son 2 y 3 los subnodos son 4 y 5 de 2 al final tendria 1 subnivel +1 seria 2 al final el resultado es 2

# Casos de prueba
def test_tree_height():# funcion que sirve para probar la funcion tree_height
    # Caso de Prueba 1: Árbol normal
    root = TreeNode(1) # se crea la raiz del arbol con el valor 1
    root.left = TreeNode(2) # se crea el subarbol izquierdo con el valor 2
    root.right = TreeNode(3) # se crea el subarbol derecho con el valor 3
    root.left.left = TreeNode(4) # se crea el subarbol izquierdo del subarbol izquierdo con el valor 4
    root.left.right = TreeNode(5) # se crea el subarbol derecho del subarbol izquierdo con el valor 5
    
    # Caso de Prueba 2: Árbol vacío
    empty_tree = None # se crea un arbol vacio al no tener raiz
    
    # Caso de Prueba 3: Árbol de un solo nodo
    single_node = TreeNode(1) # se crea un arbol con un solo nodo que es la raiz con el valor 1
    
    # Ejecutar pruebas e imprimir resultados
    casos_prueba = [ # se crea una lista de casos de prueba con el nombre del caso, el arbol y el resultado esperado
        ("Árbol Normal", root, 2), # donde "Arbol Normal" es el nombre del caso, root es el arbol y 2 es la altura esperada
        ("Árbol Vacío", empty_tree, -1), # donde "Arbol Vacio" es el nombre del caso, empty_tree es el arbol y -1 es la altura esperada
        ("Árbol de Un Solo Nodo", single_node, 0) # donde "Arbol de Un Solo Nodo" es el nombre del caso, single_node es el arbol y 0 es la altura esperada
    ]
    
    for nombre, arbol, esperado in casos_prueba: # se itera sobre cada caso de prueba
        resultado = tree_height(arbol) #se llama a la funcion tree_height para calcular la altura del arbol
        estado = "ÉXITO" if resultado == esperado else "FALLO" #se evalua si el resultado es igual al esperado y se asigna el estado de la prueba
        print(f"Prueba: {nombre} - Esperado: {esperado}, Obtenido: {resultado} - {estado}") #se imprime el resultado de la prueba con el nombre del caso, el resultado esperado, el resultado obtenido y el estado de la prueba

test_tree_height() #se llama a la funcion test_tree_height para ejecutar las pruebas y mostrar los resultados
