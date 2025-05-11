from balance_bst import BinarySearchTree, balance_bst, print_tree_inorder

def test_balance_bst():
    print("Ejecutando casos de prueba para balance_bst...")

    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)

    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)

    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)

    bst4 = BinarySearchTree()

    bst5 = BinarySearchTree()
    bst5.insert(42)

    for i, tree in enumerate([bst1, bst2, bst3, bst4, bst5], start=1):
        balanced = balance_bst(tree)
        original_inorder = tree.inorder()
        balanced_inorder = print_tree_inorder(balanced.root)
        assert original_inorder == balanced_inorder, f"❌ Error en el caso {i}"
        print(f"✅ Caso {i} correcto. Inorder: {balanced_inorder}")

test_balance_bst()
