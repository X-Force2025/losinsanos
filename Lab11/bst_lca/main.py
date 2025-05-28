class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def build_from_list(self, values):
        for val in values:
            self.insert(val)

    def find_lca(self, val1, val2):
        """🧬 Find lowest common ancestor of two values in the BST"""
        current = self.root
        while current:
            if val1 < current.val and val2 < current.val:
                current = current.left  # 👈 Both values in left subtree
            elif val1 > current.val and val2 > current.val:
                current = current.right  # 👉 Both values in right subtree
            else:
                return current.val  # 🌟 This is the LCA
        return None  # In case values are not present

def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# 🚀 Run all tests
test_find_lca()

