from avl_tree import AVLTree

if __name__ == "__main__":
    tree = AVLTree()
    root = None
    for value in [15, 10, 20, 25, 30]:
        root = tree.insert(root, value)
    print("In-order traversal:")
    tree.inorder(root)
