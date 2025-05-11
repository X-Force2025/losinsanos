from vertical_traversal import BinaryTree, vertical_order_traversal  


def test_vertical_order_traversal():  
    
    print("Running tests for vertical_order_traversal...")  
   

    tree1 = BinaryTree()  
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])  
    
    assert vertical_order_traversal(tree1.root) == [[4], [2], [1, 5], [3], [6]]  
 

    tree2 = BinaryTree()  
    tree2.build_tree_from_list([1, 2, None, 3])  
  
    assert vertical_order_traversal(tree2.root) == [[3], [2], [1]]  
  

    tree3 = BinaryTree()  
    
    assert vertical_order_traversal(tree3.root) == []  
    

    tree4 = BinaryTree()  
    tree4.build_tree_from_list([1])  
    
    assert vertical_order_traversal(tree4.root) == [[1]]  
    # Verifica que el recorrido contenga solo ese nodo

    tree5 = BinaryTree()  
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])  
    # Construye un árbol binario completo:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    assert vertical_order_traversal(tree5.root) == [[4], [2], [1, 5, 6], [3], [7]]  
    # Verifica el recorrido vertical esperado

    print("✅ All test cases passed.")  
    # Muestra un mensaje si todas las pruebas son exitosas

test_vertical_order_traversal()  
# Llama a la función de pruebas para ejecutarlas
