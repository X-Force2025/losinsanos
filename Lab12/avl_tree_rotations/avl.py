class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height of a new node is 1

class AVLTree:
    def get_height(self, node):
        """Helper method to safely get the height of a node."""
        return node.height if node else 0

    def update_height(self, node):
        """Update height of a node based on its children's heights."""
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, z):
        """🔄 Perform left rotation on node z."""
        y = z.right                # Step 1: Identify new root (right child of z)
        T2 = y.left                # Step 2: Temporarily save y's left subtree

        y.left = z                 # Step 3: Rotate
        z.right = T2               # Step 4: Assign T2 as z's new right child

        self.update_height(z)      # Step 5: Update heights bottom-up
        self.update_height(y)

        return y                   # Return new root of the subtree

    def rotate_right(self, z):
        """🔁 Perform right rotation on node z."""
        y = z.left                 # Step 1: Identify new root (left child of z)
        T3 = y.right               # Step 2: Temporarily save y's right subtree

        y.right = z                # Step 3: Rotate
        z.left = T3                # Step 4: Assign T3 as z's new left child

        self.update_height(z)      # Step 5: Update heights bottom-up
        self.update_height(y)

        return y                   # Return new root of the subtree
