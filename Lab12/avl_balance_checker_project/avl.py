# 📦 AVL Tree implementation with balance checker
class AVLNode:
    def __init__(self, key):
        # Initialize a new node with the given key
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height starts at 1 for leaf node

class AVLTree:
    def get_height(self, node):
        # Return height if node exists, otherwise return 0
        return node.height if node else 0

    def update_height(self, node):
        # Update height using the max height of left and right children
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, z):
        # Perform left rotation (used for rebalancing)
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        # Perform right rotation (used for rebalancing)
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, node, key):
        # Insert a new key into the AVL Tree and rebalance
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        self.update_height(node)

        # Calculate balance factor
        balance = self.get_height(node.left) - self.get_height(node.right)

        # Rebalance tree if necessary
        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)  # LL case
            else:
                node.left = self.rotate_left(node.left)  # LR case
                return self.rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)  # RR case
            else:
                node.right = self.rotate_right(node.right)  # RL case
                return self.rotate_left(node)

        return node

    def is_avl_balanced(self, root):
        """
        📏 Check if tree is AVL-balanced:
        Ensures every node has balance factor in [-1, 1]
        """
        def check(node):
            if not node:
                return True, 0  # Base case: balanced, height 0

            # Check balance of left subtree
            left_balanced, left_height = check(node.left)

            # Check balance of right subtree
            right_balanced, right_height = check(node.right)

            # Node is balanced if both subtrees are and height difference is within 1
            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            return balanced, 1 + max(left_height, right_height)

        return check(root)[0]
