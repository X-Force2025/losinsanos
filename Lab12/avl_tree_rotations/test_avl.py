from avl import AVLNode, AVLTree

def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z.height = 3
    z.right.height = 2
    z.right.right.height = 1
    z = tree.rotate_left(z)
    print("🧪 Test 1:", z.key == 20 and z.left.key == 10 and z.right.key == 30)

    # Test 2: Right Rotation
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z.height = 3
    z.left.height = 2
    z.left.left.height = 1
    z = tree.rotate_right(z)
    print("🧪 Test 2:", z.key == 20 and z.left.key == 10 and z.right.key == 30)

    # Test 3: Heights after rotation
    print("🧪 Test 3:", z.height == 2 and z.left.height == 1 and z.right.height == 1)

    # Test 4: Structure after rotation
    print("🧪 Test 4:", z.left.left is None and z.left.right is None)

    # Test 5: More structure validation
    print("🧪 Test 5:", z.right.left is None and z.right.right is None)

# Run tests
if __name__ == "__main__":
    test_rotations()
