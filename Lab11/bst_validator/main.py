class TreeNode:
    """A node in a binary tree"""
    def __init__(self, val):
        # Initialize the node with a value
        self.val = val
        # Left child is initially None
        self.left = None
        # Right child is initially None
        self.right = None

def is_valid_bst(root):
    """
    Check if a binary tree is a valid Binary Search Tree (BST)
    using helper function with initial min and max bounds.
    """
    return validate(root, float('-inf'), float('inf'))

def validate(node, min_val, max_val):
    """
    Recursive helper function to validate the BST property.
    Ensures all nodes follow the rule:
    - Left subtree values < node value
    - Right subtree values > node value
    """
    if not node:
        # An empty subtree is valid
        return True

    if not (min_val < node.val < max_val):
        # Current node value violates the BST property
        return False

    # Recursively validate the left subtree
    left_is_valid = validate(node.left, min_val, node.val)

    # Recursively validate the right subtree
    right_is_valid = validate(node.right, node.val, max_val)

    # The tree is valid only if both subtrees are valid
    return left_is_valid and right_is_valid

# ✅ Test cases

# Test 1: Valid BST
#     2
#    / \
#   1   3
tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)
# Expected output: True
print(is_valid_bst(tree1) == True)  # ✅ True

# Test 2: Invalid BST
#     5
#    / \
#   1   4
#      / \
#     3   6
# 4 is not valid because it's less than 5 but on the right
tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)
# Expected output: False
print(is_valid_bst(tree2) == False)  # ❌ False

# Test 3: Valid larger BST
#      10
#     /  \
#    5    15
#        /  \
#      12    20
tree3 = TreeNode(10)
tree3.left = TreeNode(5)
tree3.right = TreeNode(15)
tree3.right.left = TreeNode(12)
tree3.right.right = TreeNode(20)
# Expected output: True
print(is_valid_bst(tree3) == True)  # ✅ True

# Test 4: Invalid BST (left child is greater than root)
#     10
#    /  \
#   12   15
# 12 is invalid as left child of 10
tree4 = TreeNode(10)
tree4.left = TreeNode(12)
tree4.right = TreeNode(15)
# Expected output: False
print(is_valid_bst(tree4) == False)  # ❌ False
