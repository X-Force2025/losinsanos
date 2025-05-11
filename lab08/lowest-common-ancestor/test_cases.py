from main import TreeNode, lowest_common_ancestor
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

lca = lowest_common_ancestor(root, 5, 1)
print("LCA of 5 and 1:", lca.val)  # Output: 3

lca = lowest_common_ancestor(root, 6, 4)
print("LCA of 6 and 4:", lca.val)  # Output: 5