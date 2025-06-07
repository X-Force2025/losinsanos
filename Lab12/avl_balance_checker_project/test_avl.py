# 🧪 Unit tests for AVL balance checking
from avl import AVLNode, AVLTree

def test_is_avl_balanced():
    avl = AVLTree()

    # ✅ Test 1: Balanced tree
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1 (Balanced):", avl.is_avl_balanced(root) == True)

    # ⚠️ Test 2: Manually unbalanced tree
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2 (Unbalanced):", avl.is_avl_balanced(unbalanced) == False)

    # 🌱 Test 3: Empty tree should be considered balanced
    print("🧪 Test 3 (Empty tree):", avl.is_avl_balanced(None) == True)

    # 📉 Test 4: Deep imbalance to the right
    deep_unbalanced = AVLNode(10)
    deep_unbalanced.right = AVLNode(20)
    deep_unbalanced.right.right = AVLNode(30)
    deep_unbalanced.right.right.right = AVLNode(40)
    print("🧪 Test 4 (Deep imbalance):", avl.is_avl_balanced(deep_unbalanced) == False)

    # 🏗️ Test 5: Full AVL compliant tree
    root = None
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root = avl.insert(root, val)
    print("🧪 Test 5 (AVL Compliant):", avl.is_avl_balanced(root) == True)

# 🚀 Run all tests
if __name__ == "__main__":
    test_is_avl_balanced()
