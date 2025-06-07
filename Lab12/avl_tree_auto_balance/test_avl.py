from avl_tree import AVLTree

def test_avl_insert():
    avl = AVLTree()

    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1 (RR):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print("🧪 Test 2 (LL):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 3 (LR):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 4 (RL):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 5 (Balanced):", end=" ")
    avl.inorder(root)
    print()

if __name__ == "__main__":
    test_avl_insert()
