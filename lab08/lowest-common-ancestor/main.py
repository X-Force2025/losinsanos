class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right