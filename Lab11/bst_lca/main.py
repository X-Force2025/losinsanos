class TreeNode:
    """A node in a binary search tree"""
    def __init__(self, val):
        # Store the value of the node
        self.val = val
        # Initialize left child to None
        self.left = None
        # Initialize right child to None
        self.right = None

def build_bst(values):
    """Helper function to build a BST from a list of values"""
    # If the list is empty, return None
    if not values:
        return None

    # The first value becomes the root
    root = TreeNode(values[0])

    # Insert the rest of the values into the BST
    for val in values[1:]:
        insert_into_bst(root, val)

    # Return the root of the BST
    return root

def insert_into_bst(root, val):
    """Insert a value into the BST"""
    # If the value is less than the current node's value
    if val < root.val:
        # Go left if there is a left child
        if root.left:
            insert_into_bst(root.left, val)
        else:
            # Otherwise, insert the new node here
            root.left = TreeNode(val)
    else:
        # If the value is greater or equal, go right
        if root.right:
            insert_into_bst(root.right, val)
        else:
            # Otherwise, insert the new node here
            root.right = TreeNode(val)

def find_lca(root, val1, val2):
    """Find lowest common ancestor of two values in a BST"""
    # Traverse the tree while the current node is not None
    while root:
        # If both values are smaller, go left
        if val1 < root.val and val2 < root.val:
            root = root.left
        # If both values are larger, go right
        elif val1 > root.val and val2 > root.val:
            root = root.right
        else:
            # One value is on the left and the other on the right,
            # or one is equal to the root → this is the LCA
            return root.val
    # If no LCA found (should not happen in proper BST with valid input)
    return None

# ✅ Test cases
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # Root as LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # Subtree LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # Ancestor relationship
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)                    # Same node
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)        # Leaf nodes
